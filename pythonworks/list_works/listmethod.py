#         -3    -2     -1
colors=["red","green","blue","red"]
#         0      1       2
colors.append("yellow")
 
colors.pop(1) #remove from specific position 
print(colors)



colors.sort()

colors.sort(reverse=True) #decending order
# print(colors)


print(colors.count("red")) #count of object that we defined

colors.clear()  #clear all 
# print(colors)