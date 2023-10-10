from re import*
f=open("C:\\Users\\91759\\Desktop\\pythonworks\\regularexpression\\data.txt")
phone_rule="\d{10}"
mail_rule="[\w]+@gmail.com"
phone_number=[]
mail_ids=[]
for line in f:
    words=line.rstrip("\n").split()
    for w in words:

        matcher1=fullmatch(phone_rule,w)
        matcher2=fullmatch(mail_rule,w)
        if matcher1!=None:
            phone_number.append(w)
        elif matcher2!=None:
            mail_ids.append(w)
print(phone_number)
print(mail_ids)
