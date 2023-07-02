# Anime Game Multilingual Language

Collection of multilingual language data from anime games stored in parquet format.

Jupyter notebook is used to generate the data from `GAMEDATA`. 

 - [Genshin Impact](#genshin-impact) 231514 rows
 - [Arknights](#arknights) 57191 rows

## Genshin Impact

> https://www.kaggle.com/datasets/toshihikochen/genshin-impact-ja-zh

Language: en ja zh

 - GenshinReadable.parquet: 10239 rows
 - GenshinSubtitle.parquet: 168 rows
 - GenshinTextMap.parquet: 221107 rows

Example:

|en|ja|zh|
|---|---|---|
|The long-wandering eccentric no longer thinks ...|長年放浪してきた傾奇者は、もうそのことを思い出さないだろう。|流浪多年的倾奇者已不会再想起它，|
|"But when he closes his eyes, he can still see ..."|しかし目を閉じると、たたら砂の月夜や炉火が見える。|但闭上双眼，却仍能看到踏鞴砂的月夜与炉火。|
|The kind young deputy said:|若く、心優しい副官が言った。|年轻仁厚的副官说：|
|"This gold ornament is a proof of identity gra..."|「この金の飾りは、将軍から授かった身分の証である。」|“这金饰是将军大人所赐身份之证，”|
|"But as you travel the world, please bear this..."|「世を渡り歩く時、やむを得ない場合を除き、」|“但你行走世间时，若非万不得已，”|
|...|...|...|
|"Sangonomiya was once an ocean abyss, until the..."|珊瑚宮は、最初は海溝だった。大蛇が渡来した際、渦が巻き上がった珊瑚が島になった。故に珊瑚宮の...|珊瑚宫者，初为海渊，后有大蛇渡来，盘桓而升涡流，塑珊瑚而成岛。是故珊瑚宫人名之“海祇岛”，盖...|
|The inhabitants of Watatsumi call themselves t...|海祇の人は海民と自称し、大蛇オロバシノミコトを祀る。海祇島に将軍奉行の位がなく、神宮を最高権...|海祇之人自称海民，奉大蛇远吕羽氏尊。海祇岛以神宫为高府，无将军奉行之畴。大小事务仰赖诸巫女，...|
|"During the Archon War, Her Excellency the Almi..."|往年魔神の混戦中、雷電大御所将軍様が稲妻全土を平定した。皆ひれ伏し、各々の地を治めた。事を起...|往年魔神混战，雷电大御所将军殿下定稻妻全土于一元，众皆震悚俯首，各安其位，或有直遭殄灭，再无...|
|"The war was brutal, and brought great sufferin..."|過酷な戦で民が苦しんだ。今のヤシオリ島で激しい戦闘が行われ、双方の被害が甚大だった。大御所殿...|战事酷烈，民生惨苦。两方鏖战今八酝岛，皆多有伤亡，大御所殿下之爱将天狗笹百合亦陨落其间。大蛇...|
|"Thereafter, Sangonomiya sent envoys to announc..."|この後、珊瑚宮は降伏し、稲妻幕府を大宗主とするようになった。|自此以后，珊瑚宫遣使降服，尊稻妻幕府为大宗主也。|

## Arknights

Language: en ja zh

> https://www.kaggle.com/datasets/toshihikochen/arknights-en-ja-zh

 - ArknightsStory.parquet: 57191 rows

Example:

|en|ja|zh|
|---|---|---|
|Operator Thorns accompanies Rhodes Island to S...|ロドス一行と共にシエスタに来たソーンズは、一日の休日を謳歌する。|干员棘刺随罗德岛来到汐斯塔，度过休闲一日。|
|"When the sun started to set, the Ægirians, far..."|日が沈みゆく中、エーギル人は異郷のビーチに佇んでいた。程なくして、未知の敵と遭遇する——|而当日落临近，离乡的阿戈尔人在沙滩旁，偶然遭遇了未知的敌人|
|Capone betrayed Gambino. Mostima rescued Bison...|カポネはガンビーノを裏切った。モスティマはバイソンを救い出した。そして鼠王は本当の姿を見せた...|卡彭背叛了甘比诺。莫斯提马救下了拜松。鼠王露出了真面目。龙门晚风轻拂。|
|"Bison and Mostima, while wandering around seem..."|悠々と街を歩くバイソンとモスティマは、飴屋の前を通りかかったところでマフィアに狙われてしまう...|优哉游哉的拜松与莫斯提马路过了一家糖果店，却也在此时被黑手党盯上。为了顺利摆脱追踪，拜松跳上...|
|"Yith is being watched by a certain Liberi, and..."|イースはあるリーベリに監視されており、そしてモスティマは以前から鼠王の存在を知っていた。 再...|伊斯遭到了某位黎博利的监视，而莫斯提马也早已知晓鼠王存在。重新汇合的企鹅物流众人得到了大帝的...|
|...|...|...|
|Preparation is always the first step of victory.|作戦前の周到な準備は、常に勝利への第一歩となる。|做好战前的准备永远都是胜利的第一步。|
|"Now then, I will be officially transferring th..."|じゃあ、危機契約————作戦コード「荒廃」に関して、正式にドクターに委任するよ。|那么，危机合约————代号荒芜行动，正式转交给博士。|
|"Subsequently, PRTS will collate all the releva..."|ここからはPRTSが関連資料の整理をしてくれるよ。もし何か分からないことがあったら管理画面で...|PRTS会做好后续的相关资料整理工作，如果还有疑问博士可以在管理界面进行再确认。|
|The operation has officially begun. I wish eve...|じゃあ始めよう。みんなどうか無事でね。|行动正式开始，祝大家一切顺利。|
|May we bring hope to this Catastrophe-stricken...|この多事多難な大地に、僕たちが希望をもたらしていこう。|愿我们能为这片多灾的大地带去希望。|

# How to load parquet file

```python
import pandas as pd
df = pd.read_parquet('*****.parquet')
```
you might need to install `pyarrow` first.

# Announcement

> Data is for personal use only. Please DO NOT use it for commercial purposes. 

> 小孩子不懂事，上传着玩的 :)
