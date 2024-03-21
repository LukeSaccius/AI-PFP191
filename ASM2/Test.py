def read_file(filename):
    stocks = {}  # Khởi tạo một dictionary rỗng để lưu trữ dữ liệu cổ phiếu
    days_data = []  # Tạo một list để theo dõi dữ liệu hàng ngày
    with open(filename, 'r') as file:  # Mở file để đọc
        n = int(file.readline().strip())  # Đọc số lượng mã cổ phiếu mỗi ngày
        lines = [line.strip() for line in file if line.strip() and not line.startswith('...')]  # Loại bỏ dòng trống và dòng bắt đầu bằng "..."

    for i in range(0, len(lines), n):  # Xử lý từng nhóm dữ liệu hàng ngày
        day_data = []  # Tạo một list để lưu trữ dữ liệu của từng ngày
        day_lines = lines[i:i + n]  # Lấy dữ liệu của từng ngày
        for line in day_lines:  # Xử lý từng dòng trong dữ liệu hàng ngày
            parts = line.split('\t')  # Tách dữ liệu dựa trên ký tự tab
            if len(parts) != 3:  # Bỏ qua dòng nếu không đủ 3 phần tử
                continue
            code, open_price, close_price = parts[0].strip(), float(parts[1].strip()), float(parts[2].strip())  # Lấy mã, giá mở cửa và giá đóng cửa
            if code not in stocks:
                stocks[code] = {'changes': [], 'close_prices': []}  # Nếu mã cổ phiếu chưa có trong dictionary, khởi tạo key và list rỗng
            change = close_price - open_price  # Tính sự thay đổi giá trong ngày
            stocks[code]['changes'].append(change)  # Thêm sự thay đổi vào list
            stocks[code]['close_prices'].append(close_price)  # Thêm giá đóng cửa vào list
            day_data.append((code, open_price, close_price))  # Thêm dữ liệu ngày vào list
        days_data.append(day_data)  # Thêm dữ liệu của từng ngày vào list chung

    # Tính toán sự thay đổi trung bình cho mỗi mã cổ phiếu sau khi đã đọc hết dữ liệu
    for code in stocks:
        stocks[code]['average_change'] = sum(stocks[code]['changes']) / len(stocks[code]['changes'])

    return stocks, days_data  # Trả về dictionary chứa dữ liệu cổ phiếu và list dữ liệu hàng ngày


def print_average_changes(stocks):
    for code in sorted(stocks.keys()):  # Duyệt qua từng mã cổ phiếu và in sự thay đổi trung bình
        avg_change = stocks[code]['average_change']
        print(f"{code}: Average Change: {avg_change:.3f}")


def search_by_code(stocks, code):
    if code in stocks:  # Kiểm tra xem mã cổ phiếu có tồn tại trong dữ liệu không
        highest_close = max(stocks[code]['close_prices'])  # Tìm giá đóng cửa cao nhất
        lowest_close = min(stocks[code]['close_prices'])  # Tìm giá đóng cửa thấp nhất
        print(f"{code}: Highest closing price: {highest_close:.3f}")
        print(f"{code}: Lowest closing price: {lowest_close:.3f}")
    else:
        print("Stock code not found.")  # In ra thông báo nếu mã không tồn tại


def increasing_trend(days_data):
    if len(days_data) < 2:  # Đảm bảo có ít nhất hai ngày dữ liệu
        print("Not enough data to determine trend.")
        return
    
    day1_stocks = {data[0] for data in days_data[0] if data[2] > data[1]}  # Lấy ra mã cổ phiếu tăng giá ngày đầu
    day2_stocks = {data[0] for data in days_data[1] if data[2] > data[1]}  # Lấy ra mã cổ phiếu tăng giá ngày thứ hai
    increasing_stocks = day1_stocks.intersection(day2_stocks) # Tìm giao của hai tập mã cổ phiếu tăng giá
    
    if increasing_stocks:
        print("Stock codes with an increasing trend on both day 1 and day 2:", ', '.join(sorted(increasing_stocks))) # In ra mã cổ phiếu tăng giá liên tiếp
    else:
        print("No stock codes with an increasing trend on both day 1 and day 2 found.") # Thông báo nếu không có mã nào tăng giá liên tiếp

def largest_increase_days(stocks):
    max_days = 0 # Biến lưu trữ số ngày tăng giá lớn nhất
    codes = [] # List lưu trữ các mã cổ phiếu có số ngày tăng giá lớn nhất
    for code in stocks: # Duyệt qua từng mã cổ phiếu
        increase_days = sum(1 for change in stocks[code]['changes'] if change > 0) # Đếm số ngày giá tăng
        if increase_days > max_days: # Nếu số ngày tăng nhiều hơn giá trị hiện tại
            max_days = increase_days # Cập nhật số ngày tăng giá lớn nhất
            codes = [code] # Lưu mã cổ phiếu
        elif increase_days == max_days: # Nếu số ngày tăng giá bằng với giá trị lớn nhất hiện tại
            codes.append(code) # Thêm mã cổ phiếu vào danh sách
    print("Stock codes with the largest increase in days:", ', '.join(codes), f"with {max_days} days.") # In ra các mã và số ngày tăng giá lớn nhất

def main_menu():
    stocks_data = {} # Khởi tạo dictionary rỗng để lưu trữ dữ liệu cổ phiếu
    days_data = [] # Khởi tạo list rỗng để lưu trữ dữ liệu theo ngày
    filename = "data.txt" # Đặt tên file chứa dữ liệu
    while True:
    print("\nMAIN MENU")  # In menu chính
    print("1. Print average changes")  # Lựa chọn in sự thay đổi giá trung bình
    print("2. Search by stock code")  # Lựa chọn tìm kiếm theo mã cổ phiếu
    print("3. Search for stock codes with an increasing trend")  # Lựa chọn tìm kiếm mã cổ phiếu theo xu hướng tăng giá
    print("4. Find the code with the largest increase in days")  # Lựa chọn tìm mã cổ phiếu tăng giá nhiều ngày nhất
    print("5. Exit")  # Lựa chọn thoát chương trình
    choice = input("Enter your choice: ")  # Nhận lựa chọn từ người dùng

    if choice == '1':
        if not stocks_data:  # Nếu chưa có dữ liệu, đọc file
            stocks_data, days_data = read_file(filename)  # Đọc file và lấy dữ liệu
        print_average_changes(stocks_data)  # In sự thay đổi giá trung bình
    elif choice == '2':
        if not stocks_data:  # Nếu chưa có dữ liệu, đọc file
            stocks_data, _ = read_file(filename)  # Đọc file và lấy dữ liệu cổ phiếu
        code = input("Enter stock code: ").upper()  # Nhận mã cổ phiếu từ người dùng
        search_by_code(stocks_data, code)  # Tìm kiếm và in kết quả theo mã
    elif choice == '3':
        if not days_data:  # Nếu chưa có dữ liệu theo ngày, đọc file
            _, days_data = read_file(filename)  # Đọc file và lấy dữ liệu theo ngày
        increasing_trend(days_data)  # Tìm và in mã cổ phiếu có xu hướng tăng
    elif choice == '4':
        if not stocks_data:  # Nếu chưa có dữ liệu, đọc file
            stocks_data, _ = read_file(filename) # Đọc file và lấy dữ liệu cổ phiếu
            largest_increase_days(stocks_data) # Tìm và in mã cổ phiếu có số ngày tăng giá lớn nhất
    elif choice == '5':
        print("Exiting the program.") # Thông báo thoát chương trình
        print("Author: [Lê Thông Tấn], [HE190505]") # In thông tin tác giả
        break # Thoát vòng lặp và kết thúc chương trình
    else:
        print("Invalid choice. Please try again.") # Nếu lựa chọn không hợp lệ, yêu cầu người dùng nhập lại
        

if __name__ == "__main__":
    main_menu()