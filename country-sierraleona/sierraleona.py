import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

try:
    leon=pd.read_csv(r"C:\Users\pc\Desktop\Data coll\data\data\sierraleone-bumbuna.csv")
    print("Data Imported")
except:
    print("Try again!")    

leon.shape 

leon.count()

leon.info()

leon.isnull().sum()

sns.heatmap(leon.isnull())
plt.show()

leon["Timestamp"]=pd.to_datetime(leon["Timestamp"])







Q1=leon.quantile(0.25)
Q3=leon.quantile(0.75)
IQR=Q3-Q1

leon_clean=leon[-((leon<(Q1-1.5*IQR)) | (leon>(Q3+1.5*IQR))).any(axis=1)]

leon_clean.info()

leon_clean.head()

leon_clean.describe()


leon_clean.to_csv("leon_clean", index=False)


leon_clean=pd.read_csv(r"leon_clean")

leon_clean.head()

leon_clean.info()

leon_GHI=leon_clean.groupby("Timestamp")["GHI"].sum()
leon_GHI.head()
leon_GHI.plot(kind="line", color="green")
plt.title("GHI vs TimeStamp")
plt.show()

leon_DNI=leon_clean.groupby("Timestamp")["DNI"].sum()
leon_DNI.head()
leon_DNI.plot(kind="line", color= "green")
plt.title("DNI vs TimeStamp")
plt.show()

leon_DHI=leon_clean.groupby("Timestamp")["DHI"].sum()
leon_DHI.head()
leon_DHI.plot(kind="line", color="green")
plt.title("DHI vs TimeStamp")
plt.show()

leon_Tamb=leon_clean.groupby("Timestamp")["Tamb"].sum()
leon_Tamb.head()
leon_Tamb.plot(kind="line", color="green")
plt.title("Tamb vs TimeStamp")
plt.show()

leon_ModA_post=leon_clean.groupby("Cleaning")["ModA"].mean()
leon_ModA_post.plot(kind="bar", color="green")
plt.title("ModA vs Cleaning")
plt.show()

leon_ModA_pre=leon.groupby("Cleaning")["ModA"].mean()
leon_ModA_pre.plot(kind="bar", color="green")
plt.title("ModA vs Cleaning")
plt.show()

leon_ModB_post=leon_clean.groupby("Cleaning")["ModB"].mean()
leon_ModB_post.plot(kind="bar", color="green")
plt.title("ModA vs Cleaning")
plt.show()

leon_ModB_pre=leon.groupby("Cleaning")["ModB"].mean()
leon_ModB_pre.plot(kind="bar", color="green")
plt.title("ModA vs Cleaning")
plt.show()

leon_clean=pd.read_csv(r"leon_clean")
leon_clean=leon_clean.apply(pd.to_numeric, errors='coerce')

corr=leon_clean.corr()

plt.figure(figsize=(10,8))
sns.heatmap(corr, annot=True)
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(leon_clean["GHI"], kde=True, color="green", bins=20)
plt.title("Histogram GHI")
plt.xlabel("GHI")
plt.ylabel("WS")
plt.show()

plt.figure(figsize=(10, 6)) 
sns.scatterplot(x="TModA", y="RH", data=leon_clean, alpha=1, color="green") 
plt.title("Temp vs RH")
plt.xlabel("Global Horizontal Irradiance (GHI)")
plt.ylabel("Relative Humidity (RH)")
plt.grid(True, linestyle='--', alpha=1) 
plt.show()


plt.figure(figsize=(10, 6)) 
sns.scatterplot(x="GHI", y="RH", data=leon_clean, alpha=0.7, color="green") 
plt.title("Relationship between Global Horizontal Irradiance (GHI) and Relative Humidity (RH)")
plt.xlabel("Global Horizontal Irradiance (GHI)")
plt.ylabel("Relative Humidity (RH)")
plt.grid(True, linestyle='--', alpha=0.6) 
plt.show()

plt.figure(figsize=(10, 6)) 
sns.scatterplot(x="Tamb", y="RH", data=leon_clean, alpha=0.7, color="green") 
plt.title("GHI vs Tamb")
plt.xlabel("Global Horizontal Irradiance (GHI)")
plt.ylabel("Relative Humidity (RH)")
plt.grid(True, linestyle='--', alpha=0.6) 
plt.show()