
# from re import*
# text="abcdABCD7#e9fkI"
# pattern="[AaEeIiOouU]"
# matcher=finditer(pattern,text)

# for m in matcher:
#     if m.group().isalpha():
#         print(m.group())


#digits only
from re import*
text="abcd12kABC@#"
pattern="[^aeiou\W\d]"
# pattern="\D" #D expect digits  
# pattern="\w" #[a-zA-Z0-9]
# pattern="\W" #exepct alpha numeric
matcher=finditer(pattern,text)
for m in matcher:
    print(m.group(),m.start())
    