# **PYTHON'DA CLASS OLUŞTURACAKSAN SELF KULLANMAK ZORUNDASIN **SELF=KENDİM yani matematiks sınıfının kendisi.

class Matematik:
    def __init__(self, sayi1, sayi2): #constructor(yapıcı) blok.
        self.s1 = sayi1               #matematiğin içinde bi değişken ata=s1 olsun. s1'i de sayi1'e eşitle.
        self.s2 = sayi2
        print("Matematik başladı (referansı oluştu)")
    def topla(self):   #DEF=FONKSİYON HALİNE GETİRİYOR.
        return self.s1 + self.s2
    def cikar(self):
        return self.s1 - self.s2
    def bol(self):   #DEF=FONKSİYON HALİNE GETİRİYOR.
        return self.s1 / self.s2
    def carp(self):
        return self.s1 * self.s2

matematik = Matematik(6,7)  #6 sayi1 e ,7 de sayi2 ye gider yani 4. satıra.
sonuc = matematik.cikar()
print("Sonuç : "+ str(sonuc))

class Istatistik(Matematik):            #yeni sınıf açtık bu sınıfta MATEMATİĞİN init'lerini kullandık.
    def __init__(self, sayi1, sayi2):   #yukarıda Matematik classını belirttik.
        super().__init__(sayi1,sayi2)
    def varyansHesapla(self):
        return self.s1 * self.s2

#inheritance(miras-kalıtım)

istatistik = Istatistik(5,8)