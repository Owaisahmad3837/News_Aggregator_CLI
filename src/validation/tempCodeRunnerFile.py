import pandas as pd
from pathlib import Path


source_1_path = Path("data/raw/soruce_1.parquet")
source_2_path = Path("data/raw/soruce_2.parquet")

output = Path("data/validation/Good/source.csv")


def source_1():

    df = pd.read_parquet(source_1_path)

    df = df[
        [
            "title",
            "description",
            "url",
            "published_at"
        ]
    ]

    return df


def source_2():

    df = pd.read_parquet(source_2_path)

    df = df[
        [
            "title",
            "description",
            "url",
            "publishedAt"
        ]
    ]

    # Make column name the same as Source 1
    df = df.rename(columns={
        "publishedAt": "published_at"
    })

    return df


def validate_and_save():

    df1 = source_1()
    df2 = source_2()

    # Validate Source 1
    if df1["title"].isnull().any() or df1["url"].isnull().any():
        print("Source 1: Invalid data found")
        return

    # Validate Source 2
    if df2["title"].isnull().any() or df2["url"].isnull().any():
        print("Source 2: Invalid data found")
        return

    # Combine both sources
    df = pd.concat([df1, df2], ignore_index=True)

    # Save one CSV
    output.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output, index=False)

    print("Both sources validated and saved successfully")


validate_and_save()