import numpy as np

notlar = np.array([
    [60, 70, 80],
    [90, 85, 95],
    [40, 50, 60],
    [75, 65, 85]
])


eklenenNot=np.array([5,10,15])

yeniNotlar=notlar+eklenenNot

ortalamalar=yeniNotlar.mean(axis=1)

print(ortalamalar)

basarili=ortalamalar[ortalamalar>=70]

print(basarili)

print(yeniNotlar.mean())