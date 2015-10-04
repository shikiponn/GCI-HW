#coding:utf-8
import MeCab
import math
import matplotlib.pyplot as plt
import numpy as np
keywords = []
tweets = ['昨夜は気仙沼二郎と初タッグ\n\nそして今日はメンズテイオーと久々のタッグ\n\nみちのくプロレスを離れて１０数年\n\nかつての同志達との巡り合わせ\n\n俺の根底にはみちのくプロレスがある\n\n久々のメンズテイオーとの融合は何が生まれるか\n\n楽しみです\n #kdojo #michipro', '何気に気仙沼二郎とタッグ組むのは初めてかもと言うことに気付いた\n\n高校時代からの付き合いだからもう25年の付き合い\n\n同期タッグ楽しみます\n\n＃michipro https://t.co/NUMQm9jijb', '6月4日＆11日深夜！ 高橋裕二郎選手がフジテレビの『EXILE CASINO JP』に再び登場!! http://t.co/Mk6Xe5KHLF #njpw http://t.co/9AAnQbvQ9x', 'もしかして二郎本2冊？', 'RT @ka_natuki: ラーメン二郎 おーぷん待ち\nしんやっちょ\nhttp://t.co/IaVsNiDUMr\n放送許可したんかな、次郎は放送ダメと聞いたはずなんだが。。。 http://t.co/40X6fWCh1e', '二郎系のラーメンとか見過ぎたせいか、にんにく入れればなんでもうまくなると錯覚している気がする', 'http://t.co/SQA0YU2iyK デカ盛りで有名な『ラーメン二郎』に公式ソングが誕生！\u3000ひばりヶ丘店で聴けるらしい', '@Pingu_bot 二郎', '二郎きてるぞおおおおおお', 'RT @kgky_9: ラーメン二郎\nトッピングの注文が難しい\n敷居が高い\n高カロリー\n\nスターバックス\nトッピングの注文が難しい\n敷居が高い\n高カロリー\n\n俺からしたらお男が二郎いくのは女がスタバ行くのと変わんねーよ！！！！', '若松二郎なう。', '昼飯。郎郎郎という二郎インスパイアに入るつもりだったが、12時にならないと開かないので、こっちに。 (@ 麺や 樽座 子安町店 in 八王子市, 東京都) https://t.co/fU7AH460PL', '二郎並んでたら前に並んでるのが高校の時に辞めた部活の先輩だった(めっちゃ気まずい)', '偉くなるか、ならないか。それは時の運だ。でも、絶対に人に迷惑をかけるな。そして、嘘をつくな。この2つを守れば人間はそれでいい\u3000／\u3000ｂｙ\u3000小津安二郎', 'RT @takam777: 昨夜は気仙沼二郎と初タッグ\n\nそして今日はメンズテイオーと久々のタッグ\n\nみちのくプロレスを離れて１０数年\n\nかつての同志達との巡り合わせ\n\n俺の根底にはみちのくプロレスがある\n\n久々のメンズテイオーとの融合は何が生まれるか\n\n楽しみです\n #kdo…', '東電株主代表訴訟: ＜お勧め本＞明���昇二郎『刑事告発東京電力 ルポ福島原発事故』金曜日刊。http://t.co/VffJFBSUzF http://t.co/h0qQidGo4a', '二度と食いたくたないって言ったのに二郎食いたい', '@wtnbkzk10 @shin505 神奈川予選と関内二郎かな 笑', '藤二郎、TLの監視は怠らないようにして', 'ランチらうめん。二郎系😁 http://t.co/iKHJszqz5q', '二郎兄もお変わりなく。親父殿が倒れたと聞いているが、今どちらに？', 'http://t.co/WzkhRkPKlL 本日放送「エンカメ」で友近が冠二郎にドッキリ決行', '@karonn_rosu デブに対するヘイト値が一気に上がった一日だったわ。悔しいから今日イベント行く前に二郎の野菜増しラーメン食べてデブになってから行こうかな＞＜', '二郎、おい！飯だ、行こうぜ。', '一杯の二郎', '@ryota_jiro そうなんだぁ〜 羨ましいっす♪代謝良くする秘訣は・・・毎日二郎食べる事ですか？(笑)', '近所の二郎系ラーメンを食べに行く', 'RT @habomaijiro: 平成27年6月6日土曜日、ラーメン二郎大宮店、大ラーメン+味付ウズラ+味付ウズラ アブラカラメ生姜900YEN\n今日の麺、もっと茹でれば、俺好み\n安定の、味付ウズラ、塩気よし\nカラメ増し、生姜加えて、ウマい汁\n完飲。 ごっそさんです。 http…', '二郎の行列やっっべんだwww', '注目のシャウトです。\n\nにーぼ… らーめん公kimi\u3000板倉店\u3000※二郎系インスパイア [+]Photo\nhttp://t.co/knvWIcQvPv http://t.co/RwVFJxT4x1', 'バイトも人に会う予定もないので心置きなく二郎行けるな。', 'いせやさんの榎木津礼二郎初登場シーンとかめちゃくちゃ見てみたい 京極堂シリーズの映像化はもう絶望的なんだろうか… 百器 百器だけでも 百器ならささき榎木津が動いてるの見たい ささき榎木津はラジオドラマのときの笑い方がすごいイメージ通りの榎さんだし笑顔が絶対にかわいい', "I'm at ラーメン二郎 会津若松駅前店 in 会津若松市, Fukushima https://t.co/bsTUYbUTSU", '小金井二郎行くか～', '朝夕食抜く勢いで、二郎インスパイア系にきてみた', '待たせてる身分で二郎行くとは', 'RT @takam777: 昨夜は気仙沼二郎と初タッグ\n\nそして今日はメンズテイオーと久々のタッグ\n\nみちのくプロレスを離れて１０数年\n\nかつての同志達との巡り合わせ\n\n俺の根底にはみちのくプロレスがある\n\n久々のメンズテイオーとの融合は何が生まれるか\n\n楽しみです\n #kdo…', '@mikimiki_prpr 奈緒二郎の方も買っとく？', '俺が願った世界\u3000http://t.co/08r002kR2l\u3000\u3000\u3000\u3000\u3000ラーメン二郎 wiki\u3000http://t.co/bXdmecPNAj\u3000#_ラーメン二郎', '相模大野にぃ、ラーメン二郎、あるらしいですよ', 'RT @nikatatsublog: http://t.co/KE4vyTOoou 「ラーメン二郎 大宮店」で、ラーメン。 #jiro #ramen http://t.co/pM0c8Qag2S', 'http://t.co/F88Hs31A36 二郎みたいで二郎じゃない。ガッツリ系「野郎ラーメン」の店舗レビューまとめ', '@ginchan817 \nまーた二郎かと思ったら笑っちゃいましたw', '新潟市西区にニューオープン「麺マッチョ 新大店」\nラーメンは二郎インスパイア系のガッツリとした一杯です。\nhttp://t.co/XK9KyTdwYo #二郎インスパイア', 'RT @sasakiyusuke: 映画にとってインターネットとは何か（6）Jホラー・ネットロア・モビリティ  - qspds996 http://t.co/HSZp79I9KJ 第6回です。インターネット×ホラーの二大巨頭の作品、永江二郎『２ちゃんねるの呪い 劇場版』と福田陽…', 'RT @485_485: デスノートを福田雄一が監督したら月は山田孝之だしLは柳楽優弥だし松田はムロツヨシでリュークは佐藤二郎。', 'プレイヤー名五郎にしようかと思ったんだけど気に入った妖がなんか爽やかだからとりあえず音二郎にしたよね', '関内二郎並んでるけど、列クソ長いし、クソ暑い', '今日誰かムタヒロか二郎一緒に行ってくれる心優しい人はいませんか！', '二郎行かねーよ！！', 'オススメの本。『二郎に学ぶ経営学』そう、私はジロリアンである！二郎食べたいよォォォォォ！！！', 'これから二郎とかもうびしょ濡れ…', '平成子門の高野二郎さんが歌リハ中！\n\n本日13時〜阿佐ヶ谷ロフトA\n【ミュージックファイルフェスタVol.6】子門真人コンピCDの不破了三さん音源解説、映画版電人ザボーガー主題歌の高野二郎さんによる唱法解説とミニミニライヴ！歌えます！\nhttp://t.co/EQqFwTaaqo', 'RT @uchikoget1: ラーメン二郎 めじろ台法政大学前店\n小ラーメン¥700＋つけ麺（麺少なめ・野菜・白アブラ）¥150\n\n練習で疲れきった体を癒すべく訪問❗️ 写真はミスりましたが味はミスりません👍\n野菜高騰でも相変わらずのキャベツ率✨ 頭が下がります🙇 http:…', 'シャークは約束通り、この時代へ来る。何十年前の約束だが、絶対に破ったりはしない。そういう男だよ。（宗二郎）【第7話\u3000追憶・1960】', '二郎コピペとか見たら余計にいけないｗｗｗ', '餅みかんつかさてとちゃん計4名 (@ ラーメン二郎 中山駅前店 in 横浜市, 神奈川県) https://t.co/qGb1hMgo52', '幼獣５：一郎くんをちょっと撫でて、ほんの少しだけ笑う二郎ちゃんの笑顔が優しすぎて胸が痛い。 #マメシバ一郎', '@kurotann0822 \nRTどうも～山の下の健の二郎が\nお迎え来たで←\nhttps://t.co/livuf0KBh8', 'しまじろうは二郎インスパイア', "I'm at ラーメン二郎 仙台店 in 仙台市, 宮城県 http://t.co/kyGfQjtZ9I", '失恋の名言：男女の仲というのは、夕食を二人っきりで三度して、 それでどうにかならなかったときはあきらめろ。 小津安二郎', '二郎食いてえ', 'http://t.co/vch4R7cojl 中毒必至！ガッツリマシマシコールはまさに弁当界の二郎「わせ弁」', '男女の仲というのは、夕食を二人っきりで三度して、それでどうにかならなかったときはあきらめろ。\u3000◆小津安二郎', '@Y_K_0524_xxx うわ、ポニョ二郎', '@Pingu_bot 二郎', 'RT @haruka_26: ちなみに調べたが二郎ラーメン(スープ抜き)が1371kCalでスタバの新作、チョコレートクランチフラペチーノventiとほぼ同じ。\n神座のラーメンが558kCalでshortとほぼ同じでした。\nさあ、これを見て何か言いたい事は？ http://t.…', 'ちなみに調べたが二郎ラーメン(スープ抜き)が1371kCalでスタバの新作、チョコレートクランチフラペチーノventiとほぼ同じ。\n神座のラーメンが558kCalでshortとほぼ同じでした。\nさあ、これを見て何か言いたい事は？ http://t.co/28G1vgT6fx', '関内二郎行きたい(行くとは言っていない', '二郎で脂少なめを頼んだらその通りに来るけど、デブに脂少なめを頼んでもその通りにならない現象', 'http://t.co/QGR71qFGmI デカ盛りで有名な『ラーメン二郎』に公式ソングが誕生！\u3000ひばりヶ丘店で聴けるらしい', '@Da_iCE_SOTA 想太くん…やっと二郎に行けたのに休みでした。もう立ち直れないです＿|￣|○', '二郎の悪循環\u3000aaaa614_5 http://t.co/7VSp6bu4X2', '@yuhei0430 おっ、二郎行くんか', '二郎の悪循環\u3000aaaa614_5 http://t.co/UmuNgKYMjD', '二郎食うか…', '二郎わず', 'ラーメン二郎 会津若松駅前店\n開店11:00 10人程の並びです🌟 http://t.co/bbGXh9SacX', '青春18きっぷで札幌二郎計画、さすがに無謀な気がして悩んでいる', '２周年を迎えたラーメ���二郎仙台店がまだまだ熱い - NAVER まとめ http://t.co/royjdgiQRw #ラーメン二郎 #sendai #仙台 #宮城 #miyagi #二郎 #jiro #matome #naver #まとめ', '関内二郎行きてぇ(なお', 'ラーメン二郎横浜関内付近を通過中', '二郎って１時くらいにいってもええんかな？', '二郎戻し(☝ ；o；)☞@_yamakou_', '@toro1006t 二郎、、写真を見ただけで無理と思う。\n何事も少しで充分です。', 'http://t.co/rDbSu9HEkc\n06-06のラーメンランキング\n1位\nラーメン二郎 池袋東口店\n2位\n麺処 花田\nばんから 池袋東口店\n3位\n屯ちん 池袋本店', 'RT @koichi011: "公明も戦争法強行へＺ旗＜本澤二郎の「日本の風景」（２００７） : 「ジャーナリスト同盟」通信" #feedly http://t.co/ylDBtJf77d', 'とても二郎系が食べたい気分です', '待っててね二郎さん！！！菜穂子さん！！！(テンションMAX', 'ラーメン二郎\n・最早それはラーメンとは言えぬ独立した味\n・カロリーが高い\n・糖分、タンパク質、脂肪のバランス栄養食\n\nスタバの新作\n・最早それはコーヒーとは言えぬ独立した味\n・カロリーが高い\n・糖分、タンパク質、脂肪のバランス栄養食\n\nつまり、ラーメン二郎＝スタバ', 'RT @takam777: 昨夜は気仙沼二郎と初タッグ\n\nそして今日はメンズテイオーと久々のタッグ\n\nみちのくプロレスを離れて１０数年\n\nかつての同志達との巡り合わせ\n\n俺の根底にはみちのくプロレスがある\n\n久々のメンズテイオーとの融合は何が生まれるか\n\n楽しみです\n #kdo…', 'RT @takam777: 昨夜は気仙沼二郎と初タッグ\n\nそして今日はメンズテイオーと久々のタッグ\n\nみちのくプロレスを離れて１０数年\n\nかつての同志達との巡り合わせ\n\n俺の根底にはみちのくプロレスがある\n\n久々のメンズテイオーとの融合は何が生まれるか\n\n楽しみです\n #kdo…', '昨日二郎さん食べたけど夜ごはん食べないで寝たら1キロ痩せてたヾ(๑ㆁᗜㆁ๑)ﾉ"\nお出かけして夜ごはん控えめにするといつも痩せてる気がする…？？', '二郎vsスタバ', 'スタバの新商品を「ラーメン2杯分」みたいに煽ってるけど、ラーメン絡める前に二郎・二郎系ラーメンのことをツッコメよ。', 'ラーメン二郎 歌舞伎町店の大盛りチャーシューダブル＋野菜増し増し (8:54) http://t.co/jXqvHw0E7p #sm26428770 ワロタｗ', "I'm at ラーメン二郎 大宮店 in さいたま市, 埼玉県 https://t.co/v7KtKa5E2A", '@machan1964 \n城下町の二郎です(≧∇≦)', 'リスポーン地点 (@ ラーメン二郎 仙台店 in 仙台市, 宮城県) https://t.co/UOH8PhhqpR']


def extractKeyword(text):
    #extを形態素解析して、名詞のみのリストを返す"""
    tagger = MeCab.Tagger()
    encoded_text = text.encode('utf-8')
    tagger.parse('')    #python3のバグ回避用　cf http://www.trifields.jp/how-to-use-mecab-in-ubuntu-14-04-and-python-3-1196
    node = tagger.parseToNode(text)
    wordCount = {}
    keywords = []
    while node:
        hinshi = node.feature.split(",")[0]
#         print(hinshi)
        if hinshi  == "動詞" or hinshi == "名詞":
            keywords.append(node.surface)
            wordCount.setdefault(node.surface,0)
            wordCount[node.surface]+=1
        node = node.next
    return keywords, wordCount
print(tweets[0])
print(extractKeyword(tweets[0])[0])
print(extractKeyword(tweets[0])[1])
results = []    #辞書のリスト
allwords = []   #全単語のユニークリスト
for tweet in tweets :
    result = extractKeyword(tweet)[1]
    print(result)
    results.append(result)
    for key in result:
        allwords.append(key)
set(allwords)
print(results[0])
print(allwords)


def tfdtf(allwords , texts):
    #全文書数
    D = len(texts)
    print(D)
    #idf
    idfs = {}
    for word in allwords:
        count = 0 
        for text in texts:
            if word in text:
                count += 1
        idf = math.log10((D/count))
        idfs[word] = str(idf)
    print(idfs)
    #TF
    list_tfs = []
    for text in texts:
        tfs = {}
        sigma = len(text)
#         print(text)
        for word in text:
            tf = (text[word]/sigma)
            tfs[word] = tf
#         print(tfs)
        list_tfs.append(tfs)
    #TF-IDF
    tfidf_list = []
    for tfs in list_tfs:
        tfidf_line = {}  
        for tf in tfs:
            cidf = float(idfs[tf])
            ctf = float(tfs[tf])
            ctfidf = cidf * ctf
            tfidf_line[tf] = ctfidf
        tfidf_list.append(tfidf_line)

    return(tfidf_list)
        
    
           
        
    
result = tfdtf(allwords, results)
nums = []
small = []
i=1
for row in result:
    for key in row:
        nums.append(row[key])
        if row[key] >= 0.4:
            print(i, ": ", key, ":", row[key])
            small.append(row[key])
            
    i+=1
small = sorted(small)
nums = sorted(nums)
length = np.arange(len(small))
print(nums)
nums = np.array(nums)
small = np.array(small)
plt.plot(length, small, "o")
plt.show()