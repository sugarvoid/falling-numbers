from pyglet.text import Label
from pyglet.graphics import Batch
from pyglet import font

from random import randint

from kgolib.color import hex_to_rgba

font.add_file("PeaberryMono.ttf")
font.load("Peaberry")


class NumberObject:
    def __init__(self, starting_x: float = 50, parent_holder: list = None):
        self.value: str = ""
        self.current_element: int
        self.fall_speed = 40
        self.full_label: list
        self.starting_x: int = starting_x
        self.starting_y: int = 600
        self.batch = Batch()
        self.labels: list = []
        self.x = 0
        self.y = 0
        self.done: bool = False
        self.completed: bool = False
        self.parent_holder: list = parent_holder
        self.last_ele_checked: bool

    def go_to_next_char(self) -> None:
        self.current_element += 1

    def reset(self) -> None:
        print("RESET")
        test = NumberObject._generate_number(4)
        for x in range(len(test)):
            self.labels[x].text = test[x]
            self.labels[x].color = hex_to_rgba("#ecf2f1")
        self.y = self.starting_y
        for lbl in self.labels:
            lbl.y = self.y
        self.done = False
        self.completed = False

    def add_to_screen(self, batch: Batch) -> None:
        test = NumberObject._generate_number(4)

        for x in range(len(test)):
            _lbl = Label(
                text=test[x],
                font_name="Peaberry",
                font_size=36,
                x=self.starting_x + x * 32,  # Adjust the x-coordinate for spacing
                y=self.starting_y,
                anchor_x="center",
                anchor_y="center",
                batch=batch,
            )
            self.labels.append(_lbl)

    def draw(self) -> None:
        return
        self.batch.draw()

    def update(self, dt) -> None:
        self._update_label(dt)

    def _update_label(self, dt) -> None:
        for lbl in self.labels:
            lbl.y = lbl.y - (self.fall_speed * dt)
        self.y = self.labels[0].y
        if self.y <= 50:
            self.reset()

    def check_key_pressed(self, key: str, element: int) -> None:
        if key == self.labels[element].text:
            self.labels[element].color = hex_to_rgba("#20e01d")
        else:
            self.labels[element].color = hex_to_rgba("#eb102a")

    def remove_self(self) -> None:
        # for char in self.labels:
        # char.batch = None
        # self.parent_holder.remove(self)
        self.reset()

    @staticmethod
    def _generate_number(len: int = 5) -> list[str]:
        _nums: list = []
        for i in range(len):
            _nums.append(str(randint(0, 9)))

        return _nums
