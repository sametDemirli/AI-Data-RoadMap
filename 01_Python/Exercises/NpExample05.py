import numpy as np

notlar = np.array([
    [60, 70, 80],
    [90, 85, 95],
    [40, 50, 60]
])

eklenenNot=np.array([5])

yeniNotlar=np.array(notlar+eklenenNot)

print(yeniNotlar.mean(axis=1))