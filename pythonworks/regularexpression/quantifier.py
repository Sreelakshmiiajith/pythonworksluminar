# from re import*
# text="aabbcaabdaaa"
# Pattern="a+" #one or more occurence of a
# Pattern="a*" #zero or more ocuurence of a
# Pattern="a{1,2}" #minimum one a and maxinum 2 a
# matcher=finditer(Pattern,text)
# for m in matcher:
#     print(m.group(),m.start())


# from re import*
# phone=input("enter your phone number:")
# rule="\d{10}"
# matcher=fullmatch(rule,phone)
# if(matcher==None):
#     print("invalid")
# else:
#     print("valid")

from re import*
variable=input("enter a variable")
rule="[a-zA-Z][\w_]"
matcher=fullmatch(rule,variable)
if(matcher==None):
    print("invalid")
else:
    print("valid")




