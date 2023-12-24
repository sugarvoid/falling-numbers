
from random import randint


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def _generate_number(len: int=4) -> list[str]:
        _nums: list = []
        for i in range(len):
            _nums.append(str(randint(0, 9)))
        
        return _nums


all_people = [
      Person('mr. one', 13),
      Person('mr. two', 15),
      Person('mr. three', 3),
      Person('mr. four', 10),
      Person('mr. five', 11)
]

def update_lowest_number(list: list) -> Person:
    youngest = min(list, key=lambda x: x.age)
    print(f'youngest guy is {youngest.name}')

update_lowest_number(all_people)