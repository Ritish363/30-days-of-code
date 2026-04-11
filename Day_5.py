import numpy as np

data = np.random.randint(1, 101,size=5)

print("Data:", data)

print("Mean:", np.mean(data))
print("Standard Deviation:", np.std(data))
print("Min:", np.min(data))
print("Max:", np.max(data))