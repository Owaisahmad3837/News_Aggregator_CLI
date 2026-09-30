import os
from dotenv import load_dotenv
import requests
import json
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


res=response.json()
status=response.status_code

print(status)


print(json.dumps(res, indent=4, ensure_ascii=False))

