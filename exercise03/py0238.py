'''红楼梦源文件我换了编码方式为utf-8'''
import jieba
import re
stop_words=["什么","一个","我们","那里","如今","你们","说道","知道","老太太","起来",
            '这里','知道','他们','众人','姑娘','一面','自己','只见','太太','不是',
            '没有','两个','怎么','出来','不知','这个','听见','这样','进来','咱们',
            '告诉','就是','东西','回来','只是','大家','老爷','只得','丫头','这些',
            '不敢','出去','所以','不过','的话','不好','姐姐','一时','过来','不能',
            '心里','如此','今日','银子','二人','几个','答应','还有','只管','一回',
            '说话','这么','那边','外头','这话','打发','自然','今儿','那些','罢了',
            '听说','小丫头','屋里','二爷','如何','问道','妹妹','看见','人家','不用',
            '媳妇','原来','一句','家里','一声','不得','到底','这会子','姊妹','进去'
]
with open("红楼梦.txt", "r", encoding='utf-8') as f:
    txt=f.read()
f.close()
#太多了就替换这么多了
txt=re.sub('奶奶','贾母',txt)
txt=re.sub('老太太','贾母',txt)
txt=re.sub('林黛玉','黛玉',txt)
txt=re.sub('林姑娘','黛玉',txt)
txt=re.sub('林妹妹','黛玉',txt)
txt=re.sub('凤姐儿','凤姐',txt)
txt=re.sub('王熙凤','凤姐',txt)
txt=re.sub('辣妹子','凤姐',txt)
txt=re.sub('宝二爷','贾宝玉',txt)
txt=re.sub('怡红公子','贾宝玉',txt)
txt=re.sub('绛洞花主','贾宝玉',txt)

words = jieba.lcut(txt)
counts = {}
for word in words:
    if word in stop_words:
        pass
    else:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)

for i in range(20):
    word, count = items[i]
    print("{0:<5}{1:>5}".format(word, count))
