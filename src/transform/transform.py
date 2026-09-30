import pandas as pd
from pathlib import Path


source_path = Path("data/validation/Good/source.csv")

output = Path("data/Transform/Final_data/Final.csv")


def transform():
  df=pd.read_csv(source_path)

  df = df.drop_duplicates(subset=["title"])
  
  df["ID"] = range(1, len(df) + 1)
  df=df.rename(columns={
    "title":"Title",
    "description":"Description",
    "url":"Link",
    "published_at":"Published_Date"
    
  })
  df = df[
        [
            "ID",
            "Title",
            "Description",
            "Link",
            "Published_Date"
        ]
    ]

  output.parent.mkdir(parents=True, exist_ok=True)
  
  df.to_csv(output,index=False)
  print("Transform complete..")


