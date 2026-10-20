import pandas as pd
import numpy as np

df=pd.read_csv("PandasExample02.csv",sep=";")

df.loc[2,"Not"]=np.nan
df.loc[4,"Bolum"]=np.nan

print("Tablo:")
print(df)

print("\nEksik değerlerin tablosu:")
print(df.isna())

print("\nEksik değerlerib sütün bazında sayısı:")
print(df.isna().sum())

print("\nEksik değerlerin toplam sayısı:")
print(df.isna().sum().sum())

#df["Not"]=df["Not"].fillna(df["Not"].mean())
#print("\nEksik not diğer notların ortalamasıyla doldurulduktan sonra tablo:")
#print(df)

#enCokTekrarEdenBolum=df["Bolum"].mode()[0]
#df["Bolum"]=df["Bolum"].fillna(enCokTekrarEdenBolum)

#print("\nEksik bölüm en sık tekrar eden bölümle değiştirildikten sonra tablo:")
#print(df)

dfYeni=df.dropna()

print("\nEksik veri bulunan satırlar silindikten sonra tablo:")
print(dfYeni)

print("Orijinal tablo:", df.shape)
print("Temizlenmiş tablo:", dfYeni.shape)