class Config:
    def __init__(self, icon_size=64):
        self.icon_size = icon_size
    def save(self):
        with open("config.py", "w", encoding="utf-8") as f:
            f.write(f'''
icon_size = "{self.icon_size}"
''')