import requests

class Downloader:

    def __init__(self, URL, params=None, method="GET"):
        self.url = URL
        self.params = params
        self.method = method.upper()

    def get_html(self):
        responce = requests.request(method=self.method, url=self.url, params=self.params)
        return responce.text

    def save(self, path):
        html = self.get_html()
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
