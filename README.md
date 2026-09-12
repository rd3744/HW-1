S&P 500 US Stock Market Data 2026 

## Why I Chose This Dataset
I chose the S&P 500 US Stock Market Data 2026 because of my personal interest in the stock market and its real data. 
The dataset stores pricing, volume, date/time, and even split and dividend data. 
This wide breath of data makes this dataset great for an assignment like this as we can ask and answer some really interesting questions about these stocks.
I also found this particular dataset interesting because this is something I would use if I wanted to backtest a particalur trading strategy.


## 3 Data Questions

# Question 1: How many trading days does AAPL appear in the dataset?
#count = 0
#for row in data:
#    if row["Ticker"] == "AAPL":
#        count += 1
#print(count)
# Output: 11521

Why the data structure supports this question:
Each row is one stock's price on one day, so counting the rows where
Ticker == "AAPL" gives the total number of trading days recorded for Apple.


# Question 2: How many rows recorded a dividend payment?
#div_count = 0
#for row in data:
#    if float(row["Dividends"]) > 0:
#        div_count += 1
#print(div_count)
# Output: 25992

Why the data structure supports this question:
Dividends is a numeric column where most rows are 0.0 and non-zero values indicate an actual payment. 
As each row is one stock-day observation, counting rows where Dividends > 0 tells us exactly how many times a
dividend was paid across all tickers and dates.


# Question 3: Which ticker has the most trading days in the dataset?
#ticker_counts = {}
#for row in data:
#    ticker = row["Ticker"]
#    if ticker in ticker_counts:
#        ticker_counts[ticker] += 1
#    else:
#        ticker_counts[ticker] = 1
#
#most_common = max(ticker_counts, key=lambda t: ticker_counts[t])
#print(most_common, ticker_counts[most_common])
# Output: CVX 16274

Why the data structure supports this question:
Because every row has a Ticker column, we can group rows by ticker and count them. 
The ticker with the highest count has the longest history in the dataset.
This works directly from the one-row-per-stock-per-day structure.


What the Data Cannot Answer:
A question I might want to ask is: "Which stock gave investors the best total return over the full period(the past 26-ish years)?"
This dataset cannot cleanly answer that because different tickers have different date ranges. For example, CVX has 16,274 rows
while a newer company might have only a few hundred. Comparing raw price change would be misleading since the starting dates differ. 
The dataset also has no column for shares outstanding or market cap, so there's no way to weight returns or account for the effects 
of a stock split on an investor's portfolio.

