yas=int(input("yaşınızı girin"))
OgrenciMi=bool(int(input("Öğrenci iseniz 1 değilseniz 0 girin: ")))

if yas>=18 and OgrenciMi:
    print("Siz ",yas," yaşında yetişkin bir öğrencisiniz." )
elif yas<18 and OgrenciMi:
    print("Siz ",yas," yaşında henüz yetişkin olmayan bir öğrencisiniz.")
elif yas>18 and OgrenciMi:
    print("Siz",yas," yaşında yetişkin ama öğrenci değilsiniz.")
else :
    print("Siz ne yetişkin ne de öğrencisiniz")