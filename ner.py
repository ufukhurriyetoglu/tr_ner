from sklearn.feature_extraction.text import CountVectorizer


# veri setlerini ayrı dosyalardan okuyup liste formatında döndürür.
def load_gazetteers():
    # isim dosyasını okur. satırlara böler
    # satırda ekstra boşluk varsa temizler
    with open('name_list.txt', mode = 'rt', encoding = 'utf-8') as f:
        names = [name.strip() for name in f.readlines()]

    with open('city_list.txt', mode = 'rt', encoding = 'utf-8') as fp:
        places = [place.strip() for place in fp.readlines()]
    return names, places


def recognize(text):
    output = []
    # listeleri yükleyelim 
    names, places = load_gazetteers()
    # verilen metni tokenlara bölelim
    tokens = CountVectorizer().build_tokenizer()(text)

    for token in tokens: # tokenları dön
        if token in names:
            output.append((token,'ISIM')) # isim listesinde bulunmuş output'a ekle
        if token in places:
            output.append((token,'YER')) # yer ismi bulunmuş output'a ekle
    return output

