import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
headers=["Zulassungsraten-Frauen","Zulassungsraten-Männer",
"Anteil-Bewerbungen-Frauen","Anteil-Bewerbungen-Männer"]

#read CSV
st = pd.read_excel("C:\ZHAW\Semester2-2022\Statistik\Tabelle.xlsx",names=headers)

#rename 1. column
st.index=["A","B","C","D","E","F","Total"]


#Test Dataframe
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
print(st)

#1 Variable statisics
print(st.describe())



#Declare columns
ZF=list(st["Zulassungsraten-Frauen"])
ZM=list(st["Zulassungsraten-Männer"])
AF=list(st["Anteil-Bewerbungen-Frauen"])
AM=list(st["Anteil-Bewerbungen-Männer"])

plt.show()
st[["Zulassungsraten-Frauen","Zulassungsraten-Männer"]].plot()
st[["Anteil-Bewerbungen-Frauen","Anteil-Bewerbungen-Männer"]].plot()
st[["Zulassungsraten-Frauen","Zulassungsraten-Männer"]].plot.bar()
st[["Anteil-Bewerbungen-Frauen","Anteil-Bewerbungen-Männer"]].plot.bar()


def Kreuztabelle (x):
    data={
    "X (Männer)":[AF[x]*AM[x],(1-AF[x])*AM[x],AM[x]],
    "X̅":[(1-AM[x])*AF[x],(1-AF[x])*(1-AM[x]),1-AM[x]],
    "Tot":[AF[x],1-AF[x],1]
    }
    df=pd.DataFrame(data)
    df.index=["Y (Frauen)","Ȳ","Tot"]
    print(df)
    
for x in range(6):
    Kreuztabelle(x)
    
