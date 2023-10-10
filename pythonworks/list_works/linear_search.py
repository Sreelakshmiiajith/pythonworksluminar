lst=[10,2,13,14,5]
element=int(input("enter a number:"))
i=0
limit=len(lst)
is_present=False
while(i<limit):
    current_value=lst[i]
    if current_value==element:
        is_present=True
        break
    i+=1
print(is_present)