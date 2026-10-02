notlar={
    "Veri Yapilari":75,
    "Matematik":85,
    "Programlama":90,
    "Istatistik":30,
    "fizik":45
}

ortalama=sum(notlar.values())/len(notlar)


for anahtar,deger in notlar.items():
    if deger<50:
        gectimMi="Kaldı."
    else:
        gectimMi="Geçti."

    if deger<ortalama:
        ortUstuMu="ortalama altı."
    else:
        ortUstuMu="ortalama üstü."
    

    print(anahtar,":",deger,",",gectimMi,",",ortUstuMu)