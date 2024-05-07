from dataclasses import dataclass
import logging

print("Hello world")

@dataclass
class MyData:
    name: str
    age: int

data = MyData(
    name="lister",
    age=18
)

logging.warning(data)

