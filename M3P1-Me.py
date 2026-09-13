symbol = input("Enter Stock Symbol:")
stock = float(input("How much stock:"))
cost_per_share = float(input("What is the cost per share:"))

Investment = cost_per_share*stock

print(f"Your investment in {symbol} is ${Investment:.2f}")