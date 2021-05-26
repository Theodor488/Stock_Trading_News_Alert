import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_API_KEY = "INSERT_KEY"
NEWS_API_KEY = "INSERT_KEY"


# Use https://www.alphavantage.co to get stock info (yesterday close and day before yesterday close)

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_API_KEY
}

response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
data = response.json()

daily_series = list(data["Time Series (Daily)"])
yesterday = daily_series[1]
day_before_yesterday = daily_series[2]

yesterday_close = float(data["Time Series (Daily)"][yesterday]["4. close"])
day_before_yesterday_close = float(data["Time Series (Daily)"][day_before_yesterday]["4. close"])


# percentage difference between yesterday's close and the day before yesterday's close

percent_diff = round(abs(yesterday_close - day_before_yesterday_close) / ((yesterday_close + day_before_yesterday_close)/2) * 100, 2)
arrow = ""

if yesterday_close > day_before_yesterday_close:
    arrow = "🔺"
elif yesterday_close < day_before_yesterday_close:
    arrow = "🔻"
else:
    arrow = "="


# Use https://newsapi.org to get 3 relevant headlines involving the company name

parameters = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME
}

news_response = requests.get(url="https://newsapi.org/v2/everything", params=parameters)
news_response.raise_for_status()
data = news_response.json()

stock_info = f"\n{STOCK}: {arrow}{percent_diff}%" \
                 f"\nYesterday Close: ${yesterday_close}" \
                 f"\nDay Before Yesterday Close: ${day_before_yesterday_close}"

print(stock_info)

# Return 3 headlines

for i in range(0, 3):
    articles_title = list(data['articles'])[i]["title"]
    article_brief = list(data['articles'])[i]["description"]

    articles_text = f"\nHeadline: {articles_title}" \
           f"\nBrief: {article_brief}"

    print(articles_text)

