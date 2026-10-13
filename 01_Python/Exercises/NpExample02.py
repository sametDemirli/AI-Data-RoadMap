import numpy as np

veri = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])

matris=veri.reshape(3,4)

print(matris)
print(matris.shape)
print(matris[0,:])#burada : gerek yok 
print(matris[:,1])