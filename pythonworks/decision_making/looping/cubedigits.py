num=153
sum=0
original=num

while(num !=0):
    last_digit=num %10
    num=num//10
    cube=(last_digit**3)

    sum+=cube #sum=sum+last_digit

    
print(sum)

if(original==sum):
    print("the number is amstrong")
else:
    print("number is not amstorng")


#153 is 3 digit amstrong number