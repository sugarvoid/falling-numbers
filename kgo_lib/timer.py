# timer.py 0.1.0

from typing import Callable


class Timer:
    """
    How to use:
 
    Creation:
        new_timer: Timer = Timer(5)

    Starting:
        new_timer.start()
        
 
    Updating:
        new_timer.update(delta_time)
    """
    def __init__(self, finished_time: int=1, callback: Callable=None, repeat:bool=False) -> None:
        self.elapsed_time: float = 0
        self.is_paused: bool = True
        #self.START_TIME = finished_time
        self.is_repeat = repeat
        self.finished_time = finished_time
        self.is_finished: bool = False
        self.is_running: bool = False
        self.on_done_func = callback
        if self.on_done_func is None:
            self.on_done_func = self.print_done
    
    def update(self, dt: float) -> None:
        if not self.is_finished and not self.is_paused:
            self.elapsed_time += dt
            if self.elapsed_time > self.finished_time:
                self.is_finished = True
                self.is_running = False
                self.on_done_func()
                if self.is_repeat:
                    print(f'{self} is starting again')
                    self.start()
    
    def start(self):
        self.elapsed_time = 0
        self.is_finished = False
        self.is_running = True
        self.is_paused = False

    def pause(self):
        self.is_paused = not self.is_paused
    
    def print_done(self) -> None:
        print('I\'m done')