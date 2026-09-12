#Native Python aproach
import csv

def load_csv(filepath):
    data = []
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

data = load_csv("master_stock_data.csv")

# 1. First 2 rows
print("1. First 2 rows")
for row in data[:2]:
    print(row)

# 2. First row
print("\n2. First row")
print(data[0])

# 3. Rows 10–19
print("\n3. Rows 10–19")
for row in data[10:20]:
    print(row)

# 4. Column names
print("\n4. Column names")
print(list(data[0].keys()))

# 5. First 10 values of one column
print("\n5. First 10 values of 'Ticker'")
for row in data[:10]:
    print(row["Ticker"])

# 6. First 10 rows of three columns
print("\n6. First 10 rows of Date, Ticker, Close")
for row in data[:10]:
    print(row["Date"], row["Ticker"], row["Close"])
