from itertools import repeat

from setting import get_time
class Timer:
    def __init__(self,duration,callback,autostart:bool,repeat:bool):
        self.duration = duration
        self.callback = callback
        self.strt = 0
        self.active = False
        self.repeat = repeat
        if autostart:
            self.activate()

    def activate(self):
        self.active = True
        self.strt = get_time()
    def deactivate(self):
        self.active = False
        self.strt = 0
        if self.repeat:
            self.activate()
    def update(self):
        if self.active:
            if get_time()-self.strt >= self.duration:
                if self.callback:
                    self.callback()
                self.deactivate()