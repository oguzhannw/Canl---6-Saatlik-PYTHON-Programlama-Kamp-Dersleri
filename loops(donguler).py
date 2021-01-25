# sehirler = ["Ankara","İstanbul","İzmir"]

# for sehir in sehirler: #sehirlerin içini tek tek dolaştı.
#     print(sehir)       #dolaştığı her str yi yazdırdı.

# for sayi in range(10): #10 a kadar yazar.
#     print(sayi)

# for sayi in range(0 , 10, 2):   # 0 dan başlayıp 10 a kadar 2 şer yazar.
#     print(sayi)

sayac = 1
while sayac<=10:       #WHİLE ŞART GERÇEKLEŞTİĞİ SÜRECE DÖNGÜ DEVAM EDER. 1 DEN BAŞLA 10 OLANA KADAR 
    print(sayac)
    sayac = sayac + 1  #SAYAC+1 DÖNGÜ DEVAM ETSİN.


isim = input("Adınız")    # Kodu çalıştırdıktan sonra **terminalden adımızı  giriyoruz**.
print("isim : "+ isim)    #ENTER basınca bize adımızı veriyor.

sayi = int(input("Kaçın faktoriyelini hesaplayalım : "))  #Çalışınca **terminalden sayı girmemizi istiyor**

#5 FAKTORİYEL = 5*4*3*2*1
faktöriyel = 1
if sayi>0:
    for i in range(1,sayi+1) :   # i=başlangıç işlemi ** ranger(devam şartları)
        faktöriyel = faktöriyel * i
    print("Sonuç : ",faktöriyel)
elif sayi==0:
    print("Sonuç 1")
else:
    print("Negatif sayıların faktöriyeli hesaplanmaz.")

    # 1                           TERMİNALE 5 GİRERSEK SAYI=5   5+1 KERE FOR DÖNGÜSÜ DÖNECEK.
    # 1*2
    # 2*3
    # 6*4
    # 24*5
    # 120