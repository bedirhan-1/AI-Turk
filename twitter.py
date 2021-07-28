import urllib
import json

class Twitter():
    def __init__(self) -> None:
        pass

    def getData(self):
        with urllib.request.urlopen("Twitter-api-link") as url:
            data = json.loads(url.read().decode())
            data2 = data['data']
            return data2

    