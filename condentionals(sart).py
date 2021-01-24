istenilenKredi = 100000
hesap=9502
minimumOlmasiGerekenHesap = 10000

if hesap>=minimumOlmasiGerekenHesap:     #eğer hesap 10000 den büyükse.
    print("Kredi verilebilir.")

elif hesap>=9000 and hesap<=9500:
    print("Müdüre sorulacak.")           #9000 ve 9500 arasında Müdüre sorulacak.

elif hesap>=9501 and hesap<=9999:        #9500 ve 9999 arasında Danışmana sorulacak.
    print("Danışmana sorulacak.")

else:                                    #if ve elifin geçerli olmadığı yerde bu kod çalışır.
    print("Kredi almak için bakiyeniz yetersiz.")

print("İşlem sonu")
