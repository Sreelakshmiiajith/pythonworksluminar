lst=[2,3,4,6,7,8]


# normal method

# squares=[]
# for n in lst:
#     sq=n**2
#     squares.append(sq)
# print(squares)


# method using comprehesion

# cubes=[n**3 for n in lst]
# print(cubes)



# add_two=[n+2 for n in lst]
# print(add_two)

# #print greater than 5
# gt=[n for n in lst if n>5]
# print(gt)


even_number=[n for n in lst if n%2==0]
print(even_number)


odd=[n for n in lst if n%21!=0]
print(odd)

#years 1800-2025

years=[y for y in range(1800,2026)]
print(years)

# century years
century_years=[y for y in years if y%100==0]
print(century_years)

#non century years
non_centuryyears=[y for y in years if y%100!=0]
print(non_centuryyears)