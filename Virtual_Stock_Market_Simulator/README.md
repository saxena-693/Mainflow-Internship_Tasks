# Virtual Stock Market Simulator:-

## Objective:-
The **Virtual Stock Market Simulator** models a stock trading environment where users can:
- Track stock price fluctuations over time
- Buy and sell shares
- Monitor their portfolio balance
- Visualize stock performance with charts

This project simulates **realistic market dynamics** using randomness, volatility, and trends.


## Features:-
- **Stock price simulation** using random walk + upward/downward **trend bias**
- **Volatility factor** → each stock has its own risk level
- **Portfolio management** → balance, holdings, profit tracking
- **Buy/Sell system** with validation (enough balance or shares)
- **Automatic simulation loop** (demo mode with random buy/sell/hold)
- **Graphical visualization** of stock prices with `matplotlib`


## Technologies Used:-
- **Python 3**
- `random` - stock price fluctuations  
- `matplotlib` - stock price history visualization  


## Example console output:-
- ✤ Day 1
- TechCorp: 98.23
- AutoInc: 50.39
- PharmaLtd: 69.36
- Balance: 1000, Portfolio Value: 1000
- Bought 1 shares of PharmaLtd at 69.36


## At the end of the simulation, a chart will display stock price history:-
- X-axis -> Days
- Y-axis -> Price
- Separate line for each stock


## Restrictions:-
- No real-world stock data is used.
- Prices are simulated randomly with volatility and trend parameters.
- This is for demo purposes only, not financial advice.
