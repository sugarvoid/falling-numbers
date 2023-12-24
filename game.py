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
    
    def add_new_number(self, start_x: int) -> None:
        print('making a new number')
        _new_num = NumberObject(starting_x=start_x)
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
        lowest_y = min(numbers, key=lambda x: x.y)
        return lowest_y

    def _draw(self):
        if self.state == GameStates.MAIN_MENU:
            self._draw_main_menu()
        if self.state == GameStates.PLAYING:
            self._draw_gameplay()

    def _update(self, dt):
        self.test_timer.update(dt)
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
        self.lowest_number = self.update_lowest_number(self.number_holder)
        match symbol:
            case key.NUM_1:
                print('Numpad 1 was pressed')
            case key.NUM_2:
                print('Numpad 2 was pressed')
            case key.NUM_3:
                print('Numpad 3 was pressed')
            case key.NUM_4:
                print('Numpad 4 was pressed')
            case key.NUM_5:
                print('Numpad 5 was pressed')
                self.lowest_number.labels[2].color = (100, 255, 100, 255)
            case key.NUM_6:
                print('Numpad 6 was pressed')
            case key.NUM_7:
                print('Numpad 7 was pressed')
            case key.NUM_8:
                print('Numpad 8 was pressed')
            case key.NUM_9:
                print('Numpad 9 was pressed')
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
                print('Numpad 0 was pressed')
