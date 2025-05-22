import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

try:
    togo=pd.read_csv(r"C:\Users\pc\Desktop\Data coll\data\data\togo-dapaong_qc.csv")
    print("Data Imported")
except:
    print("Try again!")    

togo.shape 

togo.count()

togo.info()

togo.isnull().sum()

sns.heatmap(togo.isnull())
plt.show()

togo["Timestamp"]=pd.to_datetime(togo["Timestamp"])





togo= togo.drop(columns="Comments")

Q1=togo.quantile(0.25)
Q3=togo.quantile(0.75)
IQR=Q3-Q1

togo_clean=togo[-((togo<(Q1-1.5*IQR)) | (togo>(Q3+1.5*IQR))).any(axis=1)]

togo_clean.info()

togo_clean.head()

togo_clean.describe()


togo_clean.to_csv("togo_clean", index=False)


togo_clean=pd.read_csv(r"togo_clean")

togo_clean.head()

togo_clean.info()

togo_GHI=togo_clean.groupby("Timestamp")["GHI"].sum()
togo_GHI.head()
togo_GHI.plot(kind="line")
plt.title("GHI vs TimeStamp")
plt.show()

togo_DNI=togo_clean.groupby("Timestamp")["DNI"].sum()
togo_DNI.head()
togo_DNI.plot(kind="line")
plt.title("DNI vs TimeStamp")
plt.show()

togo_DHI=togo_clean.groupby("Timestamp")["DHI"].sum()
togo_DHI.head()
togo_DHI.plot(kind="line")
plt.title("DHI vs TimeStamp")
plt.show()

togo_Tamb=togo_clean.groupby("Timestamp")["Tamb"].sum()
togo_Tamb.head()
togo_Tamb.plot(kind="line")
plt.title("Tamb vs TimeStamp")
plt.show()

togo_ModA_post=togo_clean.groupby("Cleaning")["ModA"].mean()
togo_ModA_post.plot(kind="bar")
plt.title("ModA vs Cleaning")
plt.show()

togo_ModA_pre=togo.groupby("Cleaning")["ModA"].mean()
togo_ModA_pre.plot(kind="bar")
plt.title("ModA vs Cleaning")
plt.show()

togo_ModB_post=togo_clean.groupby("Cleaning")["ModB"].mean()
togo_ModB_post.plot(kind="bar")
plt.title("ModA vs Cleaning")
plt.show()

togo_ModB_pre=togo.groupby("Cleaning")["ModB"].mean()
togo_ModB_pre.plot(kind="bar")
plt.title("ModA vs Cleaning")
plt.show()

togo_clean=pd.read_csv(r"togo_clean")
togo_clean=togo_clean.apply(pd.to_numeric, errors='coerce')

corr=togo_clean.corr()

plt.figure(figsize=(10,8))
sns.heatmap(corr, annot=True)
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(togo_clean["GHI"], kde=True, color="blue", bins=20)
plt.title("Histogram GHI")
plt.xlabel("GHI")
plt.ylabel("WS")
plt.show()

plt.figure(figsize=(10, 6)) 
sns.scatterplot(x="TModA", y="RH", data=togo_clean, alpha=0.7) 
plt.title("Temp vs RH")
plt.xlabel("Global Horizontal Irradiance (GHI)")
plt.ylabel("Relative Humidity (RH)")
plt.grid(True, linestyle='--', alpha=0.6) 
plt.show()


plt.figure(figsize=(10, 6)) 
sns.scatterplot(x="GHI", y="RH", data=togo_clean, alpha=0.7) 
plt.title("Relationship between Global Horizontal Irradiance (GHI) and Relative Humidity (RH)")
plt.xlabel("Global Horizontal Irradiance (GHI)")
plt.ylabel("Relative Humidity (RH)")
plt.grid(True, linestyle='--', alpha=0.6) 
plt.show()

plt.figure(figsize=(10, 6)) 
sns.scatterplot(x="Tamb", y="RH", data=togo_clean, alpha=0.7) 
plt.title("GHI vs Tamb")
plt.xlabel("Global Horizontal Irradiance (GHI)")
plt.ylabel("Relative Humidity (RH)")
plt.grid(True, linestyle='--', alpha=0.6) 
plt.show()