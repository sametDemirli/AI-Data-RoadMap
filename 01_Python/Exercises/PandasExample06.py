import pandas as pd

df=pd.read_csv("PandasExample02.csv",sep=";")

#print(df)

bolumOrtalamalari=df.groupby("Bolum")["Not"].mean()

print("Bölüm ortalamaları:")
print(bolumOrtalamalari)


print("\nBolumlere göre not ortalaması 75 ve üzeri olan bölümler:")
print(bolumOrtalamalari[bolumOrtalamalari>=75])

uygunBolumler=bolumOrtalamalari[bolumOrtalamalari>=75].index

dfYeni=df[df["Bolum"].isin(uygunBolumler)]
print("\nBolum ortalaması 75 üzeri olan bölümlerde okuyan öğrencilerin tablosu:")
print(dfYeni)