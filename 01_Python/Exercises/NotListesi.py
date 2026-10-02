notListesi=[]

for i in range(5):
    notListesi.append(int(input("sayı girin: ")))

for notum in notListesi:
    if notum>=50:
        print(notum)
    


#print("girilen notlar: ",notListesi)
#print("en yükseği: ",max(notListesi))
#print("en düşüğü: ",min(notListesi))
#print("ortalaması: ",sum(notListesi)/len(notListesi))