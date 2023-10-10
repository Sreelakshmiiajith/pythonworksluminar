# text="coffee"
# for ch in text:
#     if ch in["a","e","i","o","u"]:
#         print(ch)

text="coffee"
v_count=0
c_count=0
for ch in text:
    if ch in["a","e","i","o","u"]:
        v_count+=1
    elif ch!=" ": #elif ch not in[" ",":","."]
        c_count+=1
print("vowel count",v_count)
print("consonent_count",c_count)



    