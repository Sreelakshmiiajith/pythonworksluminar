text="ACDA"
wc={}
for ch in text:
    if ch in wc:
        print("print first recursive character is",ch)
        break
    else:
        wc[ch]=1
