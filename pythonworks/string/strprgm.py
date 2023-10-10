# name="theLumInarthe"
# print(name.casefold())
# print(name.capitalize())
# print(name.count("L"))
# print(name.startswith("Lu"))
# print(name.endswith("m"))

# print(name.isalpha())
# print(name.isdigit())
# print(name.isalnum())
# print(name.strip("21")) #remove specify string
# print(name.strip("the"))
# print(name.rstrip("the")) remove from right
# print(name.lstrip("r")) #remove from left
# # print(name.index("L")) #INDEX POSITION

# name="python is a scripting language"
# words=name.split(" ")

# for w in words:
#     print(w)
# for w in name:
#     if w in("a","e","i","o","u"):
#         print(w)

text="eight five sixt out"
vowels="a","e","i","o","u"
words=text.split(" ")
for w in words:
    if w.casefold().startswith(vowels):
        print(w)
       
