
from random import randint

from kgo_lib.timer2 import Timer2


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age




timer: Timer2 = Timer2(finished_time=3, repeat=True)
timer.start()