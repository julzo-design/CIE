import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#file_path = "class_0_perfect_structure_csv"
file_path = "class_1_imperfect_structure_csv"
file_name = "Displacement_Long_Structure_2MN_Force.csv"

df = pd.read_csv(f"{file_path}/{file_name}")

plt.figure()
plt.plot(df.iloc[:,0], df[' _U:U1 PI: PART-1-1 N: 83'], label='U_1, N83')
plt.plot(df.iloc[:,0], df['_U:U2 PI: PART-1- 1 N: 83'], label='U_2, N83')
plt.plot(df.iloc[:,0], df['_U:U3 PI: PART-1- 1 N: 83'], label='U_3, N83')
plt.legend()
plt.title(f"{file_path}/{file_name}")
plt.ylabel("Component Deformation [m]")
plt.xlabel("Time [s]")

plt.figure()
plt.plot(df.iloc[:,0], df['_U:U1 PI: PART-1-1 N: 156'], label='U_1, N156')
plt.plot(df.iloc[:,0], df['_U:U1 PI: PART-1-1 N: 156'], label='U_2, N156')
plt.plot(df.iloc[:,0], df['_U:U1 PI: PART-1-1 N: 156'], label='U_3, N156')
plt.legend()
plt.title(f"{file_path}/{file_name}")
plt.ylabel("Component Deformation [m]")
plt.xlabel("Time [s]")

plt.figure()
plt.plot(df.iloc[:,0], df['_U:Magnitude PI:PART-1-1 N: 83'], label='U_ges, N83')
plt.plot(df.iloc[:,0], df[' _U:Magnitude PI:PART-1-1 N: 156'], label='U_ges, N156')
plt.legend()
plt.title(f"{file_path}/{file_name}")
plt.ylabel("Total Deformation [m]")
plt.xlabel("Time [s]")

