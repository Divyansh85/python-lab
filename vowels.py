st=input("enter a sentence")
vowels=['a','A','e','E','i','I','o','O','u','U']
v=c=ws=dig=co=0
for i in st:
    if i in vowels:
        v=v+1
    elif i.isspace():
        ws=ws+1
    elif i.isdigit():
        c=c+1
    elif i.isalpha() and i not in vowels:
        co=co+1
print(f"""
          vowels occur {v} times
          digit occurs {c} times
          whitespace occurs {ws} times
          consonants occurs {co} times""")        
        
