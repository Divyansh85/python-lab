st=input()
n=st.split()
new=''
for i in n:
    ct=st.count(i)
    if ct>=2:
        result=st.split(i)
for i in result:
    if i!=' ':
        new=new+i
print(new)        
