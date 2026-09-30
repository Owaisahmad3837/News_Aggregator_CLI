import os
import requests
from dotenv import load_dotenv


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

status=response.status_code

print(status)

res=response.text

print(res)
