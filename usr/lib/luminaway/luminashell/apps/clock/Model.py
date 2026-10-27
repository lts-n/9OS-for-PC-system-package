import time

class Model:
    def __init__(self):
        pass
    def get_current_time(self):
        return time.strftime("%H:%M:%S")
    def get_current_date(self):
        return time.strftime("%Y-%m-%d")
    def set_timer(self, hours, minutes, seconds):
        total_seconds = hours * 3600 + minutes * 60 + seconds
        while total_seconds > 0:
            time.sleep(1)
            total_seconds -= 1
        return 0