fread=open("C:\\Users\\91759\\Desktop\\pythonworks\\fileinputoutput\\years.txt","r")
fwrite=open("C:\\Users\\91759\\Desktop\\pythonworks\\fileinputoutput\\leapyr.txt","w")
for line in fread:
    year=int(line.strip("\n"))
    if(year%100==0 and year%400):
        fwrite.write(str(year)+"\n")
    elif(year %100!=0 and year %4==0):
        fwrite.write(str(year)+"\n")