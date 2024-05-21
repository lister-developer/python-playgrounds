from dataclasses import dataclass
from dataclasses_json import dataclass_json
import json

@dataclass_json
@dataclass
class Pets:
    name: str
    type: str

@dataclass_json
@dataclass
class Person:
    name: str
    age: int
    city: str
    pets: list[Pets]

# JSON字符串
json_str = '{"name": "Lister", "age": 18, "city": "Shanghai", "pets": [{"name": "Bigdog", "type": "cat"}]}'

# 从JSON字符串加载到Person对象
person = Person.from_json(json_str)

# 输出Person对象
print(person)

# 将Person对象转换为字典
person_dict = person.to_dict()

# 输出字典
print(person_dict)
