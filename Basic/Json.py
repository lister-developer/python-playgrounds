import json
from dataclasses import dataclass, asdict

def json2Dict():
    # JSON字符串
    json_str = '{"name": "John", "age": 30, "city": "New York"}'

    # 解析JSON字符串为Python对象
    data = json.loads(json_str)

    # 输出Python对象
    print(data)  # {'name': 'John', 'age': 30, 'city': 'New York'}

    # 访问对象的属性
    print(data['name'])  # John
    print(data['age'])   # 30
    print(data['city'])  # New York

    json_arr_str = '[{"name": "John", "age": 30, "city": "New York"}]'

    data = json.loads(json_arr_str)
    print(data)
    print(f"data[0]['name'] {data[0]['name']}")

    for d in data:
        print(d['name'])  # John
        print(d['age'])   # 30
        print(d['city'])  # New York
    
def dict2json():
    # Python字典对象
    data = {'name': 'John', 'age': 30, 'city': 'New York'}

    # 将Python对象转换为JSON字符串
    json_str = json.dumps(data)

    # 输出JSON字符串
    print(f"json_str is {json_str}")

  
def jsonConvert():
    
    @dataclass
    class Person:
        name: str
        age: int
        city: str

    p = Person(name="Lister", age=18, city="Shanghai")
    # 简单的 p 对象可以直接调用他的 __dict__ 信息，将其转换为json
    pjson = json.dumps(p.__dict__)
    print(f"simple p object to json: {pjson}")
    
    
    @dataclass
    class Pets:
        name: str
        type: str
        
    @dataclass
    class Person1:
        name: str
        age: int
        city: str
        pets: list[Pets]

    p = Person1(name="Lister", age=18, city="Shanghai", pets=[Pets(name="Bigdog", type="cat")])
    # 使用dataclasses.asdict()函数将Person对象转换为一个包含其属性的字典，
    # 然后使用json.dumps()函数将该字典转换为JSON字符串。由于Pets对象是Person对象的一部分，
    # 因此你需要适当处理它们以确保它们也能被正确地转换为JSON。
    p_dict = asdict(p)
    pjson = json.dumps(p_dict, indent=4)
    print(f"pjson whit pets is {pjson}")

    p1 = json.loads(pjson)
    print(p1)

    # {'name': 'Lister', 'age': 18, 'city': 'Shanghai', 'pets': [{'name': 'Bigdog', 'type': 'cat'}]} to Person1
    json_str = "{'name': 'Lister', 'age': 18, 'city': 'Shanghai', 'pets': [{'name': 'Bigdog', 'type': 'cat'}]}"
    data = json.loads(json_str)
    pp = Person1(**data)
    print(f"pp is {pp}")


# 如何判断json是对象还是数组
# ChatGPT
# 在处理JSON数据时，你可以使用Python中的json模块来解析JSON字符串并判断其类型。
# JSON字符串可以表示对象（键值对）或数组（有序列表）。你可以根据解析后的数据类型来判断JSON是对象还是数组。以下是一个示例：

# 示例JSON字符串
json_str_object = '{"name": "John", "age": 30, "city": "New York"}'
json_str_array = '[1, 2, 3, 4, 5]'

# 解析JSON字符串
data_object = json.loads(json_str_object)
data_array = json.loads(json_str_array)

# 判断类型
if isinstance(data_object, dict):
    print("JSON是一个对象")
elif isinstance(data_object, list):
    print("JSON是一个数组")
else:
    print("JSON既不是对象也不是数组")

if isinstance(data_array, dict):
    print("JSON是一个对象")
elif isinstance(data_array, list):
    print("JSON是一个数组")
else:
    print("JSON既不是对象也不是数组")
    
    
    
  # 定义Person类
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age}, city={self.city})'

# JSON字符串
json_str = '{"name": "John", "age": 30, "city": "New York"}'

# 将JSON字符串转换为Python字典
data = json.loads(json_str)

# 使用字典的值初始化Person对象
person = Person(**data)

# 输出Person对象
print(person)  # Person(name=John, age=30, city=New York)