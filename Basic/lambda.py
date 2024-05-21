from dataclasses import dataclass

@dataclass
class User:
    user_id: int
    user_name: str
    email: str
    mobile: str
    enable: bool

user_list = []
user_list.append(User(user_id=1,user_name="Lister",email="L547837@163.com",mobile="186xxx",enable=True))
user_list.append(User(user_id=2,user_name="Lister2",email="L547837@1631.com",mobile="186xxx1",enable=True))
user_list.append(User(user_id=3,user_name="Lister3",email="L547837@1633.com",mobile="186xxx3",enable=False))

user_id_list = list(map(lambda x: x.user_id, user_list)) # 或者 [t.user_id for t in user_list]
print(user_id_list)

user_dict = {user.user_id: user.user_name for user in user_list}

print(user_dict)

from itertools import groupby

# 先对 user_list 按 enable 排序，因为 groupby 需要预先排序的数据
sorted_user_list = sorted(user_list, key=lambda user: user.enable)

# 使用 groupby 按 enable 分组
user_dict = {key: list(group) for key, group in groupby(sorted_user_list, key=lambda user: user.enable)}

print(user_dict)