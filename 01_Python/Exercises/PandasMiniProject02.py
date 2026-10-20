import pandas as pd
import numpy as np

df=pd.read_csv("PandasExample02.csv",sep=";")

df["Gecti"]=df["Not"]>=60

rapor=df.groupby("Bolum").agg(
    OgrenciSayisi=("Not","count"),
    Ortalama=("Not","mean"),
    EnYuksek=("Not","max"),
    GecenSayisi=("Gecti","sum"),
)

rapor["KalanSayisi"]=rapor["OgrenciSayisi"]-rapor["GecenSayisi"]
rapor["BasariOrani%"]=np.where(rapor["KalanSayisi"]==0,100,rapor["GecenSayisi"]/rapor["OgrenciSayisi"]*100)

rapor.reset_index().to_csv("BolumRaporu.csv", sep=";", index=False)

print(pd.read_csv("BolumRaporu.csv",sep=";"))