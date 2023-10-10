stopwords=open("C:\\Users\\91759\\Desktop\\pythonworks\\takenization\\stopwords.txt")
news=open("C:\\Users\\91759\\Desktop\\pythonworks\\takenization\\news.txt")
stop_words={line.rstrip("\n") for line in stopwords}
news_set=set()
for line in news:
    words=line.split()
    for w in words:
        news_set.add(w)
print(news_set.difference(stop_words))
