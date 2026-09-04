import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Read the dataset
data = pd.read_csv("Mall_Customers.csv")

# Select the columns for clustering
X = data[["Annual Income (k$)", "Spending Score (1-100)"]]

# Create K-Means model
kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)

# Train the model
kmeans.fit(X)

# Add cluster number to the dataset
data["Cluster"] = kmeans.labels_

# Display the result
print(data)

plt.scatter(
    X["Annual Income (k$)"],
    X["Spending Score (1-100)"],
    c=data["Cluster"]
)

plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.title("Customer Segmentation using K-Means")

plt.show()
