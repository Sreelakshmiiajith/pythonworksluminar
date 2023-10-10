tummy_size=int(input("enter tummy size"))
buttock_size=int(input("enter buttock size"))
gender=input("enter gender male or female")

messurement=tummy_size/buttock_size
val=round(messurement,2)
print(val)
if gender=="female":

    if messurement<0.80:
        print("your health risk is low and body shape is pear")
    elif(messurement<=0.85):
        print("your health risk is moderate and body shape is avacado")
    elif(messurement>0.85):
        print("your health risk is high and body shape is apple")

elif(gender=="male"):
    if messurement<0.95:
         print("your health risk is low and body shape is pear")
    elif(messurement<=1.0):
         print("your health risk is moderate and body shape is avacado")
    elif(messurement>1.0):
         print("your health risk is high and body shape is apple")

else:
    print("please enter valid gender")

    