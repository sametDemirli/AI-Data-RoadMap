import pandas as pd

df=pd.read_csv("PandasExample02.csv",sep=";")

print("Bilgisayar bölümünde okuyan VE notu 80 ve üstü olan öğrenciler:")
print(df[(df["Bolum"]=="Bilgisayar")&(df["Not"]>=80)])

print("\nNotu 90 ve üstü olan VEYA yazılım bölümünde olan öğrenciler:")
print(df[(df["Not"]>=90)|(df["Bolum"]=="Yazilim")])

print("\nBilgisayar bölümünde okumayanların tablosu:")
print(df[df["Bolum"]!="Bilgisayar"])