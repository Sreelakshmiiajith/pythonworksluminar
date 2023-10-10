length=int(input("enter a number:"))
num=int(input("enter a number:"))
start=1
prev=0
current=1
print(prev)
print(current)
for start in range(prev,current+1):
    sum=prev+current
    print(sum)
    prev=current
    current=sum
