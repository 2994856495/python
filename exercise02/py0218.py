'''2、有一字符串，有字母、数字、空格、其它字符。
1) 统计单词个数。可以使用split()函数。可以用WORD的统计作为参考，
2) 统计每个字母出现次数。大小写为同一字母。使用字典来统计。
3) 统计出现的字母。大小写为同一字母。使用集合来统计。
The Mate X supports next-generation 5G networks and will cost 2,299 euros ($2,606) when released in the summer. 
'''
s="The Mate X supports next-generation 5G networks and will cost 2,299 euros ($2,606) when released in the summer."

kongge=len(s.split(" "))-1
print(kongge)
# 1 12dd edd
dict1={}
s1=s.lower()
for i in range(len(s1)):
    if s1[i].isalpha():
        if s1[i] in dict1:
            dict1[s1[i]]=dict1[s1[i]]+1
        else:
            dict1[s1[i]] = 1
print(dict1)

t=set(dict1.keys())
print(t)

