import pandas as pd
import numpy as np

df=pd.read_csv("PandasExample02.csv",sep=";")#eğer ilk satır başlık değilde veri içeriyorsa header=None kullanmalısın. 

print("Tablo:")
print(df)

df["Durum"]=np.where(df["Not"]>=60,"Geçti","Kaldi")
#print(df)

#print(df.columns)#ilk satrırı yani sütunların başlıklarını verir
#print(df.shape)#boyutlarında ayrı ayrı kaç eleman var (satir,sutun) şeklinde gösterir
#print(df.head(3))#ilk 3 elemanı  göster

#print("İlk 5 öğrenci:")
#print(df.head(5))

#print("\nTablo boyutu:")
#print(df.shape)

#print("\nTablo bilgileri:")
#df.info()

#print("\nNot istatistikleri:")
#print(df["Not"].describe())

#print("\n80 ve üzeri not alanlar:")
#print(df[df["Not"]>=80])

#print("\nEn yüksek not alan öğrenci:")
#print(df.sort_values("Not",ascending=False).head(1))

#print("\nBölümlere göre not ortalaması: ")
#print(df.groupby("Bolum")["Not"].mean())

#print("\n60 altı notlar:")
#print(df[df["Not"]<60])

#print("\nEn düşük Not:")
#print(df.sort_values("Not").head(1))

df.to_csv("OgrenciSonuc.csv",sep=";",index=False)

dfYeni=pd.read_csv("OgrenciSonuc.csv",sep=";")
print("\nYeni Tablo:")
print(dfYeni)