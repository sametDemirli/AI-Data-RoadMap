vizeNotu=int(input("vize notunuzu girin: "))
finalNotu=int(input("final notunuzu girin: "))
devamsizlik=int(input("kaç devamsızlığınız var: "))

if devamsizlik>3:
    devamsizlikKalma=True
else :
    devamsizlikKalma=False

ortalama=vizeNotu*0.4+finalNotu*0.6

if ortalama<50:
    ortalamadanKalma=True
else:
    ortalamadanKalma=False

if not ortalamadanKalma:
    if not devamsizlikKalma:
        if finalNotu>=50:
            print("GEÇTİNİZ:)")
        if ortalama>=90:
                print("Harf Notunuz AA")
        elif ortalama>=80 and ortalama<90:
                print("Harf notunuz BA")
        elif ortalama>=70 and ortalama<80:
                print("Harf notunuz BB")
        elif ortalama>=60 and ortalama<70:
                print("Harf notunuz CB")
        else:
                print("Harf notunuz CC")
else:
    print("KALDINIZ:(")
    print("Harf notunuz FF")