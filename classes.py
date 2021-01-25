
class Banka:              #fonksiyonları sınıflara aldık. kredibasvur ve kredihesaplayı Banka sınıfına aldık.
    def krediBasvur(self):     #FONKSİYON
        print("Kredi başvurusu yapıldı.")

    def krediHesapla(self):
        print("Hesaplar yapıldı.")

banka=Banka()
banka.krediBasvur()

#self = c#'taki this gibi.   class olduğu zaman fonksiyonların içine self gelir.
