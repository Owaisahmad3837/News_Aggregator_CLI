import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()

api_key=os.getenv("TheNewsApi")

url="https://api.thenewsapi.com/v1/news/top"


response=requests.get(
  url,
  params={
        "api_token": api_key,
    "locale": "us",
    "published_after": "2026-09-28",
    "published_before": "2026-09-30",
    }
)

res=response.json()
status=response.status_code

print(status)


print(json.dumps(res, indent=4, ensure_ascii=False))