import pandas as pd

veriler={
    "Ogrenci":["Ali","Ayse","Mehmet"],
    "Bolum":["Bilgisayar","Elektronik","Bilgisayar"],
    "Not":[85,None,68]
}

df=pd.DataFrame(veriler)


#Bölümü bilgisayar olanlar
#print(df[df["Bolum"]=="Bilgisayar"])

#notu 80 üstü olanlar
#print(df[df["Not"]>=80])


#print("Tüm öğrencilerin ortalaması: ", round(df["Not"].mean(),2))

#print("Notu 80 ve üzeri olan öğrencilerin ortalaması: ",round(df[df["Not"]>=80]["Not"].mean(),2))

#print("Küçükten Büyüğe: ")
#print(df.sort_values("Not"))

#print("Büyükten Küçüğe: " )
#print(df.sort_values("Not",ascending=False))

#print("Notu 80 ve üzeri olan fakat bölümü bilgisayar olmayanlar")
#print(df[(df["Not"]>=80)&(df["Bolum"]!="Bilgisayar")])

#print("Notu 80 ve üzeri olan veya bölümü bilgisayar olanlar")
#print(df[(df["Not"]>=80)|(df["Bolum"]=="Bilgisayar")])

print(df.isna().sum())

#eksik veri bulunan satırı komple silme
dfTemiz=df.dropna()
print(dfTemiz)

#eksik veriyi diğer verilerin ortalaması ile doldurma
df["Not"]=df["Not"].fillna(df["Not"].mean())
print(df)

#Yeni kodlar

print(df.head())#ilk 5 eleman
print(df.shape)#satır sütun sayısını döndürür
print(df.info())#veri tablosunu tanımaya yarar.kaç satır sütun var, boş olmayan eleman sayıları, veri türleri ve bellekteki kapladığı alanı gösteri
print(df.describe())#sayısal değerlerin kaç tane olduğu,ortalamaları,standart sapması,minimumu,maksimumu ve bu aralığı dörde bölerek ilk çeyrek ortanca değer(medyan) üçüncü son çeyrek değerleri verir
print(df.groupby("Bolum")["Not"].mean())#gruplandırma yapmanı sağlar groupby("Bolum") bölümleri gruplandırır