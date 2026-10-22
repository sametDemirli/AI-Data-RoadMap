import pandas as pd
import numpy as np
df=pd.DataFrame({
    "Ogrenci":["Ali","Ayşe","Mehmet","Zeynep"],
    "Not":[80,None,70,90],
    "Bolum":["Bilgisayar","Bilgisayar",None,"Yazılım"]
})

print("Tablo:")
print(df)

print("\nEksik değerler:")
print(df.isna())

print("\nEksik değerlerin sütun bazında sayısı:","\n",df.isna().sum())
print("Eksik değerlerin toplama sayısı: ",df.isna().sum().sum())

enCokTekrarEdenBolum=df["Bolum"].mode()[0]
df["Not"]=df["Not"].fillna(df["Not"].mean())
df["Bolum"]=df["Bolum"].fillna(enCokTekrarEdenBolum)

print("\nEksik değerler girildikten sonra tablo:")
print(df)


df["Durum"]=np.where(df["Not"]>=60,"Geçti","Kaldı")
print("\nDurum satırı eklendikten sonra tablo:","\n",df)

print(df[["Ogrenci","Durum","Not"]])

bilgisayarBolumu=df[df["Bolum"]=="Bilgisayar"]
print(bilgisayarBolumu)
print(bilgisayarBolumu["Not"].mean())