# all_users=["mohan lal","fahad","unni","mammooty","nivin"]
nivin_friends=["mohan lal","unni","fahad"]
fahad_friends=["mohan lal","mammooty"]
mutual_lst=[]
for i in nivin_friends:
    if i in fahad_friends:
        mutual_lst.append(i)
print(mutual_lst)