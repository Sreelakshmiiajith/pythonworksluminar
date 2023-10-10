foods=[
    {"id":1,"name":"ghee-roast","price":70,"category":"veg"},
    {"id":2,"name":"chicken-roast","price":170,"category":"non-veg"},
    {"id":3,"name":"cb","price":170,"category":"non-veg"},
    {"id":4,"name":"bb","price":190,"category":"non-veg"},
    {"id":5,"name":"fried-rice","price":140,"category":"veg"},
    {"id":6,"name":"chicken-friedrice","price":170,"category":"non-veg"},
    {"id":7,"name":"nan","price":70,"category":"veg"},
    {"id":8,"name":"alfham","price":370,"category":"non-veg"},
     
]

# total_items=len(foods)
# print(total_items)

# veg=[i.get("name") for i in foods if i.get("category")=="veg"]
# print("veg_items:",veg)

# avlunder_100=[i.get("name") for i in foods if i.get("price")<100]
# print(avlunder_100)

# costly_item=max(foods,key=lambda i: i.get("price"))
# print("costly_item",costly_item)

# nonveg_foods=[f for f in foods if f.get("category")=="non-veg"]
costly_nonveg=max(foods,key=lambda f:f.get("category")=="non-veg" and f.get("price"))
print("costly non veg:",costly_nonveg)

categories={f.get("category") for f in foods }  #add } this for avoid duplicates
print(categories)


        






# total number of items
# # print name whose category = veg
# food names available under rs 100
# costly item
# costly non-veg food