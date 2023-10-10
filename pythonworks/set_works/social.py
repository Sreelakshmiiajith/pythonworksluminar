all_users=["sachin","dhoni","kohli","rohit","sanju","padikkal"]
sanju_followings=["padikkal","sachin"]
suggestion=list(set(all_users).difference(set(sanju_followings)))

# all_user=set(all_users)
# sanju=set(sanju_followings)

# suggestion=all_user.difference(sanju)
suggestion.pop(suggestion.index("sanju"))
print(suggestion)