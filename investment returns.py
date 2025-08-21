#initial_price = float(input('enter your initial investment: '))
#final_price = float(input('enter your final value: '))
#ROI = (final_price/initial_price)*100
#print(f'your ROI is: {ROI:.2f}%')

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

tickers = ["AAPL", "MSFT"]
data = yf.download(tickers, start="2023-01-01", end="2025-01-01")

if "Adj Close" in data.columns:
    data = data["Adj Close"]
else:
    data = data["Close"]

# Calculate daily returns
daily_returns = data.pct_change()

# Calculate cumulative returns
cumulative_returns = (1 + daily_returns).cumprod()

# Plot results
cumulative_returns.plot(figsize=(10,6))
plt.title("Portfolio Cumulative Returns (£100 invested)")
plt.ylabel("Growth")
plt.savefig("portfolio_returns.png", dpi=300, bbox_inches="tight")
plt.savefig('portfolio_returns.pdf', bbox_inches = 'tight')

plt.show()
