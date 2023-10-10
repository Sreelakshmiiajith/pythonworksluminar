from json import load
path="C:\\Users\\91759\\Desktop\\pythonworks\\readfromjason\\data.json"
with open(path)as f:
    records=load(f)


# for f in records:
#     print(f.get("name"))
# print(records)

# fw_names=[f.get("name") for f in records]
# print(fw_names)

top_fw=max(records,key=lambda d:d.get("rating"))
print(top_fw)

#frontend frame work name
#