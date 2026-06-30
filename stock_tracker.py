stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 140,
    "MSFT": 300,
    "AMZN": 200,
    "META": 320
}

portfolio = {}
total = 0

print("=" * 45)
print("      STOCK PORTFOLIO TRACKER")
print("=" * 45)

while True:
    stock = input("\nEnter Stock Symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stocks:
        print("Stock not available.")
        continue

    try:
        quantity = int(input("Enter Quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

    except ValueError:
        print("Enter a valid number.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity

print("\n" + "=" * 45)
print("PORTFOLIO SUMMARY")
print("=" * 45)

if not portfolio:
    print("No stocks purchased.")
else:
    for stock, quantity in portfolio.items():
        price = stocks[stock]
        value = price * quantity
        total += value

        print(f"{stock}")
        print(f"Price    : ${price}")
        print(f"Quantity : {quantity}")
        print(f"Value    : ${value}")
        print("-" * 30)

    print(f"Total Investment = ${total}")

    with open("investment.txt", "w") as file:
        file.write("STOCK PORTFOLIO\n\n")

        for stock, quantity in portfolio.items():
            price = stocks[stock]
            value = price * quantity

            file.write(f"{stock}\n")
            file.write(f"Price : ${price}\n")
            file.write(f"Quantity : {quantity}\n")
            file.write(f"Value : ${value}\n\n")

        file.write(f"Total Investment = ${total}")

    print("\nPortfolio saved to investment.txt")
    