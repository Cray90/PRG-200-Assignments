import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('nepal_bank_transactions.csv')

print(df.columns)
print("-" * 100)
print(df.head())
print("-" * 100)
print(df.tail())
print("-" * 100)

print(df.info())
print("-" * 100)

print(df.shape)
print("-" * 100)

print(df.describe())
print("-" * 100)

print(df["channel"].head())
print("-" * 100)

print(df[["branch_name", "channel", "amount_npr"]].head())
print("-" * 100)

print(df.loc[0, "branch_name"])
print(df.iloc[0, 3])
print("-" * 100)

print(df.loc[0:2, ["branch_name", "channel", "transaction_status"]])
print("-" * 100)

atm_withdrawals = df[
    (df["channel"] == "ATM") &
    (df["transaction_type"] == "Cash Withdrawal")
]

print(f"ATM cash withdrawals: {len(atm_withdrawals)}")
print(atm_withdrawals.head())
print("-" * 100)

not_successful = df[df["transaction_status"] != "Success"]

print(
    f"Not Successful: {len(not_successful)} out of {len(df)} "
    f"({len(not_successful) / len(df):.1%})"
)

print(not_successful["transaction_status"].value_counts())
print("-" * 100)

large_transfers = df[
    (df["transaction_type"] == "Fund Transfer") &
    (df["amount_npr"] > 50000)
]

print(f"Large fund transfers (> NPR 50,000): {len(large_transfers)}")
print("-" * 100)

print(
    df.sort_values("amount_npr", ascending=False).head(10)[
        [
            "transaction_id",
            "branch_name",
            "transaction_type",
            "amount_npr",
            "transaction_status",
        ]
    ]
)