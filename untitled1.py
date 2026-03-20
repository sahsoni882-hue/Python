
# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#1. NumPy - Create random data

np.random.seed(42)
data = np.random.randn(100)

#2. Pandas - Create DataFrame

df = pd.DataFrame({
'Values': data,
'Category':np.random.choice(['A', 'B', 'C'], size = 100)
})


print("First 5 rows of DataFrame:")
print(df.head())

# 3.Matplotlib - Basic Plot

plt.figure(figsize=(6,4))
plt.plot(df['Values'], label='Values')
plt.title("Matplotlib Line Plot")
plt.xlabel("Index")
plt.ylabel("Values")
plt.legend()
plt.show()

# seaborn - advanced visualization

plt.figure(figsize=(6, 4))
sns.histplot(df['Values'], kde=True)
plt.title("Seaborn Histogram with KDE")
plt.show()

# 5. Seaborn - Boxplot by Category
plt.figure(figsize=(6, 4))
sns.boxplot(x='Category', y='Values', data=df)
plt.title("Boxplot by Category")
plt.show()

