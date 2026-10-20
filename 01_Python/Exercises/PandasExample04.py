import pandas as pd
import numpy as np

df=pd.read_csv("PandasExample02.csv",sep=";")

sonuc=df.groupby("Bolum")["Not"].agg(
    ["mean","max","min","count"]
)

print(sonuc)