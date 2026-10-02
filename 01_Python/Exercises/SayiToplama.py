toplam=0
kontrol=True

while kontrol:
    sayi=int(input("Sayı girin: "))
    if sayi==0:
        kontrol=False
    else:
        toplam+=sayi

print(toplam)