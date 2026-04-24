# ===== HOMEWORK 2 - PYTHON BUỔI 2 =====
# Chủ đề: Vòng lặp (Loop), Hàm (Function)
# Vòng lặp (Loop): for loop với range(), Vòng lặp lồng nhau (nested loop), Câu lệnh break / Câu lệnh continue, và vòng lặp white (while loop).
# Hàm (Function): cú pháp def, Tham số (parameter) và Đối số (argument), Câu lệnh return, keyword argument, default argument, Hàm lồng nhau ( Nested function), PHẠM VI (Scope)(Toàn cục (global) / (Cục bộ) local / ( Bao ngoài) enclosing), Hàm vô danh (lambda function), và các built-in function phổ biến.

# Họ tên: [Trần Thị Thủy Tiên]_BrSE AI
# Ngày: 17-24/04/2026
# =======================================

# Bài 1: In danh sách sản phẩm (có index)
products = ["Áo", "Quần", "Giày", "Mũ"]
for i in range(len(products)):
    print(f"{i+1}. {products[i]}")

# Bài 2: Tính tổng tiền giỏ hàng
prices = [100000, 200000, 150000]
total = 0
for price in prices:
    total += price
print("Tong tien: ", total, "VND")

# Bài 3: Đếm sản phẩm giá cao
prices = [100000, 500000, 700000, 200000]
i = 0
for price in prices:
    if price > 300000:
        i += 1
print(f"Số sản phẩm có giá trên 300000 VND: {i}")

# Bài 4: Tìm giá lớn nhất
prices = [100000, 500000, 700000, 200000]
max_price = prices[0]
for price in prices:
    if price > max_price:
        max_price = price
print(f"Giá sản phẩm cao nhất: {max_price} VND")

# Bài 5: Tổng số chẵn
numbers = [1, 2, 3, 4, 5, 6]
total_even = 0
for number in numbers:
    if number % 2 == 0:
        total_even += number
print("Tong chan: " + str(total_even))

# Bài 6: Bảng cửu chương mini
for i in range(2, 6):
    for j in range(1, 11):
        print(str(i) + " x " + str(j) + " = " + str(i * j))

# Bài 7: Kiểm tra số nguyên tố
n = 17
is_prime = True
if n < 2:
    is_prime = False
for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break
if is_prime:
    print(str(n) + " la so nguyen to")
else:
    print(str(n) + " khong phai so nguyen to")

# Bài 8: Đếm số lần xuất hiện
orders = ["A", "B", "A", "C", "A"]
count_a = 0
for order in orders:
    if order == "A":
        count_a += 1
print(f"A xuất hiện: {count_a} lần")

# Bài 9: Hàm tính tổng tiền
def calculate_total(price, quantity):
    total = price * quantity
    return total
 
price = 100000
quantity = 3
result = calculate_total(price, quantity)
print(f"Tổng tiền: {result} VND")

# Bài 10: Hàm kiểm tra đăng nhập
def check_login(is_logged_in):
    if is_logged_in == True:
        return "Da dang nhap"
    else:
        return "Chua dang nhap"
is_logged_in = True
print(check_login(is_logged_in))

# Bài 11: Hàm giảm giá
def apply_discount(price, percent):
    giam_gia = int(price * (percent / 100))
    gia_moi = price - giam_gia
    return gia_moi

gia_hien_tai = 200000
gia_sau_giam = apply_discount(gia_hien_tai, 20)
print(f"Giá hiện tại: {gia_hien_tai} VND")
print(f"Giá sau khi giảm: {gia_sau_giam} VND")

# Bài 12: Hàm free ship
def is_free_shipping(order_value):
    if order_value >= 500000:
        return True
    else:
        return False
free_ship = is_free_shipping(600000)
if free_ship:
    print("Đơn hàng được miễn phí vận chuyển")
else:
    print("Đơn hàng không được miễn phí vận chuyển")


# Bài 13: Phân loại khách hàng
def classify_customer(total_spent):
    if total_spent >= 1000000:
        return "VIP"
    elif total_spent >= 500000:
        return "Gold"
    else:
        return "Normal"
print(classify_customer(1200000))
print(classify_customer(600000))
print(classify_customer(300000))

# Bài 14: Validate email
def is_valid_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False
email = "test@gmail.com"
result = is_valid_email(email)
if result:
    print("Email hop le")

# Bài 15: Tổng doanh thu
def total_revenue(orders):
    total = 0
    for order in orders:
        total += order
    return total
 
orders = [100000, 200000, 300000]
print(f"Tổng doanh thu: {total_revenue(orders)} VND")

# Bài 16: Lọc giá cao
def filter_prices(prices):
    result = []
    for price in prices:
        if price > 300000:
            result.append(price)
    return result
 
print(f"Danh sách giá cao (VND): {filter_prices([100000, 500000, 700000, 200000])}")

# Bài 17: Đếm đơn hợp lệ
def check_orders(orders):
    valid_count = 0
    for order in orders:
        if order > 0:
            valid_count += 1
    return valid_count
print(check_orders([100000, 0, 200000, -50000]))

# Bài 18: Tổng sau giảm giá
def total_after_discount(prices):
    total = 0
    for price in prices:
        total = int(total + price - (price * 0.1))
    return total
 
prices = [100000, 200000, 300000]
print(f"Tổng sau giảm giá: {total_after_discount(prices)} VND")

# Bài 19: Lọc khách VIP
def vip_checker(cart):
    vip = True
    for i in cart:
        if i < 3000000:
            vip = False
    return vip
cart = [200000, 1500000, 800000]
customer = vip_checker(cart)
if customer == True:
    print("Khách này VIP")
else:
    print("Khách chưa VIP")

# Bài 20: Hệ thống thanh toán (mini backend)
def checkout(cart, balance):
    total = 0
    for item in cart:
        total += item
 
    if balance >= total:
        remaining_balance = balance - total
        return {"status": "Thanh toán thành công", "Số dư còn lại": remaining_balance}
    else:
        return {"status": "Không đủ tiền", "Số dư còn lại": balance}
 
cart = [100000, 200000, 150000]
balance = 500000
print(checkout(cart, balance))







