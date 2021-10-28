first=input('enter string to edit')
second=input('enter string to search')
new=first.split(second)
newstr=''
for i in new:
    if i!=' ':
        newstr=newstr+i
print(newstr)        
        

