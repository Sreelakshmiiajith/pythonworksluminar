all_users=["mohan lal","fahad","unni","mammooty","nivin"]
nivin_friends=["mohan lal","unni","fahad"]
fahad_friends=["mohan lal","mammooty"]

suggession_lst=[]
for u in all_users:
    if u not in nivin_friends:
        suggession_lst.append(u)
print(suggession_lst)