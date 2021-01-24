sayi1=100
sayi2=20
sayi3=55

if sayi1>sayi2 and sayi1>sayi3:                   #eğer 1 2 ve 3 den büyükse.
    buyukSayi=sayi1                               
elif sayi2>sayi1 and sayi2>sayi3:                 #2 1 ve 3 den büyükse.
    buyukSayi=sayi2
else:                                              #if ve elifin çalışmadığı durumlarda.
    buyukSayi=sayi3 

print("En büyük sayı : " + str(buyukSayi))
