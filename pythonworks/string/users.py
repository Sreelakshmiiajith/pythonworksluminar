tweet="what a game, hatts of to teams . well done @enstrokes "
words=tweet.split(" ")
for w in words:
    if w.startswith("@"):
        print(w)