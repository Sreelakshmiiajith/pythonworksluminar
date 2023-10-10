# expenses=[12000,13000,14000,15000,16000]

# # expenses of feb month
# print(expenses[1])

# for e in expenses:
#     print(e)

#exp>15000
# for e in expenses:
#     if e>15000:
#         print(e)

# sum of expenses
# sum=0
# for e in expenses:
#     sum=e+sum
# print(sum)

# higest expense
# max_exp=0
# for e in expenses:
#     if e >max_exp:
#         max_exp=e
# print(max_exp)

# cheap_exp=expenses[0]
# max_expense=0
# for e in expenses:
#     if e<cheap_exp:
#        cheap_exp=e
     
# print(cheap_exp)


expenses=[12000,13000,14000,15000,16000]
total_exp=sum(expenses)
print(total_exp)

min_expense=min(expenses)
print(min_expense)

max_expense=max(expenses)
print(max_expense)
