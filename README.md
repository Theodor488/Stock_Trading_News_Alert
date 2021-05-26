# Stock Trading News Alert

The Stock Trading News Alert takes a company's recent closing stock prices, returns the percentage differences and return three relevant news headlines.

## Description

This program uses the Alpha Vantage API to get yesterday's and the day before yesterday's closing stock prices for TSLA. Given these close prices a message
containing the percentage difference between the two close prices and three relevant headlines are returned. 


## APIs Used Sources

https://www.alphavantage.co/

https://newsapi.org/


## Example Output

TSLA: 🔺4.31%
Yesterday Close: $606.44
Day Before Yesterday Close: $580.88

Headline: Fisker is building an electric popemobile
Brief: Electric vehicle startup Fisker Inc. says it’s building a custom version of its Ocean SUV for the Vatican, to be used as the so-called popemobile. Fisker says it will deliver the SUV next year.

Headline: Tesla says supports standardisation of China auto industry - Reuters
Brief: U.S. electric vehicle maker Tesla Inc (TSLA.O) said via Weibo on Wednesday that it supports standardisation of China auto industry.

Headline: Tesla to add EV components recycling facilities at Shanghai factory - Reuters
Brief: U.S. electric vehicle (EV) maker Tesla Inc (TSLA.O) plans to add facilities at its Shanghai factory to repair and reproduce key components such as electric motors and battery cells, a document submitted by Tesla to Shanghai authorities shows.
