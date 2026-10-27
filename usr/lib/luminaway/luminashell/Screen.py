from screeninfo import get_monitors

class Screen:
    def __init__(self, monitor=0):
        self.monitor = get_monitors()[monitor] 
        
    def width(self):
        return self.monitor.width

    def height(self):
        return self.monitor.height