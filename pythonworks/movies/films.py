from json import load
path="C:\\Users\\91759\\Desktop\\pythonworks\\movies\\mdb.json"
with open(path, encoding="utf-8") as m:
    movies=load(m)
# print(len(movies))
# # for i in records:
# #     for g in i.get("title"):

# # movie_name=[m.get("title") for m in movies ]
# # print(movie_name)
# # released_year=[m.get("title") for m in movies if m.get("year")=="2005"]
# # print(released_year)

# # comedy_movie=[m.get("title") for m in movies if "Comedy" in m.get("genres")]
# # print(comedy_movie)

# lengthy_movie=max(movies,key=lambda m:int(m.get("runtime")))
# print(lengthy_movie)



 #print all geners
# geners={g for m in movies for g in m.get("genres")}
# print(geners)


# released_year=[m.get("title") for m in "Comedy" in m.get("genres") and m.get("year")=="2005"]
# print(released_year)




wc={}
for m in movies:
    year=m.get("year")
    if year in wc:
        wc[year]+=1
    else:
        wc[year]=1
print(max(wc))