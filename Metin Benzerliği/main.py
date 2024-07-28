import sqlite3


database=sqlite3.connect("odev.db")
imlec=database.cursor() 

imlec.execute("CREATE TABLE IF NOT EXISTS database(Text TEXT)") 
database.commit()

imlec.execute("INSERT INTO database VALUES('Integer volutpat eu diam non mollis. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur at facilisis lorem, in pulvinar diam. Nullam placerat metus quis ornare ornare. Sed bibendum faucibus lacinia. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Aenean tortor orci, porttitor nec ultricies id, imperdiet ac diam. Nunc ac eros metus. Ut maximus est in erat volutpat maximus. Nullam metus dui, convallis vel dictum sed, efficitur at est. Aliquam congue tortor at lorem maximus tristique. Vestibulum consectetur orci quis ipsum porttitor porttitor. Pellentesque ornare congue euismod. Nulla nisi nisl, vestibulum et vestibulum sit amet, sodales ornare nibh. Nunc a cursus sapien.')" )
database.commit()

imlec.execute("INSERT INTO database VALUES('Aenean ut dolor eu lacus porttitor eleifend. Praesent vulputate eleifend turpis, quis vehicula eros molestie at. Nulla quis aliquet ipsum. Vestibulum vehicula augue vel nisl tristique, ac venenatis ante mattis. Proin faucibus condimentum lectus a posuere. Sed volutpat risus magna, non scelerisque turpis fermentum eu. Fusce pellentesque felis viverra, blandit orci et, porttitor nunc. Proin rutrum maximus est. Phasellus ex eros, euismod quis nibh ac, malesuada mollis orci. Donec sagittis mauris et neque consequat cursus. Nullam a tortor non nunc venenatis sollicitudin et ac augue. Etiam eu tellus sed massa dignissim vehicula.')")
database.commit()


imlec.execute("SELECT * FROM database")
veriler = imlec.fetchmany(2)


text=[]
for i in range(2):
    text.append(veriler[i])
    

metin_tuple = text[0]
metin1 = metin_tuple[0]
metin_tuple = text[1]
metin2 = metin_tuple[0]

def jaccard(metin1,metin2):
    kelimeler_metin1 = metin1.split()
    kelimeler_metin2 = metin2.split()

    ortak_olan_kelimeler=[]

    for kelimeler1 in kelimeler_metin1:
        for kelimeler2 in kelimeler_metin2:
            if kelimeler1 == kelimeler2:
                ortak_olan_kelimeler.append(kelimeler1)
                break

    benzerlik = len(ortak_olan_kelimeler) / (len(kelimeler_metin1) + len(kelimeler_metin2) - len(ortak_olan_kelimeler))
    
    return benzerlik

benzerlik1 = jaccard(metin1, metin2)
print("Jaccard benzerliği:", benzerlik1)

def metin_benzerliği_hesapla(metin,metin2):
    kelime_sayisi_metin1 = len(metin1.split())
    kelime_sayisi_metin2 = len(metin2.split())
    harf_sayisi_metin1 = len(metin1.replace(" ",""))
    harf_sayisi_metin2 = len(metin2.replace(" ",""))

    kelime_orani = min(kelime_sayisi_metin1,kelime_sayisi_metin2)/ max(kelime_sayisi_metin1,kelime_sayisi_metin2)
    harf_orani = min(harf_sayisi_metin1,harf_sayisi_metin2)/ max(harf_sayisi_metin1,harf_sayisi_metin2)

    benzerlik=(kelime_orani+harf_orani)/2

    return benzerlik

benzerlik2 = metin_benzerliği_hesapla(metin1, metin2)
print("Benzerlik:", benzerlik2)


dosya = open('benzerlik durumu.txt','w') 
dosya.write("Jaccard benzerligi:"+ str(benzerlik1) + "\n")  
dosya.write("Benzerlik:"+ str(benzerlik2))  


database.close()
