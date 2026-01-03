import numpy as np

# Load the file
data = np.load('/Users/naghamdaood/Projects/Adapting-Recommender-Fashion/resources/data/dataset/embeddings/EfficientNet_V2_L_final/picture.0a0a918327f3470e87860e2344771490.npy')

# Print basic information
print(f"Array Shape: {data.shape}")
print(f"Data Type: {data.dtype}")
print(f"First 5 values: {data[:5]}")