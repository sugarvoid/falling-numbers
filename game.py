
from kgo_lib.extra_math import clamp
from kgo_lib.timer import Timer

from number_object import NumberObject
from functools import partial

from pyglet.text import Label
from pyglet.window import Window, key
from pyglet.graphics import Batch
from pyglet import clock


class GameStates:
    MAIN_MENU = 0
    PLAYING = 1
    PAUSED = 2
    GAME_OVER = 3
    TOP_SCORES = 4

class Game(Window):
    def __init__(self):
        super().__init__(width= 500, height=700, caption = "Falling Numbers")

        self.number_holder: list = []

        #self.current_number: NumberObject = NumberObject(starting_x=100)
        self.lowest_number = None #: NumberObject = None
        self.state: int
        self.main_menu_label_1 = Label(text="Falling Numbers", x=10, y=460, font_size=36)

        self.all_numbers_batch = Batch()

        #self.current_number.add_to_screen(batch=self.all_numbers_batch)
        self.test_timer: Timer = Timer(3, repeat=True, callback=partial(self.add_new_number, 100))
        self.current_pos: int = 0
    
    def add_new_number(self, start_x: int) -> None:
        print('making a new number')
        _new_num = NumberObject(starting_x=start_x, parent_holder=self.number_holder)
        _new_num.add_to_screen(batch=self.all_numbers_batch)
        self.number_holder.append(_new_num)
        self.test_timer.start()

    def setup(self):
        self.state = GameStates.MAIN_MENU
        self.state = 1
        clock.schedule_interval(self.on_update, 1/60.0)
        self.test_timer.start()
        print('ready')
    

    def update_lowest_number(self, numbers: list) -> NumberObject:
        lowest_y: NumberObject = min(numbers, key=lambda x: x.y)
        print(f'lowest number is {lowest_y.labels}')
        return lowest_y

    def _draw(self):
        if self.state == GameStates.MAIN_MENU:
            self._draw_main_menu()
        if self.state == GameStates.PLAYING:
            self._draw_gameplay()

    def _update(self, dt):
        self.test_timer.update(dt)
        if len(self.number_holder) > 0:
            self.lowest_number = self.update_lowest_number(self.number_holder)
        for n in self.number_holder:
            n.update(dt)
        return
    
    def on_key_press(self, symbol, modifiers):
        self.parse_key(symbol)

    def _draw_main_menu(self):
        self.main_menu_label_1.draw()
    
    def _draw_gameplay(self):
        self.all_numbers_batch.draw()
    
    def on_draw(self):
        self.clear()
        self._draw()

    def on_update(self, dt):
        self._update(dt)
    
    def parse_key(self, symbol: int) -> str:
        
        _key:str
        match symbol:
            case key.NUM_1:
                _key = '1'
            case key.NUM_2:
                _key = '2'
            case key.NUM_3:
                _key = '3'
            case key.NUM_4:
                _key = '4'
            case key.NUM_5:
                _key = '5'
            case key.NUM_6:
                _key = '6'
            case key.NUM_7:
                _key = '7'
            case key.NUM_8:
                _key = '8'
            case key.NUM_9:
                _key = '9'
            case key.NUM_ADD:
                print('Numpad + was pressed')
            case key.NUM_SUBTRACT:
                print('Numpad - was pressed')
            case key.NUM_MULTIPLY:
                print('Numpad * was pressed')
            case key.NUM_DIVIDE:
                print('Numpad / was pressed')
            case key.NUM_ENTER:
                print('Numpad Enter was pressed')
            case key.NUM_DECIMAL:
                print('Numpad . was pressed')
            case key.NUM_0:
                _key = '0'
        self.lowest_number.check_key_pressed(_key,self.current_pos)
        self.current_pos += 1
        self.current_pos = clamp(self.current_pos, 0, len(self.lowest_number.labels))
        if self.current_pos == 4:
            self.lowest_number.completed = True
            self.lowest_number = self.update_lowest_number(self.number_holder)
            self.current_pos = 0
