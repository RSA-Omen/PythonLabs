import requests

# YouTube Data API v3 example
# Get your API key from: https://console.developers.google.com/

API_KEY = "YOUR_API_KEY_HERE"  # Replace with your actual YouTube API key
BASE_URL = "https://www.googleapis.com/youtube/v3"

# Example 1: Search for videos
search_query = "python tutorial"
search_url = f"{BASE_URL}/search"

params = {
    "part": "snippet",
    "q": search_query,
    "key": API_KEY,
    "maxResults": 5,
    "type": "video"
}

response = requests.get(search_url, params=params)
print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    data = response.json()
    print(f"\nSearch Results for '{search_query}':\n")
    
    for item in data.get("items", []):
        title = item["snippet"]["title"]
        channel = item["snippet"]["channelTitle"]
        video_id = item["id"]["videoId"]
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        
        print(f"Title: {title}")
        print(f"Channel: {channel}")
        print(f"URL: {video_url}")
        print("-" * 50)
else:
    print(f"Error: {response.status_code}")
    print(response.text)