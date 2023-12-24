
from pyglet.text import Label
from pyglet.graphics import Batch
from pyglet import font

from random import randint

font.add_file("PeaberryMono.ttf")
print('loading font')
font.load("Peaberry")


class NumberObject:
    def __init__(self, starting_x: float=50):
        self.value:str = ''
        self.current_element: int
        self.fall_speed = 30
        self.full_label: list
        self.starting_x: int = starting_x
        self.starting_y: int = 600
        self.batch = Batch()
        self.labels: list = []
        self.x = 0
        self.y = 0
    
    def go_to_next_char(self) -> None:
        self.current_element += 1
    
    def add_to_screen(self, batch: Batch) -> None:
        test = NumberObject._generate_number(4)

        for x in range(len(test)):
            _lbl = Label(
                text=test[x],
                font_name="Peaberry",
                font_size=36,
                x=self.starting_x + x * 32,  # Adjust the x-coordinate for spacing
                y=self.starting_y,
                anchor_x='center',
                anchor_y='center',
                batch=batch
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
            
    
    @staticmethod
    def _generate_number(len: int=4) -> list[str]:
        _nums: list = []
        for i in range(len):
            _nums.append(str(randint(0, 9)))
        
        return _nums
