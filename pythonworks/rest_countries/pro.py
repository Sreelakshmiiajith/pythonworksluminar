from json import load
path="C:\\Users\\91759\\Desktop\\pythonworks\\rest_countries\\countries.json"
with open(path,encoding="utf-8")as f:
    countries=load(f)
startswith_c=[c.get("name") for c in countries if c.get("name").startswith("C")]
# print(startswith_c)
name_capital=[[c.get("name"),c.get("capital")]  for c in countries]
# print(name_capital)

# countries with maximum borders5
c_with_borders=[c for c in countries if "borders" in c]
max_border_country=max(c_with_borders,key=lambda c:len(c.get("borders")))
# print(max_border_country.get("name"))

india_borders=[c.get("borders") for c in countries if c.get("name")=="India"][0] #nested list ozhivakkan ahn [0] kodithe
india_border_name=[c.get("name") for c in countries  if c.get("alpha3Code")in india_borders]
# print(india_border_name)

# regions={c.get("region") for c in countries }
# print(regions)
re={}
for c in countries:
    region=c.get("region")
    if region in re:
        re[region]+=1
    else:
        re[region]=1
print(re)
population_filter=[c.get("name") for c in countries if c.get("population")<400000]
# print(population_filter)


#asia redion etra country
# america etra country 