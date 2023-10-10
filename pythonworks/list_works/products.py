items=[
    {"id":1,"name":"sugar","price":40,"avl_qty":10},
    {"id":2,"name":"milk","price":28,"avl_qty":40},
    {"id":3,"name":"teapowder","price":230,"avl_qty":100},
    {"id":4,"name":"tomatto","price":120,"avl_qty":5},
    {"id":5,"name":"potatto","price":45,"avl_qty":70},
    {"id":6,"name":"carrot","price":80,"avl_qty":0},
    {"id":7,"name":"oreo","price":45,"avl_qty":0},
    {"id":8,"name":"hideandseek","price":50,"avl_qty":50},
    
]
# total_items=len(items)
# print(total_items)

# for i in items:
#     if i.get("avl_qty")>0:
#         print(i.get("name"))
#     elif i.get("avl_qty")<50:
#         print(i.get("name"))
    
# # for i in items:
# #     if i.get("price") in range(20,51):
# #         print(i.get("name"))

# # listcomprehesion method
# all_products_name=[i.get("name") for i in items]
# print(all_products_name)




# in_stock_product=[i.get("name") for i in items if i.get("avl_qty")>0]
# print(in_stock_product)

# total_num=[len(items) for i in items ]
# print(total_num)


under_50=[i.get("name") for i in items if i.get("price")<50]
print("under 50",under_50)

range_filter=[i.get("name") for i in items if i.get("price") in range(20,51)]
print(range_filter)

# costly product
costly_product=max(items,key=lambda i: i.get("price"))
print(costly_product)


sort_product=sorted(items,reverse=True,key=lambda i:i.get("avl_qty"))
print(sort_product)









# print total number of product
# print all product Name
# print all instock Name
# print products name available under rs 50
# print all product names available in range of 20 to 50