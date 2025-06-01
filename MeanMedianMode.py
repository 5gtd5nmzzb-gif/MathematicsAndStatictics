import pandas as pd
import numpy as np

df = pd.read_csv('/home/rahulkp/Desktop/AI/Mathematics&Statistics/income.csv', names=['Name', 'Income'],skiprows=[0])
print(df)

print("Summary Statistics:")
summary = df.describe()
print(summary)

print("Percentiles:")
percentiles = df['Income'].quantile([0.25, 0.5, 0.75])
print(percentiles)
percentiles_lower = df['Income'].quantile(0.25, interpolation='lower')
print("25th Percentile (Lower):", percentiles_lower)
percentiles_upper = df['Income'].quantile(0.75, interpolation='higher')
print("75th Percentile (Upper):", percentiles_upper)
percentiles = df['Income'].quantile(1)
print("100th Percentile:", percentiles)

percentile_99 = df['Income'].quantile(0.99)
print("99th Percentile:", percentile_99)

print("Incom above the 99th percentile:")
print(df[df['Income']>percentile_99])

df_no_outliers = df[df.Income < percentile_99]
print("DataFrame without outliers:")
print(df_no_outliers)

print(df)
df['Income'][3] = np.nan  # Introduce a NaN value for demonstration
print("DataFrame with NaN value:")  
print(df)

df_new = df.fillna(df['Income'].median())
print("DataFrame after filling NaN with median:")
print(df_new)