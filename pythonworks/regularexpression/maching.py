# from re import*
# text="abababcab"
# matcher=finditer("abc",text)
# count=0

# for m in matcher:
#     print(m.start(),m.group())
#     count+=1
# print(count)




# from re import*
# text="abcdABCD7e9fk" #checks for digits
# matcher=finditer("[0-9]",text)

# for m in matcher:
#     print(m.start(),m.group())

# from re import*
# text="abcdABCD7e9fk" #checks for digits
# pattern="[a-zA-Z0-9]" #CHECK ALL ALFABETS
# matcher=finditer(pattern,text)

# for m in matcher:
#     print(m.start(),m.group())

from re import*
text="abcdABCD7#e9fkI" #checks for digits
pattern="[AaEeIiOouU]" #R^-EMOVES ONLY DIGITS 
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())




# from re import*
# text="abcdABCD7#e9fkI"
# pattern="[AaEeIiOouU]"
# matcher=finditer(pattern,text)

# for m in matcher:
#     if m.group().isalpha():
#         print(m.group())
    