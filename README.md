# Anime Game Multilingual Data

Collection of multilingual language data from anime games stored in parquet format.

Jupyter notebook is used to generate the data from `GAMEDATA`. 

 - [Arknights](#arknights) 139428 rows
 - [Honkai Star Rail](#honkai-star-rail) 60826 rows
 - [Genshin Impact](#genshin-impact) 237530 rows

## Arknights

Language: en ja zh

> https://www.kaggle.com/datasets/toshihikochen/arknights-en-ja-zh

 - ArknightsStory.parquet: 139428 rows

Example:

|en|ja|zh|
|---|---|---|
|"In the Grand Knight Territory, Margaret asks a..."|大騎士領内。祖父の墓参りから戻ったマーガレットが過去について老騎士らに問う。一方荒野では、旧...|大骑士领内，给祖父扫墓归来的玛嘉烈问起旧事。荒野上，告别了旧友的玛恩纳和托兰谈论前路。|
|Deszcz the attorney's business trip is heavily...|車の故障により、弁護士デーシュットの予定は大幅に遅れていた。自分のせいで叩き売られようとして...|由于车辆意外故障，律师黛丝特的行程严重耽搁。这个即将因她而被低价卖掉的村庄留宿她一晚，她看见...|
|Flametail and Ashlock head for border city Dzw...|国境都市ズウォネクを訪れたフレイムテイルとアッシュロックは、現地の感染者が扇動されていること...|焰尾和灰毫前往边境城市茨沃涅克，发现此地的感染者正受人煽动。唯一与她们友善沟通的感染者被迫背...|
|"Laying low in Dzwonek, Szewczyk gets dragged i..."|人目を忍ぶためズウォネクへ越してきたシェブチックは、学校帰りの息子を迎えに行く途中で爆発事件...|搬到茨沃涅克避风头的瑟奇亚克只是去接儿子放学，却被卷入一场爆炸之中。|
|"His plot revealed, Czcibor heads down a path o..."|陰謀が暴かれ、後戻りできないことを悟った騎士団長シチボルは、自らの意地を通すことを決意する。...|阴谋败露，自知没有回头路的骑士团长切斯柏一意孤行，而玛恩纳等在他前去拦截刺杀目标的路上。|
|...|...|...|
|"To a certain extent, it also sends a sort of m..."|そして他のブラッドブルードに「この者は妾の庇護を受けている」といったメッセージを伝える役割もある。|当然某种程度上，也向其他血魔传达了“此人受我保护”这样的讯息。|
|Do you display your companionship in such a ma...|あなたもそういう方法で友情を表現するのか、ブラッドブルード？|你也用这种方式表现友谊吗，血魔？|
|"Of course, if you're willing to sign on a disc..."|もちろん、そなたらが免責事項にサインをして妾の実験に参加してくれるというのであれば、妾は断り...|当然你们要是愿意在免责声明上签下名字参加我的实验，我也是不会拒绝的啦。|
|I think I gotta go to rehearsal too. Me and Mu...|あたしもリハーサルしなきゃ……マドロックさん、行きましょう。|我好像也要排练来着，泥岩我们一起走吧。|
|"Wa—Wait, you can still participate, even if yo..."|ま、待たぬか！　サインはせずとも実験には参加してよいのだぞ、行くな！|等，等等啊，不签免责声明也可以直接来参加实验啊，别走！|

## Honkai Star Rail

Language: en ja zh

 - StarRailTextMap.parquet: 60826 rows

|en|ja|zh|
|---|---|---|
|Chinese|中国語|汉语|
|English|英語|英语|
|Japanese|日本語|日语|
|Korean|韓国語|韩语|
|Attachments|メール添付|邮件附件|
|...|...|...|
|1. (The following chapter requires payment to ...|1、（次のページ）（読み続ける）|1、（以下章节需付费阅读）（结束选择）|
|2. (Put the novel down) (Option end)|2、（小説をおろす）（選択を終わらせる）|2、（放下小说）（结束选择）|
|Energy Regeneration Rate can boost the amount ...|EP回復率はキャラクターのスキル発動、敵の殲滅、攻撃を受けた時に獲得するEPをアップさせるこ...|能量恢复效率能够提高角色在施放技能、消灭敌人、受到攻击等行为时获取的能量值。|
|A higher rate means faster energy regeneration.|この数値が高いほど、キャラクターのEP回復がはやくなる。|这个数值越高，角色能量恢复得越快。|
|"However, certain Energy-Regenerating effects w..."|一部の味方のEP回復効果によって回復したEPはEP回復率の影響を受けない。|部分恢复我方目标能量的效果所恢复的能量值不会受到能量恢复效率的影响。|

## Genshin Impact

> https://www.kaggle.com/datasets/toshihikochen/genshin-impact-ja-zh

Language: en ja zh

 - GenshinReadable.parquet: 10410 rows
 - GenshinSubtitle.parquet: 170 rows
 - GenshinTextMap.parquet: 226950 rows

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

# How to load parquet file

```python
import pandas as pd
df = pd.read_parquet('*****.parquet')
```
you might need to install `pyarrow` first.

# Announcement

> Data is for personal use only. Please DO NOT use it for commercial purposes. 

> 小孩子不懂事，上传着玩的 :)
