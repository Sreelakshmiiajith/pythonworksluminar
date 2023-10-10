text="i have 2 car and 3 cycles"
words=text.split(" ")
for w in words:
    if w.isdigit():
        print(w)