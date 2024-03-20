def read_file(filename):
    stocks = {}
    days_data = []  # Add a list to keep track of daily data
    with open(filename, 'r') as file:
        n = int(file.readline().strip())  # Number of stock codes per day
        lines = [line.strip() for line in file if line.strip() and not line.startswith('...')]

    for i in range(0, len(lines), n):
        day_data = []  # Add a list to keep track of each day's stock data
        day_lines = lines[i:i + n]
        for line in day_lines:
            parts = line.split('\t')
            if len(parts) != 3:  # This might skip the "..." lines, but check your file for any other inconsistencies
                continue  # Skip lines that do not have exactly 3 parts
            code, open_price, close_price = parts[0].strip(), float(parts[1].strip()), float(parts[2].strip())
            if code not in stocks:
                stocks[code] = {'changes': [], 'close_prices': []}
            change = close_price - open_price
            stocks[code]['changes'].append(change)
            stocks[code]['close_prices'].append(close_price)
            day_data.append((code, open_price, close_price))  # Add a tuple of the day's data
        days_data.append(day_data)  # Append each day's data to the days_data list

    # Calculate the average change for each stock code after all data is read
    for code in stocks:
        stocks[code]['average_change'] = sum(stocks[code]['changes']) / len(stocks[code]['changes'])

    return stocks, days_data  # Return both the stocks dictionary and the day-wise data



def print_average_changes(stocks):
    for code in sorted(stocks.keys()):
        avg_change = stocks[code]['average_change']
        print(f"{code}: Average Change: {avg_change:.3f}")



def search_by_code(stocks, code):
    if code in stocks:
        highest_close = max(stocks[code]['close_prices'])
        lowest_close = min(stocks[code]['close_prices'])
        print(f"{code}: Highest closing price: {highest_close:.3f}")
        print(f"{code}: Lowest closing price: {lowest_close:.3f}")
    else:
        print("Stock code not found.")
        
def increasing_trend(days_data):
    if len(days_data) < 2:  # Ensure there are at least two days of data
        print("Not enough data to determine trend.")
        return
    
    day1_stocks = {data[0] for data in days_data[0] if data[2] > data[1]}  # Stocks that increased on day 1
    day2_stocks = {data[0] for data in days_data[1] if data[2] > data[1]}  # Stocks that increased on day 2

    # Find intersection of stocks that increased on both days
    increasing_stocks = day1_stocks.intersection(day2_stocks)
    if increasing_stocks:
        print("Stock codes with an increasing trend on both day 1 and day 2:", ', '.join(sorted(increasing_stocks)))
    else:
        print("No stock codes with an increasing trend on both day 1 and day 2 found.")

def largest_increase_days(stocks):
    max_days = 0
    codes = []
    for code in stocks:
        increase_days = sum(1 for change in stocks[code]['changes'] if change > 0)
        if increase_days > max_days:
            max_days = increase_days
            codes = [code]
        elif increase_days == max_days:
            codes.append(code)
    print("Stock codes with the largest increase in days:", ', '.join(codes), f"with {max_days} days.")
def main_menu():
    stocks_data = {}
    days_data = []  # Initialize days_data
    filename = "data.txt"

    while True:
        print("\nMAIN MENU")
        print("1. Print average changes")
        print("2. Search by stock code")
        print("3. Search for stock codes with an increasing trend")
        print("4. Find the code with the largest increase in days")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            if not stocks_data:
                stocks_data, days_data = read_file(filename)  # Unpack the two return values
            print_average_changes(stocks_data)
        elif choice == '2':
            if not stocks_data:
                stocks_data, _ = read_file(filename)  # Only need stocks_data for this option
            code = input("Enter stock code: ").upper()
            search_by_code(stocks_data, code)
        elif choice == '3':
            if not days_data:  # Make sure we have day-wise data before attempting to find the trend
                _, days_data = read_file(filename)
            increasing_trend(days_data)
        elif choice == '4':
            if not stocks_data:
                stocks_data, _ = read_file(filename)
            largest_increase_days(stocks_data)
        elif choice == '5':
            print("Exiting the program.")
            print("Author: [Lê Thông Tấn], [HE190505]")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()