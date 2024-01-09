def get_grade(decimal_grade, grading_scale):
    for threshold, grade in grading_scale:
        if decimal_grade >= threshold:
            return grade
    return grading_scale[-1][1]  # Return the lowest grade if no other grade matches
# #Hàm get_grade() nhận vào hai tham số: decimal_grade, là điểm số dạng thập phân mà người dùng nhập vào, và grading_scale, là một danh sách các bộ giá trị (tuples) mà mỗi bộ chứa một ngưỡng điểm số và xếp loại tương ứng cho ngưỡng đó.

# Dưới đây là cách thức hoạt động của hàm:

# Hàm bắt đầu bằng việc lặp qua từng bộ giá trị (tuple) trong danh sách grading_scale. Mỗi bộ giá trị được định nghĩa như là (threshold, grade), nơi threshold là ngưỡng điểm số và grade là xếp loại tương ứng.

# Với mỗi bộ giá trị trong vòng lặp, hàm kiểm tra xem decimal_grade có lớn hơn hoặc bằng threshold hay không. Nếu có, hàm sẽ trả về grade tương ứng với ngưỡng điểm đó.

# Nếu decimal_grade không lớn hơn hoặc bằng ngưỡng nào cả, sau khi kết thúc vòng lặp, hàm sẽ trả về xếp loại cuối cùng trong danh sách, tức là xếp loại thấp nhất.

# Danh sách grading_scale được sắp xếp từ cao xuống thấp theo ngưỡng điểm, điều này đảm bảo rằng vòng lặp sẽ kiểm tra từ xếp loại cao nhất xuống thấp nhất.

# Define the grading scales
alphabetic_grading_scale = [
    (9, "A+"), (8, "A"), (7, "B"), (6, "C"), (5, "D"), (0, "F")
]

fourth_system_grading_scale = [
    (8.5, "4.0"), (8, "3.7"), (7, "3.0"), (6, "2.0"), (5, "1.0"), (0, "0.0")
]

# Example usage with input validation
while True:
    try:
        grade_input = input("Enter the grade of a subject in decimal system (0 to 10): ")
        grade = float(grade_input)
        if 0 <= grade <= 10:
            alpha_grade = get_grade(grade, alphabetic_grading_scale)
            system4_grade = get_grade(grade, fourth_system_grading_scale)
            print(f"Corresponding alphabetic grade: {alpha_grade}")
            print(f"Corresponding 4th system grade: {system4_grade}")
            break
        else:
            print("Grade must be between 0 and 10.")
    except ValueError:
        print("Please enter a valid decimal number for the grade.")
