range=int(input("enter a range:"))
num=int(input("enter a number"))
start=1
prev=0
current=1
print(prev)
print(current)
while(start<=range):
    sum=prev+current
    print(sum)
    prev=current
    current=sum

    
    

    # (prev,current)=(current,sum) 
    start+=1
