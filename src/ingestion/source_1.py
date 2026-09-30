import os
from dotenv import load_dotenv
import pandas as pd
import requests
from pathlib import Path
load_dotenv()

api_key=os.getenv("TheNewsApi")
url="https://api.thenewsapi.com/v1/news/top"
output=Path("data/raw/soruce_1.parquet")

def source_1():

 response=requests.get(url,
                      params={
                        "api_token":api_key,
                        "language":"en",
                        "published_after": "2026-09-28",
                        "published_before": "2026-09-30"
                      })

 data=response.json()

 df=pd.DataFrame(data["data"])

 output.parent.mkdir(parents=True,exist_ok=True)
 df.to_parquet(output,index=False)

 print("Source 1 fetch Sucess.")
 print("")
 print(f"Source 1 save :{output}")

