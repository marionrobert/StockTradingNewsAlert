import requests
import datetime
import smtplib
import os


STOCK = "TSLA"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
ALPHAVANTAGE_API_KEY = os.environ["ALPHAVANTAGE_API_KEY"]
ALPHAVANTAGE_PARAMS = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_API_KEY
}

COMPANY_NAME = "Tesla Inc"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ["NEWS_API_KEY"]
NEWS_PARAMS = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}

MY_EMAIL = os.environ["MY_EMAIL"]
GMAIL_SERVER = "smtp.gmail.com"
MY_PASSWORD = os.environ["MY_PASSWORD"]
EMAIL_TEST = os.environ["EMAIL_TEST"]


## STEP 1: When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(STOCK_ENDPOINT, ALPHAVANTAGE_PARAMS)
response.raise_for_status()
data = response.json()
days_data = data["Time Series (Daily)"]

# # my_way
# days_closing_hours = {key: days_data[key]["4. close"] for (key, value) in last_days_data.items()}
# yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
# before_yesterday = (datetime.date.today() - datetime.timedelta(days=2)).strftime("%Y-%m-%d")
# yesterday_closing_price = float(days_closing_hours[yesterday])
# before_yesterday_closing_price = float(days_closing_hours[before_yesterday])

# solution
data_list = [value for (key, value) in days_data.items()]
yesterday_closing_price = float(data_list[0]["4. close"])
before_yesterday_closing_price = float(data_list[1]["4. close"])

# Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20
positive_difference = abs(yesterday_closing_price - before_yesterday_closing_price)

# Work out the percentage difference in price between yesterday and before yesterday
diff_percent = round(positive_difference / yesterday_closing_price * 100)
up_down_sign = None

if diff_percent > 0:
    up_down_sign = "+"
else:
    up_down_sign = "-"


if diff_percent >= 3:
    ## STEP 2: Use https://newsapi.org/docs/endpoints/everything and fetch the first 3 articles for the COMPANY_NAME.
    response_news = requests.get(NEWS_ENDPOINT, NEWS_PARAMS)
    response_news.raise_for_status()
    data_news = response_news.json()
    three_articles = data_news["articles"][:3]

    ## STEP 3: Use smtplib and send a separate message with each article's title and description to your phone number.
    formatted_articles_list = []
    for article in three_articles:
        title = (article['title']).encode('ascii', 'ignore').decode('ascii')
        description = (article['description']).encode('ascii', 'ignore').decode('ascii')
        formatted_articles_list.append(f"Subject: TSLA: {up_down_sign}{diff_percent}%\n\nHeadline: {title}. \nBrief: {description}.")

    with smtplib.SMTP(GMAIL_SERVER) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        for article in formatted_articles_list:
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=EMAIL_TEST,
                                msg=f"{article}")


