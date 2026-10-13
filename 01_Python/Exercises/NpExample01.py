import numpy as np

notlar=np.array([45,70,85,30,90,60,50,100,75,40])

altmisUstu=notlar[notlar>=60].copy()
gectiKaldi=np.where(notlar>=60,'Geçti','Kaldı')
seksenUstu=notlar[notlar>=80].copy()  

print("Not ortalaması: ",notlar.mean())
print("En yüksek not: ",notlar.max())
print("En düşük not: ",notlar.min())
print("Geçenlerin notları: ",altmisUstu)
print("Geçen öğrenci sayısı: ",np.sum(notlar>=60))
print("Öğrenci durumları: ",gectiKaldi)
print("Seksen ve üzeri notlar: ",seksenUstu)