import pandas as pd

data = {
    "Name": ["A", "B", "C"],
    "Math": [80, 70, 60],
    "Science": [85, 75, 65]
}

df = pd.DataFrame(data)

print("Data:\n", df)

print("\nAverage Math:", df["Math"].mean())
print("Average Science:", df["Science"].mean())

print("\nMax Math:", df["Math"].max())
print("Max Science:", df["Science"].max())