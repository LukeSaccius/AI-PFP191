def read_file(filename):
    stocks = {} # Khởi tạo một dictionary rỗng để lưu trữ dữ liệu cổ phiếu
    days_data = []  # Tạo một list để theo dõi dữ liệu hàng ngày
    with open(filename, 'r') as file: # Mở file để đọc
        n = int(file.readline().strip())  # Đọc số lượng mã cổ phiếu mỗi ngày
        lines = [line.strip() for line in file if line.strip() and not line.startswith('...')] # Loại bỏ dòng trống và dòng bắt đầu bằng "..."

    for i in range(0, len(lines), n): # Xử lý từng nhóm dữ liệu hàng ngày
        day_data = [] # Tạo một list để lưu trữ dữ liệu của từng ngày
        day_lines = lines[i:i + n]  # Lấy dữ liệu của từng ngày
        for line in day_lines: # Xử lý từng dòng trong dữ liệu hàng ngày
            parts = line.split('\t')  # Tách dữ liệu dựa trên ký tự tab
            if len(parts) != 3: # Bỏ qua dòng nếu không đủ 3 phần tử
                continue  # Skip lines that do not have exactly 3 parts
            code, open_price, close_price = parts[0].strip(), float(parts[1].strip()), float(parts[2].strip())  # Lấy mã, giá mở cửa và giá đóng cửa
            if code not in stocks:
                stocks[code] = {'changes': [], 'close_prices': []} # Nếu mã cổ phiếu chưa có trong dictionary, khởi tạo key và list rỗng
            change = close_price - open_price # Tính sự thay đổi giá trong ngày
            stocks[code]['changes'].append(change) # Thêm sự thay đổi vào list
            stocks[code]['close_prices'].append(close_price)  # Thêm giá đóng cửa vào list
            day_data.append((code, open_price, close_price))  # Thêm dữ liệu ngày vào list
        days_data.append(day_data)   # Thêm dữ liệu của từng ngày vào list chung

     # Tính toán sự thay đổi trung bình cho mỗi mã cổ phiếu sau khi đã đọc hết dữ liệu
    for code in stocks:
        stocks[code]['average_change'] = sum(stocks[code]['changes']) / len(stocks[code]['changes'])

    return stocks, days_data  # Trả về dictionary chứa dữ liệu cổ phiếu và list dữ liệu hàng ngày



def print_average_changes(stocks):
    for code in sorted(stocks.keys()): # Duyệt qua từng mã cổ phiếu và in sự thay đổi trung bình
        avg_change = stocks[code]['average_change']
        print(f"{code}: Average Change: {avg_change:.3f}")



def search_by_code(stocks, code):
    if code in stocks:  # Kiểm tra xem mã cổ phiếu có tồn tại trong dữ liệu không
        highest_close = max(stocks[code]['close_prices']) # Tìm giá đóng cửa cao nhất
        lowest_close = min(stocks[code]['close_prices']) # Tìm giá đóng cửa thấp nhất
        print(f"{code}: Highest closing price: {highest_close:.3f}")
        print(f"{code}: Lowest closing price: {lowest_close:.3f}")
    else:
        print("Stock code not found.")  # In ra thông báo nếu mã không tồn tại
        

def find_increasing_trends_with_days(days_data):
    trends_result = {}

    # Iterate through each stock
    for code in {code for day in days_data for code, _, _ in day}:
        # Reset for each stock code
        current_streak = 0
        longest_streak = 0
        start_day_of_longest = None
        for i in range(len(days_data) - 1):
            day_data = [entry for entry in days_data[i] if entry[0] == code]
            next_day_data = [entry for entry in days_data[i + 1] if entry[0] == code]

            if day_data and next_day_data:
                # Only check if there is data for the stock on consecutive days
                _, open_price, close_price = day_data[0]
                _, next_open_price, next_close_price = next_day_data[0]

                if close_price > open_price and next_close_price > next_open_price:
                    if current_streak == 0:
                        # Start of a new streak
                        current_start_day = i
                    # Increment current streak since the stock increased on consecutive days
                    current_streak += 1
                else:
                    # Streak ends, compare with longest streak
                    if current_streak > longest_streak:
                        longest_streak = current_streak
                        start_day_of_longest = current_start_day
                    # Reset current streak
                    current_streak = 0

        # Check last streak if it ended on the last day
        if current_streak > longest_streak:
            longest_streak = current_streak
            start_day_of_longest = current_start_day

        if longest_streak > 0:
            trends_result[code] = {
                'days': longest_streak + 1,  # +1 because the streak includes both start and end day
                'start_day': start_day_of_longest + 1,  # +1 to match your day counting (starting from 1)
                'end_day': start_day_of_longest + longest_streak + 1  # End day is the last day of the streak
            }

    # Print the results
    for code, info in trends_result.items():
        print(f"{code}: {info['days']} days, from day {info['start_day']} to day {info['end_day']}")


def largest_increase_days(stocks):
    max_days = 0
    codes_with_max_days = []  # This will store all codes with the maximum increase days

    # Calculate the number of days each stock has increased
    for code, data in stocks.items():
        increase_days = sum(1 for change in data['changes'] if change > 0)

        # If this stock has more increase days than the current max, update the max
        if increase_days > max_days:
            max_days = increase_days
            codes_with_max_days = [code]  # Reset the list with the new code
        # If this stock has the same number of increase days as the current max, add it to the list
        elif increase_days == max_days:
            codes_with_max_days.append(code)

    # Print the result
    if codes_with_max_days:
        codes_str = ', '.join(codes_with_max_days)
        print(f"Stock code(s) with the largest number of increase days are: {codes_str} each with {max_days} days.")
    else:
        print("No stock codes found with an increasing trend.")

        
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
            if not days_data:  # Make sure have day-wise data before attempting to find the trend
                _, days_data = read_file(filename)
                find_increasing_trends_with_days(days_data)
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