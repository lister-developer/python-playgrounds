def func(data):
    """
    单个参数
    """
    print(data)

func("Hello")

def func(data1, data2):
    """
    两参数的方法
    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_
    """
    print(f"data1: {data1}, data2: {data2}")

func("hello", "world")

def func(name, *nums):
    """可变数量的函数,nums 类似于Java的 Integer... nums

    Args:
        name (str): _description_
    """
    print(f"name: {name}, nums: {nums}")

func("Lister", 1,2,3)

def func(name, **keywords):
    """动态参数的函数,keywords 是一个字典

    Args:
        name (str): _description_
    """
    print(f"name: {name}, keywords: {keywords}, first: {keywords['first']}")

func("Lister", first="a", second="b", last="c")

def func(*nums, **keywords):
    print(nums)
    print(keywords)
    
func(1,2,3,4, a="1",b="2")

def func(name="Lister", *, age):
    """此方法的age前面加了 *, 所以调用时 age 必须指定名称调用

    Args:
        age (_type_): _description_
        name (str, optional): _description_. Defaults to "Lister".
    """
    print(f"name={name}, age={age}")    

func(age=6)

def func(name="Lister", *, age):
    """此方法的age前面加了 *, 所以调用时 age 必须指定名称调用

    Args:
        age (_type_): _description_
        name (str, optional): _description_. Defaults to "Lister".
    """
    print(f"name={name}, age={age}")    

func(age=6)

def func(a,b,c,d,*,e,f,g):
    pass
func(1,2,3,4,e=5,f=6,g=7)


def func(*, name, age) -> str:
    """指定返回值的方法, 但返回值无法限制此方法返回什么类型

    Args:
        name (_type_): _description_
        age (_type_): _description_

    Returns:
        str: _description_
    """
    print(f"name={name}, age={age}")    
    return name + str(age)

print(func(name="l", age=18))