num=int(input("enter a number:"))
original=num
digit_count=len(str("num"))
sum=0

while(num!=0):
    last_digit=num%10
    exponent=last_digit**digit_count
    sum=sum+exponent
    num=num//10
print("number is amstrong" if original==sum else "number is not amstrong")