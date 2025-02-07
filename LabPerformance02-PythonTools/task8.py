import pandas as pd

file_path = "missing_data.csv"
df = pd.read_csv(file_path)

print("Dataset before filling missing values:")
print(df)

df.fillna(df.mean(numeric_only=True), inplace=True)

print("\nDataset after filling missing values:")
print(df)
