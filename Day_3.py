import numpy as np

marks = np.array([
    [80, 85, 90],
    [70, 75, 80],
    [60, 65, 70]
])

print("Marks:\n", marks)

total = np.sum(marks, axis=1)
print("Total marks:", total)

average = np.mean(marks, axis=1)
print("Average marks:", average)

highest = np.max(marks, axis=0)
print("Highest marks per subject:", highest)