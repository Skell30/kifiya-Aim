import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

try:
    benin=pd.read_csv(r"C:\Users\pc\Desktop\Data coll\data\data\benin-malanville.csv")
    print("Data Imported")
except:
    print("Try again!")    

benin.shape 

benin.count()

benin.info()

benin.isnull().sum()

sns.heatmap(benin.isnull())
plt.show()

benin["Timestamp"]=pd.to_datetime(benin["Timestamp"])





benin= benin.drop(columns="Comments")

Q1=benin.quantile(0.25)
Q3=benin.quantile(0.75)
IQR=Q3-Q1

benin_clean=benin[-((benin<(Q1-1.5*IQR)) | (benin>(Q3+1.5*IQR))).any(axis=1)]

benin_clean.info()

benin_clean.head()

benin_clean.describe()


benin_clean.to_csv("benin_clean", index=False)


benin_clean=pd.read_csv(r"benin_clean")

benin_clean.head()

benin_clean.info()

benin_GHI=benin_clean.groupby("Timestamp")["GHI"].sum()
benin_GHI.head()
benin_GHI.plot(kind="line")
plt.title("GHI vs TimeStamp")
plt.show()

benin_DNI=benin_clean.groupby("Timestamp")["DNI"].sum()
benin_DNI.head()
benin_DNI.plot(kind="line")
plt.title("DNI vs TimeStamp")
plt.show()

benin_DHI=benin_clean.groupby("Timestamp")["DHI"].sum()
benin_DHI.head()
benin_DHI.plot(kind="line")
plt.title("DHI vs TimeStamp")
plt.show()

benin_Tamb=benin_clean.groupby("Timestamp")["Tamb"].sum()
benin_Tamb.head()
benin_Tamb.plot(kind="line")
plt.title("Tamb vs TimeStamp")
plt.show()

benin_ModA_post=benin_clean.groupby("Cleaning")["ModA"].mean()
benin_ModA_post.plot(kind="bar")
plt.title("ModA vs Cleaning")
plt.show()

benin_ModA_pre=benin.groupby("Cleaning")["ModA"].mean()
benin_ModA_pre.plot(kind="bar")
plt.title("ModA vs Cleaning")
plt.show()

benin_ModB_post=benin_clean.groupby("Cleaning")["ModB"].mean()
benin_ModB_post.plot(kind="bar")
plt.title("ModA vs Cleaning")
plt.show()

benin_ModB_pre=benin.groupby("Cleaning")["ModB"].mean()
benin_ModB_pre.plot(kind="bar")
plt.title("ModA vs Cleaning")
plt.show()

benin_clean=pd.read_csv(r"benin_clean")
benin_clean=benin_clean.apply(pd.to_numeric, errors='coerce')

corr=benin_clean.corr()

plt.figure(figsize=(10,8))
sns.heatmap(corr, annot=True)
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(benin_clean["GHI"], kde=True, color="red", bins=20)
plt.title("Histogram GHI")
plt.xlabel("GHI")
plt.ylabel("WS")
plt.show()

plt.figure(figsize=(10, 6)) 
sns.scatterplot(x="TModA", y="RH", data=benin_clean, alpha=1, color="red") 
plt.title("Temp vs RH")
plt.xlabel("Global Horizontal Irradiance (GHI)")
plt.ylabel("Relative Humidity (RH)")
plt.grid(True, linestyle='--', alpha=1) 
plt.show()


plt.figure(figsize=(10, 6)) 
sns.scatterplot(x="GHI", y="RH", data=benin_clean, alpha=0.7, color="red") 
plt.title("Relationship between Global Horizontal Irradiance (GHI) and Relative Humidity (RH)")
plt.xlabel("Global Horizontal Irradiance (GHI)")
plt.ylabel("Relative Humidity (RH)")
plt.grid(True, linestyle='--', alpha=0.6) 
plt.show()

plt.figure(figsize=(10, 6)) 
sns.scatterplot(x="Tamb", y="RH", data=benin_clean, alpha=0.7, color="red") 
plt.title("GHI vs Tamb")
plt.xlabel("Global Horizontal Irradiance (GHI)")
plt.ylabel("Relative Humidity (RH)")
plt.grid(True, linestyle='--', alpha=0.6) 
plt.show()