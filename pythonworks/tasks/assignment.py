#Q1
num=int(input("enter a number between 10 and 20:"))
if(num<=20):
    print("thank you")
else:
    print("incorrect answer")

#Q2
num=int(input("enter a number:"))
wc={}
if num<10:
    print("too low")
elif(num<=20):
    print("correct")
else:
    print("too high")

#Q3
age=int(input("enter your age:"))
if age>=18:
    print("you can vote")
elif age==17:
    print("you can learn to drive")
elif age==16:
    print("you can buy a lottery tickte")
else:
    print("you can go for treat")

#Q4
num=int(input("select a number 1,2 or 3:"))
if num==1:
    print("thank you")
elif num==2:
    print("well done")
elif num==3:
    print("correct")
else:
    print("incorrect")

#Q5
num=int(input("enter a number"))
if num%2==0 or num%3==0:
    print("true")
else:
    print("false")

#Q6
text=input("enter a character:")
vowels=("a","e","i","o","u")
for w in text:
    if w in vowels:
        print("entered character is vowel")
    else:
        print(" entered character not vowels")

#Q8
number=int(input("enter a number:"))
for i in range(0,number):

    if  (number%2==0):
        print("number is even")
        break
    elif(number%2!=0):
        print("number is not even")
        break
    elif i!=number:
        print("number is not in range")

#Q9
name=input("enter your name:")
start=1
while(start<=3): 
    print(name)
    start+=1
     
#Q10
name=(input("enter your name:"))
number=int(input("enter a number:"))
start=0
while(start<number):
    if(number<10):
         print(name)
    elif number!=10:
        print("too high")
        break
    start+=1

#Q12
while True:
    num=int(input("enter a number"))
    if num>5:
        print(f"you entered number was",num)

#Q14
start=10
end=300
for n in range(10,301,10):
    print(n)
    
#Q15
start=1
end=5
total=0
while(start<=end):
    total=total+start
    start+=1
    average=total/end
print(average)
