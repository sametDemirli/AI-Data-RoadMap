import numpy as np

notlar = np.array([
    [70, 80, 90],
    [50, 60, 70],
    [90, 85, 95],
    [40, 55, 65]
])

altmisUstu = notlar[notlar.mean(axis=1) >= 60].copy()

print("Öğrenci ortalamaları:", notlar.mean(axis=1))
print("Sınav ortalamaları:", notlar.mean(axis=0))
print("En yüksek sınav ortalaması:", notlar.mean(axis=0).max())
print("Ortalaması 60 ve üzeri olan öğrenciler:", altmisUstu)