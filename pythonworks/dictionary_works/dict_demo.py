employee={"name":"manu","age":34,"gender":"male","id":1010,"salary":25000}

#new add akkan
employee["dep"]="soft"
print(employee["name"])
print(employee["age"])
print(employee["gender"])
print(employee["id"])
# print(employee["salary"])

if("salary" in employee):
    print("present")
else:
    print("not present")

#update
employee["salary"]=20000
# print(employee["salary"])

#to add
employee["salary"]+=500
print(employee)