from kgolib.timer import Timer
from number_object import NumberObject


class NumberManager:
    def __init__(self):
        self.number_holder: list
        self.spawn_time: int = 5
        self.spawn_timer: Timer = Timer(
            finished_time=self.spawn_time, callback=self.drop_number, repeat=True
        )
        self.last_y: int

    def move_back_to_top(self, num_obj: NumberObject):
        pass

    def drop_number():
        pass
