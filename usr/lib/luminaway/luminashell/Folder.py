import os

class Folder:
    def __init__(self, path):
        self.path = path
    def list(self):
        try:
            return os.listdir(self.path)
        except FileNotFoundError:
            return []