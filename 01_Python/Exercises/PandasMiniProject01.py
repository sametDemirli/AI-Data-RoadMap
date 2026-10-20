import pandas as pd
import numpy as np

df=pd.read_csv("PandasExample02.csv",sep=";")

df.loc[2,"Not"]=np.nan
df.loc[4,"Bolum"]=np.nan#test amacıyla eksik değer oluşturalım

print("Orijinal tablo:")
print(df)

print("\nEksik değerler tablosu:")
print(df.isna())

print("\nSütun bazıda eksik değerler:")
print(df.isna().sum())

print("\nEksik değerlerin toplam sayısı:")
print(df.isna().sum().sum())

df["Not"]=df["Not"].fillna(df["Not"].mean())

enCokTekrarEdenBolum=df["Bolum"].mode()[0]
df["Bolum"]=df["Bolum"].fillna(enCokTekrarEdenBolum)

print("\nEksik değerler doldurulduktan sonra(eksik not not ortalması ile, eksik bölüm en çok tekrar eden bölümle doldurulmuştur.) tablo:")
print(df)

df["Durum"]=np.where(df["Not"]>=60,"Gecti","Kaldi")
print("\nDurum sütunu eklendikten sonra tablo:")
print(df)

df.to_csv("OgrenciTemiz.csv",sep=";",index=False)