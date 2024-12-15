# Uses the requests library for API use

import requests
# Uses the newsdata.io API to fetch the news
API_KEY = "pub_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
BASE_URL = "https://newsdata.io/api/1/news"

def fetch_news(keyword):
    params = {
        "apikey": API_KEY,
        "q": keyword,
        "language": "en",  # Grabs only english articles
        "country": "US",
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        print(f"Error: {response.status_code}")
        return []

keyword = input("Enter a keyword to search for news: ")
articles = fetch_news(keyword)
for article in articles:
    # Safely encode and decode the title and description to handle characters not supported by the current environment
    title = article.get('title', 'No title available.')
    description = article.get('description', 'No description available.')
    
    # Handle cases where description/Title is none
    title = title.encode('utf-8', errors='replace').decode('utf-8') if title else 'No title available.'
    description = description.encode('utf-8', errors='replace').decode('utf-8') if description else 'No description available.'
    # outputs the top 10 articles for said keyword in the past 48 hours
    print(f"Title: {title}")
    print(f"Description: {description}")
    print(f"URL: {article.get('link', 'No URL available.')}")
    print("-" * 80)
