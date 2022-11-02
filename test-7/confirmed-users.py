unconfirmed_users = ['jiang', 'qin', 'long']
confirmed_users = []  # 空列表

while unconfirmed_users:
    # confirmed_users = unconfirmed_users.pop()
    current_users = unconfirmed_users.pop()

    print("Verify user:" + current_users.title())
    confirmed_users.append(current_users)

for confirmed_user in confirmed_users:
    print(confirmed_user.title())