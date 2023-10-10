from json import load
path=("C:\\Users\\91759\\Desktop\\pythonworks\\readfromjason\\name.json")
with open(path) as f:
    records=load(f)
# print(records)
# name=[f.get("name")for f in records]
# print(name)
# course=[f.get("name")for f in records if f.get("course")=="java"]
# print(course)
year=[f.get("name")for f in records if f.get("year")==2023]
print(year)