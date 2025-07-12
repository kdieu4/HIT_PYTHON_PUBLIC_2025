# Bài tập về nhà buổi 1

---
**Bài 1:**
Python là ngôn ngữ thông dịch hay biên dịch? Tại sao?

**Trả lời:**

Python được coi là một ngôn ngữ thông dịch.  
Vì mã nguồn Python được thực thi trực tiếp bởi
một trình thông dịch (interpreter), từng dòng một, thay vì được biên dịch thành mã máy trước khi chạy như trong các ngôn
ngữ biên dịch.

**Bài 2:**
Tìm hiểu trước kiến thức buổi 2 về:

- Các kiểu dữ liệu trong Python
- Các toán tử trong Python
- Mệnh đề điều kiện và vòng lặp
- Kiểu dữ liệu True, False

**Trả lời:**

1. Các kiểu dữ liệu trong python

| Kiểu       | Mô tả                                                               | Ví dụ                                                                        |
|------------|---------------------------------------------------------------------|------------------------------------------------------------------------------|
| int        | Số nguyên                                                           | `x = 10`                                                                     |
| float      | Số thực                                                             | `y = 3.14`                                                                   |
| complex    | Số phức                                                             | `z = 2 + 3j`                                                                 |
| boolean    | Kiểu logic (đúng/sai)                                               | `is_raining = False` <br/> `is_sunny = True`                                 |
| string     | Chuỗi ký tự                                                         | `str1 = 'Hello'`<br/> `str2 = "World"` <br/> `str3 = '''This is a String'''` |
| list       | Danh sách <br/>                                                     | `list = [1, 2, 3, 4, 5]`                                                     |
| tuple      | *Danh sách không đổi*                                               | `tupple1 = (1, 2, 3, 4, 5)`                                                  |
| set        | Kiểu dữ liệu tập hợp <br/> - Không có thứ tự <br/>- Không trùng lặp | `set = {1, 2, 3}` <br/> `set2 = set([1, 2, 3, 4, 5])`                        |
| dictionary | Kiểu dữ liệu từ điển <br/> - Có thứ tự <br/> - Không trùng lặp      | `dict1 = {"name" : "Dieu", "age" : 19, "city": "Tuyen Quang"}`               |

2. Các toán tử trong python

- Toán tử số học

| Toán tử | Mô tả       | Cú pháp  | Ví dụ       |
|---------|-------------|----------|-------------|
| `+`     | Cộng        | `a + b`  | 5 + 3 = 8   |
| `-`     | Trừ         | `a - b`  | 5 - 3 = 2   |
| `*`     | Nhân        | `a * b`  | 5 * 3 = 15  |
| `/`     | Chia        | `a / b`  | 5 / 2 = 2.5 |
| `**`    | Lũy thừa    | `a ** b` | 5 ** 2 = 25 |
| `%`     | Chia lấy dư | `a % b`  | 5 % 3 = 2   |

- Toán tử so sánh

| Toán tử | Mô tả             | Cú pháp  | Ví dụ             |
|---------|-------------------|----------|-------------------|
| `==`    | Bằng              | `a == b` | 5 == 5 `->`  True |
| `!=`    | Không bằng        | `a != b` | 5 != 3 `->` True  |
| `>`     | Lớn hơn           | `a > b`  | 5 > 3 `->` True   |
| `<`     | Nhỏ hơn           | `a < b`  | 5 < 3 `->` False  |
| `>=`    | Lớn hơn hoặc bằng | `a >= b` | 5 >= 3 `->` True  |
| `<=`    | Lớn hơn hoặc bằng | `a <= b` | 5 <= 3 `->` False |

- Toán tử logic

| Toán tử | Mô tả                                    | Cú pháp               | Kết quả |
|---------|------------------------------------------|-----------------------|---------|
| `and`   | Và (Đúng khi 2 biểu thức Đúng)           | `(5 > 3) and (5 < 8)` | True    |
| `or`    | Hoặc (Đúng khi 1 trong 2 biểu thức Đúng) | `(5 > 3) or (5 < -1)` | True    |
| `not`   | Phủ định (Đúng khi biểu thức Đúng)       | `not (5 > 3)`         | False   |

3. Mệnh đề điều kiện và vòng lặp

- Mệnh đề điều kiện: Thực hiện các khối mã nếu biểu thức điều kiện đúng, nếu khộng đúng thì có thể thực hiện khối mã
  khác
    - Câu lệnh if:
      ```python
      def is_sign_up(age):
            if age >= 100:
                print("You are too old to sign up!")
                # return False
            elif age >= 18:
                print("You are now signed up!")
                # return True
            elif age < 0:
                print("You haven't been born yet!")
                # return False
            else:
                print("You must be 18+ to sign up!")
                # return False
      ```
        - Câu lệnh Match-Case:
          ```python
          def is_weekend(day):
            match day:
                case 1:
                    print("It is a Sunday")
                    return True
                case 2:
                    print("It is a Monday")
                    return True
                case 3:
                    print("It is a Tuesday")
                    return True
                case 4:
                    print("It is a Wednesday")
                    return True
                case 5:
                    print("It is a Thursday")
                    return True
                case 6:
                    print("It is a Friday")
                    return True
                case 7:
                    print("It is a Saturday")
                    return True
                case _:
                    print("Not a valid day")  
                    return False
          ```
- Vòng lặp: lặp lại một khối mã nhiều lần, cho đến khi một điều kiện nào đó không còn đúng.
    - Vòng lặp while:
      ```python
      def enter_name():
            name = input("Enter your name: ")
            
            while name == "":
                print("You did not enter your name")
                name = input("Enter your name: ")
            print(f"Hello {name}")
      ```
    - Vòng lặp for: lặp với số lần xác định
        - Lặp về phía trước
      ```python
      for x in range(1, 11):
           print(str(x) + ' ') # 1 2 3 4 5 6 7 8 9 10 
      ```
        - Lặp ngược lại
      ```python
      for x in reversed(range(1, 11)):
           print(str(x) + ' ') # 10 9 8 7 6 5 4 3 2 1
      ```
        - Lặp có số bước
      ```python
      for x in range(1, 11, 2):
           print(str(x) + ' ') # 1 3 5 7 9 
      ```
        - Lặp với một chuỗi
      ```python
      def print (name):
        name = "Hoang Thanh Dieu"
        for x in name:
            print(x) 
      ```
        - Lệnh điều khiển vòng lặp: `continue` và `break`
      ```python
      for x in range(1, 9):
        if x == 6:
            continue
        else:
            print(str(x) + ' ') # 1 2 3 4 5 7 8  
      ```
      ```python
      for x in range(1, 9):
        if x == 6:
            break
        else:
            print(str(x) + ' ') # 1 2 3 4 5  
      ```

4. Kiểu dữ liệu True, False  
   Trong Python, kiểu dữ liệu True và False thuộc kiểu Boolean. Chỉ có hai giá trị:
    - True: Đại diện cho đúng, giá trị tương ứng với số 1.
      - False: Đại diện cho sai, giá trị tương ứng với số 0.
      ```python
      def test ():
          # Gán giá trị 
          is_alive = True
          is_eating = True
     
          # Sử dung trong mệnh đề điều kiện
          if is_alive:
              print("Thís man is alive")
          else:
              print("This man has dead")
     
          # Phép so sánh
          x = 10
          y = 5
          print(x > y) # True
          print(x == y) # False
      ```

* *Các giá trị như: 0, None, "" (chuỗi rỗng), [] (danh sách rỗng) được coi là False.*
* *Các giá trị khác được coi là True.*

>  Đã hoàn thành hẹ hẹ hẹ 🌻


