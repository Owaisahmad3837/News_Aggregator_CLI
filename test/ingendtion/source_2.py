import os
from dotenv import load_dotenv
import pandas as pd
import requests
from pathlib import Path
load_dotenv()

api_key=os.getenv("GNewsApi")
output=Path("data/raw/soruce_2.parquet")
url = "https://gnews.io/api/v4/top-headlines"



response=requests.get(url,
                      params={
                        "apikey":api_key,
                        "language":"en",
                        "from": "2026-09-28",
                        "to": "2026-09-30"
                      })

data=response.json()

df=pd.DataFrame(data["articles"])

output.parent.mkdir(parents=True,exist_ok=True)
df.to_parquet(output,index=False)

print("Source 2 fetch Sucess.")
print("")
print(f"Source 2 save :{output}")