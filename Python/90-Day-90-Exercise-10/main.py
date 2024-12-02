import requests


def fetch_news(api_key, topic):
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        news_data = response.json()
        articles = news_data['articles']

        for article in articles:
            print(article['title'])
    else:
        print("Failed to fetch news. Error:", response.status_code)


# Provide your NewsAPI key here
api_key = "3a440bf7953040369816f6dc4f7cd0f3"
print("Select a topic:")
print("1. Sports")
print("2. Business")
print("3. Others")
topic_choice = input(
    "Enter the corresponding number for the topic you want to fetch: ")
if topic_choice == "1":
    topic = "sports"
    fetch_news(api_key, topic)
elif topic_choice == "2":
    topic = "business"
    fetch_news(api_key, topic)
else:
    topic = "world"  # default to fetch news related to the world if an invalid choice is entered
    fetch_news(api_key, topic)
