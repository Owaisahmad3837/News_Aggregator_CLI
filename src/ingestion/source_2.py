import os
from dotenv import load_dotenv
import requests
load_dotenv()

api_key=os.getenv("GNewsApi")
url = "https://gnews.io/api/v4/top-headlines"



response=requests.get(url,
                      params={
                        "apikey":api_key,
                        "language":"en",
                        "from": "2026-09-28",
                        "to": "2026-09-30"
                      })


status=response.status_code

print(status)

res=response.text

print(res)