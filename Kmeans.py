from sklearn.cluster import KMeans
import numpy as np

# Hypothetical DNA sequence data (represented as vectors of nucleotide frequencies)
# Replace these with your actual DNA sequence data
dna_sequences = [
    [0.2, 0.3, 0.1, 0.4],  # Example DNA sequence 1
    [0.1, 0.2, 0.4, 0.3],  # Example DNA sequence 2
    # Add more DNA sequences here
]

# Convert the data to a numpy array
X = np.array(dna_sequences)

# Number of clusters (you might want to choose this based on domain knowledge or using techniques like the elbow method)
k = 2

# Initialize k-means clustering
kmeans = KMeans(n_clusters=k, random_state=42)

# Perform k-means clustering
kmeans.fit(X)

# Get the cluster assignments for each DNA sequence
cluster_assignments = kmeans.labels_

# Print the cluster assignments
print("Cluster Assignments:")
for i, label in enumerate(cluster_assignments):
    print(f"Sequence {i+1}: Cluster {label+1}")