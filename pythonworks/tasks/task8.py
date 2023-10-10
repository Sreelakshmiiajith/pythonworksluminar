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