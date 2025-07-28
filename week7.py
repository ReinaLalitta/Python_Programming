import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = [iris.target_names[i] for i in iris.target]

# Task 2.1: Basic statistics
print("Basic Statistics:")
print(df.describe())

# Task 2.2: Group by species and calculate mean
print("\nMean of each feature by species:")
print(df.groupby('species').mean())

# Task 3: Data Visualization
plt.figure(figsize=(15, 10))

# 1. Line chart - Using index as time proxy
plt.subplot(2, 2, 1)
for species in df['species'].unique():
    species_data = df[df['species'] == species]
    plt.plot(species_data.index, species_data['sepal length (cm)'], 
             'o-', label=species)
plt.title('Sepal Length Trend by Species')
plt.xlabel('Observation')
plt.ylabel('Sepal Length (cm)')
plt.legend()

# 2. Bar chart
plt.subplot(2, 2, 2)
sns.barplot(x='species', y='petal length (cm)', data=df)
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')

# 3. Histogram
plt.subplot(2, 2, 3)
sns.histplot(data=df, x='sepal width (cm)', hue='species', 
             element='step', stat='density', common_norm=False)
plt.title('Distribution of Sepal Width by Species')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Density')

# 4. Scatter plot
plt.subplot(2, 2, 4)
sns.scatterplot(data=df, x='sepal length (cm)', 
                y='petal length (cm)', hue='species')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')

plt.tight_layout()
plt.show()

# Additional analysis
print("\nInteresting Findings:")
print("1. Setosa species has significantly smaller petals compared to others")
print("2. Virginica has the longest petals on average")
print("3. Versicolor and Virginica have some overlap in sepal width")
print("4. There's a strong positive correlation between petal length and sepal length")