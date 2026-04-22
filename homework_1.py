# ===== HOMEWORK 1 - PYTHON BUỔI 1 =====
# Chủ đề: Biến(Variables), Toán tử (Operators), Câu lệnh điều kiện (if/elif/else)
# Họ tên: [Trần Thị Thủy Tiên]_BrSE AI
# Ngày: 22/04/2026
# =======================================

# Bài 1: Tính tổng tiền đơn hàng
price = 120000
quantity = 3
total_amount = price * quantity
print("Tổng tiền đơn hàng:", total_amount, "VND")

# Bài 2: Áp dụng giảm giá sản phẩm
price = 500000
discount_percent = 10
discount_amount = price * discount_percent / 100
final_price = price - discount_amount
print("Số tiền được giảm:", discount_amount, "VND")
print("Giá cuối cùng:", final_price, "VND")

# Bài 3: Tính lương nhân viên
salary_per_day = 300000
working_days = 22
monthly_salary = salary_per_day * working_days
print("Tổng lương tháng:", monthly_salary, "VND")

# Bài 4: Tính phí vận chuyển
distance_km = 12
cost_per_km = 5000
shipping_cost = distance_km * cost_per_km
print("Tổng phí vận chuyển:", shipping_cost, "VND")

# Bài 5: Kiểm tra dung lượng lưu trữ
total_storage = 256
used_storage = 180
available_storage = total_storage - used_storage
print("Dung lượng còn lại:", available_storage, "GB")

# Bài 6: Kiểm tra khả năng thanh toán
balance = 200000
item_price = 150000
if balance >= item_price:
    remaining_balance = balance - item_price
    print("Thanh toán thành công. Số dư còn lại:", remaining_balance, "VND") 
else:
    shortage = item_price - balance
    print("Bạn không đủ tiền trong tài khoản. Còn thiếu:", shortage, "VND")

# Bài 7: Điều kiện miễn phí vận chuyển
order_value = 250000
if order_value >= 200000:
    print("Đơn hàng được miễn phí vận chuyển")
else:
    print("Đơn hàng không được miễn phí vận chuyển")

# Bài 8: Phân quyền người dùng
is_logged_in = True
is_admin = False
if is_logged_in and is_admin:
    print("Người dùng có quyền admin")
else:
    print("Người dùng không có quyền admin")

# Bài 9: Kiểm tra giờ làm việc
hour = 14
if hour >= 9 and hour <= 18:
    print("Đang trong giờ làm việc")
else:
    print("Ngoài giờ làm việc")

# Bài 10: Kiểm tra email hợp lệ (cơ bản)
email = "user@gmail.com"
if "@" in email and "." in email:
    print("Email hợp lệ")
else:
    print("Email không hợp lệ")

# Bài 11: Tính phí vận chuyển theo giá trị đơn
order_value = 180000
total = order_value
if order_value >= 200000:
    shipping = 0
else:
    shipping = 30000
total = order_value + shipping
print("Tổng số tiền phải trả:", total, "VND")
print("Phí ship:", shipping, "VND")

#Bài 12: Tính thưởng nhân viên
performance_score = 8.2
if performance_score >= 9:
    bonus = 5000000
elif performance_score >= 7:
    bonus = 2000000
else:
    bonus = 0
print("Thưởng:", bonus, "VND")

# Bài 13: Mapping trạng thái đơn hàng
status_code = 2
if status_code == 1:
    print("Trạng thái:", "Pending")
elif status_code == 2:
    print("Trạng thái:", "Shipping")
elif status_code == 3:
    print("Trạng thái:", "Delivered")
else:
    print("Trạng thái:", "Unknown")

# Bài 14: Tính giá vé theo độ tuổi
age = 15
if age < 12:
    ticket_price = 50000
elif age <= 17:
    ticket_price = 70000
else:
    ticket_price = 100000
print("Giá vé:", ticket_price, "VND")

# Bài 15: Phân loại khách hàng
total_spent = 1200000
if total_spent >= 1000000:
    print("Loại khách hàng:", "VIP")
elif total_spent >= 500000:
    print("Loại khách hàng:", "Gold")
else:
    print("Loại khách hàng:", "Normal")

# Bài 16: Tính tiền điện theo bậc
kwh = 135
total_bill = 0
 
if kwh <= 50:
    total_bill = kwh * 1678
elif kwh <= 100:
    total_bill = 50 * 1678 + (kwh - 50) * 1734
else:
    total_bill = 50 * 1678 + 50 * 1734 + (kwh - 100) * 2014
 
print("Tiền điện:", total_bill, "VND")

# Bài 17: Tính lương có thưởng KPI
base_salary = 10000000
kpi = 0.85
if kpi >= 0.9:
    bonus = base_salary * 0.30
elif kpi >= 0.8:
    bonus = base_salary * 0.10
else:
    bonus = 0
total_salary = base_salary + bonus
print("Lương cơ bản:", base_salary, "VND")
print("Thưởng KPI:", bonus, "VND")
print("Tổng lương:", total_salary, "VND")

# Bài 18: Tính giá taxi
distance = 12
taxi_fare = 0
 
if distance <= 1:
    taxi_fare = 15000
elif distance <= 10:
    taxi_fare = 15000 + (distance - 1) * 12000
else:
    taxi_fare = 15000 + 9 * 12000 + (distance - 10) * 10000
 
print("Giá taxi:", taxi_fare, "VND")

# Bài 19: Kiểm tra điều kiện vay
income = 15000000
debt = 3000000
if income >= 10000000 and debt <= income * 0.5:
    print("Đủ điều kiện vay")
else:
    print("Không đủ điều kiện vay")

# Bài 20: Áp dụng nhiều điều kiện giảm giá
price = 1000000
is_member = True
voucher = 100000
if is_member:
    price = price - price * 0.10
price = price - voucher
print("Giá cuối cùng:", price, "VND")