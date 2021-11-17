first=list(map(str,input()))
second=list(map(str,input()))
cou=0
for i in range(0,len(first)):
    if first[i] in second:
        cou=cou+1
if cou==len(first):
    print('anagram')
else:
    print('not anagram')


