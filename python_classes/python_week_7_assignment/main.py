# 📦 Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# 📥 Load Dataset
try:
    iris_raw = load_iris()
    iris_df = pd.DataFrame(data=iris_raw.data, columns=iris_raw.feature_names)
    iris_df['species'] = pd.Categorical.from_codes(iris_raw.target, iris_raw.target_names)
    print("✅ Dataset loaded successfully")
except Exception as e:
    print(f"❌ Error loading dataset: {e}")

# 👀 Task 1: Explore the Dataset
print("\n🔍 First 5 rows of the dataset:")
print(iris_df.head())

print("\n📊 Data types and missing values:")
print(iris_df.info())
print("\n🧼 Missing values per column:")
print(iris_df.isnull().sum())

# No missing values in Iris dataset, but here's how you'd clean:
# iris_df.dropna(inplace=True) or iris_df.fillna(method='ffill', inplace=True)

# 📈 Task 2: Basic Data Analysis
print("\n📋 Basic statistics:")
print(iris_df.describe())

print("\n📊 Mean values grouped by species:")
grouped = iris_df.groupby('species').mean()
print(grouped)

# 🧠 Observations
# Example: Setosa has smaller petal lengths compared to Virginica and Versicolor

# 🎨 Task 3: Visualizations
sns.set(style="whitegrid")

# 1️⃣ Line Chart: Simulated time-series using index
plt.figure(figsize=(8,5))
plt.plot(iris_df.index, iris_df['sepal length (cm)'], label='Sepal Length')
plt.title("Line Chart: Sepal Length Over Index")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.tight_layout()
plt.show()

# 2️⃣ Bar Chart: Average petal length per species
plt.figure(figsize=(6,4))
grouped['petal length (cm)'].plot(kind='bar', color='skyblue')
plt.title("Bar Chart: Avg Petal Length by Species")
plt.ylabel("Petal Length (cm)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 3️⃣ Histogram: Distribution of sepal width
plt.figure(figsize=(6,4))
plt.hist(iris_df['sepal width (cm)'], bins=15, color='salmon', edgecolor='black')
plt.title("Histogram: Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 4️⃣ Scatter Plot: Sepal vs Petal Length
plt.figure(figsize=(7,5))
sns.scatterplot(data=iris_df, x='sepal length (cm)', y='petal length (cm)', hue='species')
plt.title("Scatter Plot: Sepal vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.tight_layout()
plt.show()
