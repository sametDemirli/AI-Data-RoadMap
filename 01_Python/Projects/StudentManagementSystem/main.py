Ogrenciler={}

def OgrenciEkle():
    
    if isim=="":
        return True
    
    if isim in Ogrenciler:
        print("bu öğrenci zaten kayıtlı.")
        
    else:
        yas=int(input("eklediğiniz öğrenicin yaşını girin: "))
        Ogrenciler[isim]={
            "yas":yas,
            
        }

    return False


def DersEkle():
    if eklenecekDers=="":
        return True
    else:
        Ogrenciler[isim][eklenecekDers]={}
        return False

def NotEkle(a,b,c):
    


    Ogrenciler[isim][eklenecekDers]={
            "vize":a,
            "final":b,
            "devamsizlik":c
        }

def NotHesapla(vize,final,devamsizlik):
    ortalama=vize*0.4+final*0.6
    if devamsizlik>3:
        return "ZZ"
    elif ortalama<50:
        return "FF"
    elif ortalama>=50 and ortalama<60:
        return "CC"
    elif ortalama>=60 and ortalama<70:
        return "CB"
    elif ortalama>=70 and ortalama<80:
        return "BB"
    elif ortalama>=80 and ortalama<90:
        return "BA"
    else:
        return "AA" 



def Yazdir():
    for ogrenciAdi,ogrenciBilgileri in Ogrenciler.items():
        print(ogrenciAdi,":")
        print("Öğrenicinin yaşı: ",ogrenciBilgileri["yas"])
        for dersAdi,dersBilgileri in ogrenciBilgileri.items():
            if dersAdi=="yas":
                 continue
            print(dersAdi,":")
            print(dersBilgileri)
        harfNotu=NotHesapla(dersBilgileri["vize"],dersBilgileri["final"],dersBilgileri["devamsizlik"])
        if harfNotu=="ZZ":
             print("Bu dersten devamsızlıktan dolayı ZZ ile kaldınız.")
        elif harfNotu=="FF":
             print("Bu dersten FF ile kaldınız.")
        else:
             print("Bu dersten ",harfNotu," ile geçtiniz")
            
               
               
         
while True:
    isim=input("eklemek istediğiniz öğrencinin adını girin(eğer öğrenci kaydı bittiyse bir şey girmeden enter basın.): ")
    
    kontrol1=OgrenciEkle()
    
    while True:
        if kontrol1:
            break
        eklenecekDers=input("Eklemek istediğiniz dersi girin(eğer ekleme işleminiz bittiyse enter basın): ")

        kontrol2=DersEkle()
        if kontrol2:
            break
        
        vizeNotu=int(input("Eklediğiniz dersin vize notunu girin: "))
        while vizeNotu<0 or vizeNotu>100:
            vizeNotu=int(input("HATALI BİR NOT GİRDİNİZ....!!!! Lütfen tekrar girin: "))
        finalNotu=int(input("Eklediğiniz dersin final notunu girin: "))
        while finalNotu<0 or finalNotu>100:
                    finalNotu=int(input("HATALI BİR NOT GİRDİNİZ....!!!! Lütfen tekrar girin: "))
        devamsizlikDurumu=int(input("Eklediğiniz derste öğrencinin kaç devamsızlığı var: "))
        while devamsizlikDurumu<0 :
                    devamsizlikDurumu=int(input("HATALI BİR SAYI GİRDİNİZ....!!!! Lütfen tekrar girin: "))
        NotEkle(vizeNotu,finalNotu,devamsizlikDurumu)
    
    
    if kontrol1:
         break

Yazdir()