sen=input('enter a sentence')
num=int(input('enter parts in to divide'))
if len(sen)%num==0:
    part=len(sen)//num
else:
    part=(len(sen)-len(sen)%num)//num
for i in range(0,len(sen),part):
    print(sen[i:i+part])
