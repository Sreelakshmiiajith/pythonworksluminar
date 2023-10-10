text="ABBCDCE"
wc={}
duplicate_list=[]
for ch in text:
    if ch in wc:
        duplicate_list.append(ch)
    else:
        wc[ch]=1
print(duplicate_list[1])