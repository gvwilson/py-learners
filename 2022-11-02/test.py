import pandas as pd

df = pd.DataFrame({
    "color": ["red", "red", "green", "blue"],
    "name": ["alpha", "beta", "gamma", "delta"],
    "count": [1, 2, 3, 4],
    "significance": [10, 20, 30, 40]
})
print(df)
print("-" * 40)
print(df.melt(id_vars=["color", "name"]))

print("-" * 40)

df = pd.DataFrame({
    "row_id": [1, 2, 3, 4],
    "A": [11, 12, 13, 14],
    "B": [21, 22, 23, 24],
    "C": [31, 32, 33, 34]
})
print(df)
print("-" * 40)
print(df.melt(id_vars=["row_id"], var_name="col_id"))
