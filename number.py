
from pyglet.text import Label
from pyglet.graphics import Batch

class Number:
    def __init__(self):
        self.value:str = ''
        self.current_element: int
        
        self.full_label: list
        self.starting_x: int = 50
        self.starting_y: int = 50
        self.batch = Batch()
        self.labels: list = []
    
    def go_to_next_char(self) -> None:
        self.current_element += 1
    
    def add_to_screen(self) -> None:
        test = ['1', '2', '3', '4']
        test = "1234"

        for x in range(len(test)):
            butt = Label(
                text=test[x],
                font_size=36,
                x=self.starting_x + x * 32,  # Adjust the x-coordinate for spacing
                y=self.starting_y,
                anchor_x='center',
                anchor_y='center',
                batch=self.batch
            ) 
            self.labels.append(butt)
        


    def draw(self) -> None:
        self.batch.draw()

    def update_label(self) -> None:
        pass