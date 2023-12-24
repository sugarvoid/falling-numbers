
from random import randint


def _generate_number(len: int=4) -> list[str]:
        _nums: list = []
        for i in range(len):
            _nums.append(str(randint(0, 9)))
        
        return _nums



print(_generate_number())
print(_generate_number())
print(_generate_number())
print(_generate_number())
print(_generate_number())
print(_generate_number())
print(_generate_number())
print(_generate_number())
print(_generate_number())