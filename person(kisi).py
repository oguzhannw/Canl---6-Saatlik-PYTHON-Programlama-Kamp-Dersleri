class Person:
    def __init__(self,name,lastName,yas):
        self.name = name
        self.lastName = lastName
        self.yas = yas

musteri1 = Person("Ahmet","Demiroğ","1")    #AHMET NAME   DEMİROĞ LASTNAME YANİ 2.SATIRA GİDER. 20 de yas'a gider.
musteri2 = Person("Kerem","Varış","10")
musteri3 = Person("İlker","Tural","30")

print(musteri1.yas)