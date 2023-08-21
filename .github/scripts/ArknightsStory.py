import os
import subprocess


def callsh(command):
    status = subprocess.run(command, shell=True)
    status.check_returncode()
    print(status.stdout)


# git clone https://github.com/GDFSCJY/test-auto-update-anime-game-multilingual-data.git -b auto-update
callsh('git clone https://github.com/GDFSCJY/test-auto-update-anime-game-multilingual-data.git -b auto-update')
# cd update-anime-game-multilingual-data
os.chdir('test-auto-update-anime-game-multilingual-data')
# git submodule init GAMEDATA/ArknightsData
callsh('git submodule init GAMEDATA/ArknightsData')
# git submodule update --remote GAMEDATA/ArknightsData
callsh('git submodule update --remote GAMEDATA/ArknightsData')

# pip install sentence_transformers
callsh('pip install sentence_transformers')

from functools import partialmethod
from glob import glob
import numpy as np
import pandas as pd
import re
from tqdm import tqdm
import torch
from transformers import MT5TokenizerFast
from sentence_transformers import SentenceTransformer

# disable tqdm output, enable it when debug
tqdm.__init__ = partialmethod(tqdm.__init__, disable=True)

# load all en ja zh json file paths
en_story_path = 'GAMEDATA/ArknightsData/en_US/gamedata/story'
ja_story_path = 'GAMEDATA/ArknightsData/ja_JP/gamedata/story'
zh_story_path = 'GAMEDATA/ArknightsData/zh_CN/gamedata/story'

skip_count = 0
en_story_files, ja_story_files, zh_story_files = [], [], []
for zh_file in tqdm(glob(f'{zh_story_path}/**/*.txt', recursive=True)):
    en_file = zh_file.replace('zh_CN', 'en_US')
    ja_file = zh_file.replace('zh_CN', 'ja_JP')
    if not os.path.exists(en_file) or not os.path.exists(ja_file):
        skip_count += 1
        continue
    en_story_files.append(en_file)
    ja_story_files.append(ja_file)
    zh_story_files.append(zh_file)

print(f'Skip {skip_count} files, {len(en_story_files)} files left.')

# load all en ja zh txt file into df
# empty line should be removed
# should remove lines like: [some word]
regex = re.compile(r'^(\[[^\]]+\][\n]*)$')


def read_file(file_path):
    lines = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            if line == '':
                continue
            elif regex.match(line):
                continue
            lines.append(line)

    return lines


df = pd.DataFrame(columns=['en', 'ja', 'zh'])
pbar = tqdm(zip(en_story_files, ja_story_files, zh_story_files), total=len(en_story_files))
for en_file, ja_file, zh_file in pbar:
    # show filename on progress bar
    pbar.set_description(f'Processing {en_file}')

    en_story_text = read_file(en_file)
    ja_story_text = read_file(ja_file)
    zh_story_text = read_file(zh_file)

    if len(en_story_text) != len(ja_story_text) or len(en_story_text) != len(zh_story_text):
        print(f'Warning: length of {en_file} is not equal to {ja_file} or {zh_file}')
        print(f'length of en: {len(en_story_text)}, ja: {len(ja_story_text)}, zh: {len(zh_story_text)}')
        continue

    df = pd.concat([df, pd.DataFrame({
        'en': en_story_text,
        'ja': ja_story_text,
        'zh': zh_story_text})
    ], ignore_index=True)

# drop duplicate
df = df.drop_duplicates(subset=['en', 'ja', 'zh'], keep='first')
# remove name tag of dialog
# which is like: [...]   dialog, just keep dialog
regex = re.compile(r'^(\[[^\]]+\][ ]*)')
df['en'] = df['en'].apply(lambda x: regex.sub('', x))
df['ja'] = df['ja'].apply(lambda x: regex.sub('', x))
df['zh'] = df['zh'].apply(lambda x: regex.sub('', x))
# remove row with only punctuation
df = df[~df['en'].str.match(r'^[^\w\s]+$')]
df = df[~df['ja'].str.match(r'^[^\w\s]+$')]
df = df[~df['zh'].str.match(r'^[^\w\s]+$')]
# remove lines with only numbers
df = df[~df['en'].str.match(r'^\d+$')]
df = df[~df['ja'].str.match(r'^\d+$')]
df = df[~df['zh'].str.match(r'^\d+$')]

# remove lines that tokens is more than 256 or less than 1
tokenizer = MT5TokenizerFast.from_pretrained('google/mt5-small')

df['en_len'] = df['en'].apply(lambda x: len(tokenizer.tokenize(x)))
df['ja_len'] = df['ja'].apply(lambda x: len(tokenizer.tokenize(x)))
df['zh_len'] = df['zh'].apply(lambda x: len(tokenizer.tokenize(x)))

df = df[df['en_len'] <= 256]
df = df[df['ja_len'] <= 256]
df = df[df['zh_len'] <= 256]
df = df[df['en_len'] >= 1]
df = df[df['ja_len'] >= 1]
df = df[df['zh_len'] >= 1]

# remove lines that LaBSE score is less than 0.6 or more than 0.99
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = SentenceTransformer('sentence-transformers/LaBSE').to(device)

_batch, _scores = [], []
_bs = 4
for i, row in tqdm(enumerate(df.itertuples()), total=df.shape[0]):
    inputs = [row.en, row.ja, row.zh]
    _batch.extend(inputs)
    if (i+1) % _bs == 0 or i == df.shape[0]-1:
        embeddings = model.encode(_batch)
        # calculate score between each pair
        for j in range(embeddings.shape[0]//3):
            _scores.append(np.average([
                np.matmul(embeddings[j*3], embeddings[j*3+1].T),
                np.matmul(embeddings[j*3], embeddings[j*3+2].T),
                np.matmul(embeddings[j*3+1], embeddings[j*3+2].T)
            ]))
        _batch = []
df = df.assign(score=_scores)

df = df[df['score'] >= 0.6]
df = df[df['score'] <= 0.99]

# drop len and score column
df = df.drop(columns=['en_len', 'ja_len', 'zh_len', 'score'])

# save to parquet
df.to_parquet('../ArknightsStory.parquet', index=False)

# remove repository
os.chdir('../')
callsh('rm -rf test-auto-update-anime-game-multilingual-data')
