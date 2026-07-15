from googleapiclient.discovery import build
from config import API_KEY

youtube = build("youtube", "v3", developerKey=API_KEY)

request = youtube.videos().list(
    part="snippet",
    chart="mostPopular",
    regionCode="AZ",
    videoCategoryId="10"
)

response = request.execute()

for video in response["items"]:
    print(video["snippet"]["title"])
