import requests

print("Job bot started")

url = "https://remoteok.com/api"

jobs = requests.get(url).json()

for job in jobs:

    title = job.get("position")

    if title:
        if "system" in title.lower() or "azure" in title.lower():
            print("Relevant job found:", title)
