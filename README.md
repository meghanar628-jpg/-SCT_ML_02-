# -SCT_ML_02-
K-Means clustering for customer segmentation using the Mall Customer dataset.
K-Means Customer Segmentation
Project Overview
This project uses the K-Means Clustering algorithm to segment customers based on their Annual Income and Spending Score.

The goal is to group customers with similar purchasing behavior into different clusters. This can help businesses understand their customers and make better marketing decisions.

Dataset
The project uses the Mall Customers Dataset.

The main features used for clustering are:

Annual Income (k$)
Spending Score (1-100)
Algorithm Used
K-Means Clustering
K-Means is an unsupervised machine learning algorithm that divides data points into a specified number of clusters based on their similarity.

In this project, the customers are divided into 5 clusters.

Technologies Used
Python
Pandas
Matplotlib
Scikit-learn
Project Structure
KMeans-Clustering/
│
├── Mall_Customers.csv
├── kmeans_clustering.py
└── README.md
How to Run
1. Clone the repository
git clone https://github.com/nadavigowda13/KMeans-Clustering.git
2. Navigate to the project folder
cd KMeans-Clustering
3. Install the required libraries
pip install pandas matplotlib scikit-learn
4. Run the Python program
python kmeans_clustering.py
Output
The program generates a scatter plot showing the different customer clusters based on annual income and spending score.

Objective
The main objective of this project is to understand how K-Means Clustering can be used for customer segmentation and to identify groups of customers with similar characteristics.

Author
MEGHANA R
