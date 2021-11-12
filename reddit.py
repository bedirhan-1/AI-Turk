import urllib.request, json
from numpy import positive
import pandas as pd
from textblob import TextBlob
from colorama import Fore, Back, Style


class Reddit():
    def __init__(self, coin):
        self.coin = coin

    def getData(self):
        with urllib.request.urlopen("https://api.pushshift.io/reddit/search/submission/?q=" + self.coin) as url:
            data = json.loads(url.read().decode())
            data2 = data['data']
        return data2


    def analysis(self, text, data, positivity):

        for index, i in enumerate(data):
            text = i['selftext']
            blob1 = TextBlob(text)
            
            if blob1.sentiment.polarity != 0 and blob1.sentiment.subjectivity != 0:
                positivity.append(blob1.sentiment.polarity)
                

    def addFile(self, myList):
        myList.to_csv(self.coin + "-data.csv", index = False, mode = "a", header = False)


    def rate(self, positivity):
        toplam = 0
        for i in positivity:
            toplam += i
        
        ortalama = toplam / len(positivity)
        return ortalama          

    def forReddit(self):
        positivity = []  # cümlelerdeki pozitiflik katsayısının tutulduğu array
        data = self.getData()  # yorum datasının tutulduğu değişken
        text = []  # yorumların her biri ayrı bir dizi elemanı
        self.analysis(text, data, positivity)  # datayı çekip, karışık datayı cümleler haline getirip, pozitiflik değerlendirmesi yapar
        a = self.rate(positivity)
        positivity = pd.DataFrame(positivity)
        self.addFile(positivity)  # o an alınan pozitiflik değerlerini bir "csv" dosyasına ekler.
        print()
        print(Fore.RED + "positivity rate of last", len(positivity), "comment :  %", a*100)
        print(Style.RESET_ALL)
