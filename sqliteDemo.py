import sqlite3   #sqLite için yapılmış kütüphane. SABİTTİR.

def listele():   #Listele fonksiyonunu oluşturduk.
    baglanti = sqlite3.connect("chinook.db")    #sqlite'taki chinook veritabanına bağlandık.
    cursor = baglanti.execute("select FirstName,LastName from customers")  #ilgili bağlantıyı çalıştır.
                                #     sutun[1] ,sutun[2]
    for sutun in cursor:
        print(sutun[0], sutun[1])
#             FisrtName,LastName
    baglanti.close()

listele()