# text="good morning goodmorning"

# words=text.split()
# longest_word=max(words,key=lambda w:len(w))
# print(longest_word)






# text="good morning goodmorning"

# words=text.split()
# shortest_word=min(words,key=lambda w:len(w))  #w=each word in text
# print(shortest_word)


text="good morning a a goodmorning"

words=text.split()
srt_word=sorted(words,key=lambda w:len(w),reverse=True)
print(srt_word)





