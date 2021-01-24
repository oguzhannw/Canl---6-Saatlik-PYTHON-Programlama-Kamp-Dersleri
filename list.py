#DERS VİDEOSU = https://www.youtube.com/watch?v=6IWpowC2ryc  dakika 2:45
urunler=["Laptop","Mouse","Keyboard"]      #listeyi köşeli parantezle ifade ederiz.

print(urunler)
# print(type(urunler))           #ürünlerin türünü yazdırır. yani list.
urunler.append("Telefon")      #listeye Telefon ekledik.
print(urunler)

ogrenciler1 = ["İlker","Cavit","Berkay"]
ogrenciler2 = ["Kerem","Ali","Mehmet"]

ogrenciler1 = ogrenciler2          #ogrenci1= ["Kerem","Ali","Mehmet"] yaptık.
ogrenciler2[0]="Engin"             #ogrenci2 listesindeki 1. elemanı Engin olarak değiştirdik.
print(ogrenciler1)
print(ogrenciler2)

sayi1=10
sayi2=20
sayi1=sayi2                        #sayi1=10 yaptık. [yani sayi2'nin değeri.]
sayi2 = 60
print(sayi1)
print(sayi2)


#referans tip -> list,string
#değer tip -> int,float,bool

isim = "Engin"  
print(isim)

bosListe=[]