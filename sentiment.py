import optparse
from reddit import Reddit
# from twitter import Twitter
# from facebook import facebook


prsObj = optparse.OptionParser()
prsObj.add_option("-c", "--coin", dest="coin", help="enter cryptocurrency")
prsObj.add_option("-w", "--website", dest="website", help="enter a website name")

(inputs, args) = prsObj.parse_args()

# -w ve -c ile girilen kelimeler
chs_website = inputs.website # girilen website ismi
chs_coin = inputs.coin # girilen coin ismi


    #reddit
if (chs_website == 'reddit'):
    website = Reddit(chs_coin) # Reddit class'ına obje oluşturma
    website.forReddit()

    
    # twitter
elif chs_website == 'twitter':
    # twitter'da bir obje oluştur ve fonksiyonları çalıştır
    pass
    
    # facebook
elif chs_website == 'facebook':
    # facebook'ta bir obje oluştur ve fonksiyonları çalıştır
    pass
    
else:
    print("ERROR: Girilebilecek website isimleri:\n-twitter\n-facebook\n-reddit")

