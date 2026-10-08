class WebAppModel:
    def __init__(self, url):
        self.url = url
        self.title = ""
        self.loading = False

    @property
    def window_title(self):
        return self.title or self.url
