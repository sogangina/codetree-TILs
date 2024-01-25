class user():
    def __init__(self, id='hello', lv='28'):
        self.id = id
        self.lv = int(lv)

id, lv = input().split()
user1 = user()
user2 = user(id, lv)

print(f'user {user1.id} lv {user1.lv}')
print(f'user {user2.id} lv {user2.lv}')