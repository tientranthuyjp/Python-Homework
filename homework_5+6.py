# ===== HOMEWORK 5+6 - PYTHON BUỔI 5+6 =====
# Chủ đề: Lập trình hướng đối tượng OOP + Lập trình hướng đối tượng-OOP Nâng Cao

# Python - Bài 5 & 6: Thiết Kế & Xây Dựng Class cho Hệ Thống Thương Mại Điện Tử
# PHẦN I: CÂU HỎI LÝ THUYẾT (9 CÂU HỎI)
# PHẦN II: CÂU HỎI THỰC HÀNH (5 BÀI)
# (Tạo class cho hệ thống thương mại điện tử - E-Commerce System)

# Họ tên: [Trần Thị Thủy Tiên]_BrSE AI
# Ngày: 28/04 + 05/05 - 19/05/2026
# =======================================

### =====================================
# PHẦN I: CÂU HỎI LÝ THUYẾT (9 CÂU HỎI)
### =====================================

### =====================================
# Câu 1: Phân biệt giữa Class và Object
### =====================================
# Class là bản thiết kế (blueprint/template) dùng để tạo ra các object.
# Nó định nghĩa: thuộc tính (attributes) và hành vi (methods).

# Object là thực thể thực tế được tạo ra từ Class, có dữ liệu cụ thể.

# So sánh nhanh:

# | Tiêu chí       | Class                    | Object                     |
# |----------------|--------------------------|----------------------------|
# | Là gì          | Bản thiết kế             | Thực thể cụ thể            |
# | Dữ liệu        | Chưa có dữ liệu thật     | Có dữ liệu thực tế         |
# | Tạo ra         | Lập trình viên định nghĩa| Được tạo từ Class          |
# | Ví dụ          | Class Product            | Laptop, iPhone, Mouse      |

# Ví dụ trong hệ thống thương mại điện tử:

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Object cụ thể:
product1 = Product("Laptop Asus", 20000000)
product2 = Product("iPhone 14", 25000000)
product3 = Product("Tai nghe Bluetooth", 1000000)

print("=== Câu 1: Class vs Object ===")
print("Class Product tạo ra các object:")
print("-", product1.name, "-", product1.price, "VND")
print("-", product2.name, "-", product2.price, "VND")
print("-", product3.name, "-", product3.price, "VND")

# Output:
# === Câu 1: Class vs Object ===
# Class Product tạo ra các object:
# - Laptop Asus - 20000000 VND
# - iPhone 14 - 25000000 VND
# - Tai nghe Bluetooth - 1000000 VND


### ================================================
# Câu 2: Tác dụng của hàm __init__() và tham số self
### ================================================

# Hàm __init__() là hàm khởi tạo trong Python.
# Hàm này tự động chạy ngay khi tạo object.
# Dùng để gán giá trị ban đầu cho các thuộc tính của object.

# self là tham số đại diện cho chính object đó.
# self luôn là tham số đầu tiên vì Python cần biết
# method đang làm việc với object nào.

# Ví dụ với class Product:

class Product:

    def __init__(self, product_id, name, price, quantity, category):
        # self ở đây đại diện cho object đang được tạo
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    def show_info(self):
        print("ID:", self.product_id)
        print("Tên:", self.name)
        print("Giá:", self.price, "VND")
        print("Tồn kho:", self.quantity)
        print("Danh mục:", self.category)


product1 = Product(1, "Laptop Asus", 20000000, 10, "Electronics")

print("=== Câu 2: __init__ và self ===")
product1.show_info()

# Output:
# === Câu 2: __init__ và self ===
# ID: 1
# Tên: Laptop Asus
# Giá: 20000000 VND
# Tồn kho: 10
# Danh mục: Electronics


### ===================================================
# Câu 3: Các loại thuộc tính và phương thức trong Class
### ===================================================

# Trong Python có 3 loại phương thức chính:

# 1. Instance Method
#    - Làm việc với object cụ thể
#    - Tham số đầu tiên luôn là self
#    - Dùng khi thao tác phụ thuộc dữ liệu của từng object

# 2. Class Method (@classmethod)
#    - Làm việc với class thay vì object
#    - Dùng decorator @classmethod
#    - Tham số đầu tiên là cls (class)
#    - Dùng khi thao tác với biến dùng chung cho toàn class

# 3. Static Method (@staticmethod)
#    - Không dùng self hoặc cls
#    - Dùng decorator @staticmethod
#    - Giống hàm bình thường nhưng đặt trong class
#    - Dùng khi không cần truy cập object hay class

# Ví dụ với class Order:

class Order:

    # Class Variable (biến dùng chung cho tất cả Order)
    shop_name = "FPT Shop"

    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    # Instance Method: làm việc với từng order cụ thể
    def show_order(self):
        print("Sản phẩm:", self.product_name)
        print("Giá:", self.price, "VND")

    # Class Method: làm việc với class
    @classmethod
    def show_shop(cls):
        print("Cửa hàng:", cls.shop_name)

    # Static Method: hàm hỗ trợ không cần self/cls
    @staticmethod
    def thank_you():
        print("Cảm ơn bạn đã đặt hàng!")


order1 = Order("Laptop Asus", 20000000)
order2 = Order("iPhone 14", 25000000)

print("=== Câu 3: 3 loại phương thức ===")

order1.show_order()
print()

Order.show_shop()
print()

Order.thank_you()

# Output:
# === Câu 3: 3 loại phương thức ===
# Sản phẩm: Laptop Asus
# Giá: 20000000 VND
# Cửa hàng: FPT Shop
# Cảm ơn bạn đã đặt hàng!


### ======================================================
# Câu 4: Tính đóng gói (Encapsulation) và access modifiers
### ======================================================

# Python không có access modifiers như Java/C++,
# nhưng dùng dấu gạch dưới để quy ước mức truy cập.

# 3 mức độ:

# 1. Public (không có dấu _)
#    - Truy cập ở mọi nơi
#    Ví dụ: self.name

# 2. Protected (có 1 dấu _)
#    - Nên chỉ dùng trong class hoặc class con kế thừa
#    Ví dụ: self._email

# 3. Private (có 2 dấu __)
#    - Hạn chế truy cập trực tiếp từ bên ngoài
#    Ví dụ: self.__password

# Vì sao cần Getter/Setter?
# Getter: lấy dữ liệu private một cách an toàn
# Setter: thay đổi dữ liệu private có kiểm tra điều kiện

class User:

    def __init__(self, username, password):
        self.username = username           # Public
        self._email = "user@gmail.com"    # Protected
        self.__password = password         # Private

    # Getter: lấy password
    def get_password(self):
        return self.__password

    # Setter: đổi password
    def set_password(self, new_password):
        if len(new_password) >= 6:
            self.__password = new_password
        else:
            print("Mật khẩu phải có ít nhất 6 ký tự")


user1 = User("Tien", "123456")

print("=== Câu 4: Encapsulation ===")
print("Username:", user1.username)
print("Password cũ:", user1.get_password())

user1.set_password("newpass999")
print("Password mới:", user1.get_password())

# Thử truy cập trực tiếp -> sẽ báo lỗi (nên comment lại)
# print(user1.__password)  # AttributeError

# Output:
# === Câu 4: Encapsulation ===
# Username: Tien
# Password cũ: 123456
# Password mới: newpass999


### ================================================
# Câu 5: Kế thừa (Inheritance) và ghi đè phương thức
### ================================================

# Kế thừa (Inheritance) cho phép class con dùng lại
# thuộc tính và phương thức của class cha.

# Cú pháp: class ClassName(ParentClass)

# Ghi đè (Override): class con viết lại method
# cùng tên với method của class cha.

# Lưu ý: Override phải cùng tên method với class cha.
# Nếu khác tên thì không phải Override, chỉ là method mới.

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print("Tên:", self.name)
        print("Tuổi:", self.age)


class Customer(Person):

    def __init__(self, name, age, customer_id):
        super().__init__(name, age)  # Gọi __init__ của Person
        self.customer_id = customer_id

    # Override phương thức show_info() của Person
    def show_info(self):
        print("=== Khách hàng ===")
        print("ID:", self.customer_id)
        print("Tên:", self.name)
        print("Tuổi:", self.age)


print("=== Câu 5: Inheritance và Override ===")

person1 = Person("Huy", 33)
print("--- Person ---")
person1.show_info()

print()

customer1 = Customer("Tien", 40, "KH001")
print("--- Customer ---")
customer1.show_info()

# Output:
# === Câu 5: Inheritance và Override ===
# --- Person ---
# Tên: Huy
# Tuổi: 33
#
# --- Customer ---
# === Khách hàng ===
# ID: KH001
# Tên: Tien
# Tuổi: 40


### ===================================================
# Câu 6: Scope (Phạm vi hoạt động) của biến trong class
### ===================================================

# Scope là phạm vi hoạt động của biến trong Python.

# Có 4 loại biến:

# 1. Global Variable (Biến toàn cục)
#    - Khai báo bên ngoài class/hàm
#    - Dùng được ở nhiều nơi trong chương trình

# 2. Local Variable (Biến cục bộ)
#    - Khai báo trong method/hàm
#    - Chỉ dùng được trong method/hàm đó

# 3. Instance Variable (Biến instance)
#    - Thuộc về từng object
#    - Dùng self để truy cập

# 4. Class Variable (Biến class)
#    - Thuộc về class
#    - Dùng chung cho tất cả object

# Biến Global
shop_name = "FPT Shop"

class ShoppingCart:

    # Class Variable
    max_items = 10

    def __init__(self, owner):
        # Instance Variable
        self.owner = owner
        self.items = []

    def add_item(self, product_name, price):
        # Local Variable
        item_info = product_name + " - " + str(price) + " VND"
        self.items.append(item_info)

    def show_cart(self):
        # Dùng Global Variable
        print("Cửa hàng:", shop_name)
        # Dùng Class Variable
        print("Giới hạn giỏ hàng:", ShoppingCart.max_items, "sản phẩm")
        # Dùng Instance Variable
        print("Chủ giỏ hàng:", self.owner)
        print("Sản phẩm trong giỏ:")
        for item in self.items:
            print(" -", item)

cart1 = ShoppingCart("Tien")
cart1.add_item("Laptop", 20000000)
cart1.add_item("Mouse", 500000)

print("=== Câu 6: Scope của biến ===")
cart1.show_cart()

# Output:
# === Câu 6: Scope của biến ===
# Cửa hàng: FPT Shop
# Giới hạn giỏ hàng: 10 sản phẩm
# Chủ giỏ hàng: Tien
# Sản phẩm trong giỏ:
#  - Laptop - 20000000 VND
#  - Mouse - 500000 VND


### ==================================================
# Câu 7: Nguyên lý POLYMORPHISM và ABSTRACTION của OOP
### ==================================================

# 1. POLYMORPHISM (Tính đa hình)

# Polymorphism: cùng một method nhưng mỗi class
# có cách hoạt động riêng.

# Ưu điểm:
# - Code linh hoạt, dễ mở rộng
# - Có thể gọi cùng một method trên nhiều object khác nhau
# - Dễ quản lý nhiều loại object trong cùng một danh sách

# Ví dụ: method move() trong Dog, Cat, Bird:

class Animal:
    def move(self):
        print("Animal is moving")


class Dog(Animal):
    def move(self):
        print("Dog is running")


class Cat(Animal):
    def move(self):
        print("Cat is walking")


class Bird(Animal):
    def move(self):
        print("Bird is flying")


print("=== Câu 7: Polymorphism ===")

animals = [Dog(), Cat(), Bird()]
for animal in animals:
    animal.move()

# Output:
# === Câu 7: Polymorphism ===
# Dog is running
# Cat is walking
# Bird is flying


# 2. ABSTRACTION (Tính trừu tượng)

# Abstraction: ẩn đi các chi tiết phức tạp bên trong,
# chỉ cung cấp interface (giao diện) đơn giản cho người dùng.

# Khác với Encapsulation:
# - Encapsulation: bảo vệ dữ liệu, kiểm soát truy cập
# - Abstraction: ẩn cách hoạt động, chỉ hiện cái cần dùng

# Ví dụ: class Shape với abstract method area()

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass  # Class con bắt buộc phải tự định nghĩa


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


print("=== Câu 7: Abstraction ===")

rectangle1 = Rectangle(5, 4)
circle1 = Circle(3)

print("Diện tích hình chữ nhật:", rectangle1.area())
print("Diện tích hình tròn:", circle1.area())

# Output:
# === Câu 7: Abstraction ===
# Diện tích hình chữ nhật: 20
# Diện tích hình tròn: 28.26


### =====================================================================
# Câu 8: Schema (Sơ đồ thiết kế class) - Cách lập kế hoạch xây dựng class
### ===================================================================

# Schema trong OOP là sơ đồ thiết kế class trước khi viết code.

# Schema giúp:
# - Hình dung được chương trình trước khi code
# - Tránh thiếu chức năng khi viết
# - Dễ làm việc nhóm hơn

# Các bước cần làm trước khi code:

# Bước 1: Xác định attributes (thuộc tính)
# Bước 2: Xác định methods (phương thức)
# Bước 3: Xác định mối quan hệ giữa các class
# Bước 4: Xác định public/private/protected

# Schema cho PaymentProcessor:

#  PaymentProcessor (class cha)
#  ├── Attributes: payment_name, amount
#  ├── Methods: pay(), show_info()
#  │
#  ├── CreditCardPayment (class con)
#  │   ├── Attributes: card_number
#  │   └── Methods: pay() -> override
#  │
#  ├── BankTransferPayment (class con)
#  │   ├── Attributes: bank_account
#  │   └── Methods: pay() -> override
#  │
#  └── EWalletPayment (class con)
#      ├── Attributes: wallet_id
#      └── Methods: pay() -> override

# Ví dụ code:

class PaymentProcessor:

    def __init__(self, payment_name, amount):
        self.payment_name = payment_name   # Public
        self.amount = amount               # Public

    def pay(self):
        print("Đang xử lý thanh toán:", self.amount, "VND")

    def show_info(self):
        print("Phương thức:", self.payment_name)
        print("Số tiền:", self.amount, "VND")


class CreditCardPayment(PaymentProcessor):

    def __init__(self, amount, card_number):
        super().__init__("Thẻ tín dụng", amount)
        self.card_number = card_number

    def pay(self):
        print("Thanh toán bằng thẻ tín dụng:", self.card_number)
        print("Số tiền:", self.amount, "VND")


class BankTransferPayment(PaymentProcessor):

    def __init__(self, amount, bank_account):
        super().__init__("Chuyển khoản", amount)
        self.bank_account = bank_account

    def pay(self):
        print("Thanh toán bằng chuyển khoản:", self.bank_account)
        print("Số tiền:", self.amount, "VND")


class EWalletPayment(PaymentProcessor):

    def __init__(self, amount, wallet_id):
        super().__init__("Ví điện tử", amount)
        self.wallet_id = wallet_id

    def pay(self):
        print("Thanh toán bằng ví điện tử:", self.wallet_id)
        print("Số tiền:", self.amount, "VND")


print("=== Câu 8: Schema - PaymentProcessor ===")

credit = CreditCardPayment(1000000, "1234-5678")
bank = BankTransferPayment(2000000, "0123456789")
wallet = EWalletPayment(500000, "MOMO_001")

credit.pay()
print()
bank.pay()
print()
wallet.pay()

# Output:
# === Câu 8: Schema - PaymentProcessor ===
# Thanh toán bằng thẻ tín dụng: 1234-5678
# Số tiền: 1000000 VND
#
# Thanh toán bằng chuyển khoản: 0123456789
# Số tiền: 2000000 VND
#
# Thanh toán bằng ví điện tử: MOMO_001
# Số tiền: 500000 VND


### ======================================================
# Câu 9: Cách vẽ sơ đồ tư duy (Mind Map) để thiết kế class
### ====================================================

# Mind Map là sơ đồ tư duy giúp lên kế hoạch trước khi code.

# Lợi ích của Mind Map:
# - Hình dung toàn bộ class trước khi code
# - Biết cần tạo thuộc tính và phương thức gì
# - Dễ quản lý mối quan hệ giữa các class
# - Tránh thiếu chức năng khi lập trình

# Các thành phần trong Mind Map:
# - Tên class ở trung tâm
# - Nhánh Attributes: tên, kiểu dữ liệu, access level
# - Nhánh Methods: tên, chức năng
# - Nhánh Relationship: class liên kết

# Mind Map cho class InventoryManager:

#                    InventoryManager
#                          │
#    ┌─────────────────────┼──────────────────────┐
#    │                     │                      │
# Attributes            Methods              Relationship
#    │                     │                      │
# - product_name        - add_product()       - Product
# - quantity            - remove_product()    - Supplier
# - price               - update_stock()
# - _supplier (prot)    - show_inventory()
# - __password (priv)

class InventoryManager:

    def __init__(self, manager_name):
        self.manager_name = manager_name     # Public
        self._supplier = "Supplier ABC"      # Protected
        self.__password = "admin123"         # Private
        self.products = []

    def add_product(self, product_name, quantity, price):
        product = {
            "name": product_name,
            "quantity": quantity,
            "price": price
        }
        self.products.append(product)
        print("Đã thêm sản phẩm:", product_name)

    def remove_product(self, product_name):
        for p in self.products:
            if p["name"] == product_name:
                self.products.remove(p)
                print("Đã xóa sản phẩm:", product_name)
                return
        print("Không tìm thấy:", product_name)

    def update_stock(self, product_name, new_quantity):
        for p in self.products:
            if p["name"] == product_name:
                p["quantity"] = new_quantity
                print("Cập nhật kho:", product_name, "->", new_quantity)
                return

    def show_inventory(self):
        print("=== Kho hàng ===")
        print("Quản lý:", self.manager_name)
        for p in self.products:
            print("-", p["name"], "| Số lượng:", p["quantity"], "| Giá:", p["price"], "VND")


print("=== Câu 9: Mind Map - InventoryManager ===")

inventory = InventoryManager("Tien")
inventory.add_product("Laptop", 10, 20000000)
inventory.add_product("Mouse", 30, 500000)
inventory.update_stock("Mouse", 30)
inventory.show_inventory()

# Output:
# === Câu 9: Mind Map - InventoryManager ===
# Đã thêm sản phẩm: Laptop
# Đã thêm sản phẩm: Mouse
# Cập nhật kho: Mouse -> 30
# === Kho hàng ===
# Quản lý: Tien
# - Laptop | Số lượng: 10 | Giá: 20000000 VND
# - Mouse | Số lượng: 30 | Giá: 500000 VND


### =============================================================
# PHẦN I: II: CÂU HỎI THỰC HÀNH (5 BÀI)
# (Tạo class cho hệ thống thương mại điện tử - E-Commerce System)
### =============================================================


### =====================================
# Bài tập 1: Xây dựng class Product
### =====================================

# Yêu cầu:
# - Thuộc tính: product_id, name, price, quantity, category
# - apply_discount(discount_percent): trả về giá sau giảm
# - is_in_stock(): kiểm tra còn hàng hay không
# - Chạy với 2-3 sản phẩm khác nhau

class Product:
    """Class đại diện cho một sản phẩm trong hệ thống."""

    def __init__(self, product_id, name, price, quantity, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    def apply_discount(self, discount_percent):
        """Giảm giá sản phẩm theo phần trăm, trả về giá sau giảm."""
        if discount_percent < 0 or discount_percent > 100:
            print("Phần trăm giảm giá không hợp lệ")
            return self.price
        return self.price - (self.price * discount_percent / 100)

    def is_in_stock(self):
        """Kiểm tra sản phẩm còn trong kho hay không."""
        return self.quantity > 0


product1 = Product(1, "Laptop Asus", 20000000, 5, "Electronics")
product2 = Product(2, "Mouse Logitech", 500000, 0, "Accessories")
product3 = Product(3, "Bàn phím cơ", 1200000, 3, "Accessories")

print("=== Bài tập 1: Class Product ===")

print("--- Sản phẩm 1 ---")
print("Tên:", product1.name)
print("Giá gốc:", product1.price, "VND")
print("Giá sau giảm 10%:", product1.apply_discount(10), "VND")
print("Còn hàng:", product1.is_in_stock())

print()

print("--- Sản phẩm 2 ---")
print("Tên:", product2.name)
print("Giá gốc:", product2.price, "VND")
print("Giá sau giảm 5%:", product2.apply_discount(5), "VND")
print("Còn hàng:", product2.is_in_stock())

print()

print("--- Sản phẩm 3 ---")
print("Tên:", product3.name)
print("Giá gốc:", product3.price, "VND")
print("Giá sau giảm 15%:", product3.apply_discount(15), "VND")
print("Còn hàng:", product3.is_in_stock())

# Output:
# === Bài tập 1: Class Product ===
# --- Sản phẩm 1 ---
# Tên: Laptop Asus
# Giá gốc: 20000000 VND
# Giá sau giảm 10%: 18000000.0 VND
# Còn hàng: True
#
# --- Sản phẩm 2 ---
# Tên: Mouse Logitech
# Giá gốc: 500000 VND
# Giá sau giảm 5%: 475000.0 VND
# Còn hàng: False
#
# --- Sản phẩm 3 ---
# Tên: Bàn phím cơ
# Giá gốc: 1200000 VND
# Giá sau giảm 15%: 1020000.0 VND
# Còn hàng: True

### ==========================================================
# Bài tập 2: Xây dựng class Customer với Encapsulationt
### ==========================================================

# Yêu cầu:
# - Public: customer_id, name
# - Protected: _email
# - Private: __password, __credit_balance
# - Getter/Setter cho __credit_balance (setter: chỉ cho phép >= 0)
# - add_credit(amount): nạp tiền
# - use_credit(amount): dùng tiền (kiểm tra đủ số dư)
# - Kiểm tra không thể truy cập trực tiếp __password từ bên ngoài

class Customer:
    """Class đại diện cho khách hàng trong hệ thống."""

    def __init__(self, customer_id, name, email, password, credit_balance):
        self.customer_id = customer_id       # Public
        self.name = name                     # Public
        self._email = email                  # Protected
        self.__password = password           # Private
        self.__credit_balance = credit_balance  # Private

    # Getter: lấy số dư
    def get_credit_balance(self):
        return self.__credit_balance

    # Setter: cập nhật số dư (chỉ cho phép >= 0)
    def set_credit_balance(self, amount):
        if amount >= 0:
            self.__credit_balance = amount
        else:
            print("Số dư không được âm")

    def add_credit(self, amount):
        """Nạp tiền vào tài khoản."""
        if amount > 0:
            self.__credit_balance += amount
            print("Nạp thành công:", amount, "VND")
        else:
            print("Số tiền nạp phải lớn hơn 0")

    def use_credit(self, amount):
        """Dùng tiền từ tài khoản."""
        if amount <= self.__credit_balance:
            self.__credit_balance -= amount
            print("Thanh toán thành công:", amount, "VND")
        else:
            print("Số dư không đủ. Hiện có:", self.__credit_balance, "VND")


customer1 = Customer(
    1,
    "Tien",
    "tien@gmail.com",
    "123456",
    500000
)

print("=== Bài tập 2: Class Customer - Encapsulation ===")

print("Tên:", customer1.name)
print("Số dư ban đầu:", customer1.get_credit_balance(), "VND")

customer1.add_credit(300000)
print("Sau khi nạp 300,000 VND:", customer1.get_credit_balance(), "VND")

customer1.use_credit(200000)
print("Sau khi thanh toán 200,000 VND:", customer1.get_credit_balance(), "VND")

customer1.use_credit(1000000)

# Thử truy cập trực tiếp -> sẽ báo lỗi (đã comment lại)
# print(customer1.__password)  # AttributeError: 'Customer' object has no attribute '__password'

# Output:
# === Bài tập 2: Class Customer - Encapsulation ===
# Tên: Tien
# Số dư ban đầu: 500000 VND
# Nạp thành công: 300000 VND
# Sau khi nạp 300,000 VND: 800000 VND
# Thanh toán thành công: 200000 VND
# Sau khi thanh toán 200,000 VND: 600000 VND
# Số dư không đủ. Hiện có: 600000 VND


### ==========================================================
# Bài tập 3: Xây dựng class Order và tính tổng tiền
### ==========================================================

# Yêu cầu:
# - Thuộc tính: order_id, customer, order_date, items, quantities
# - add_item(product, quantity): thêm sản phẩm vào đơn
# - calculate_total(): tính tổng tiền
# - apply_discount(discount_percent): giảm giá cho toàn đơn
# - Tạo 2-3 đơn hàng và kiểm tra tính tổng tiền

class Product:

    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class Customer:

    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name


class Order:
    """Class đại diện cho một đơn hàng."""

    def __init__(self, order_id, customer, order_date):
        self.order_id = order_id
        self.customer = customer
        self.order_date = order_date
        self.items = []           # Danh sách sản phẩm
        self.quantities = []      # Danh sách số lượng tương ứng

    def add_item(self, product, quantity):
        """Thêm sản phẩm vào đơn hàng."""
        if quantity > 0:
            self.items.append(product)
            self.quantities.append(quantity)
        else:
            print("Số lượng phải lớn hơn 0")

    def calculate_total(self):
        """Tính tổng tiền đơn hàng."""
        total = 0
        for i in range(len(self.items)):
            total += self.items[i].price * self.quantities[i]
        return total

    def apply_discount(self, discount_percent):
        """Áp dụng mã giảm giá cho toàn bộ đơn hàng."""
        total = self.calculate_total()
        return total - (total * discount_percent / 100)


p1 = Product(1, "Laptop Asus", 20000000)
p2 = Product(2, "Mouse Logitech", 500000)
p3 = Product(3, "Bàn phím cơ", 1200000)

c1 = Customer(1, "Tien")
c2 = Customer(2, "Huy")

order1 = Order(101, c1, "2026-05-14")
order1.add_item(p1, 1)
order1.add_item(p2, 2)

order2 = Order(102, c2, "2026-05-15")
order2.add_item(p2, 3)
order2.add_item(p3, 1)

print("=== Bài tập 3: Class Order ===")

print("--- Đơn hàng 1 ---")
print("Khách hàng:", order1.customer.name)
print("Tổng tiền:", order1.calculate_total(), "VND")
print("Sau giảm 10%:", order1.apply_discount(10), "VND")

print()

print("--- Đơn hàng 2 ---")
print("Khách hàng:", order2.customer.name)
print("Tổng tiền:", order2.calculate_total(), "VND")
print("Sau giảm 5%:", order2.apply_discount(5), "VND")

# Output:
# === Bài tập 3: Class Order ===
# --- Đơn hàng 1 ---
# Khách hàng: Tien
# Tổng tiền: 21000000 VND
# Sau giảm 10%: 18900000.0 VND
#
# --- Đơn hàng 2 ---
# Khách hàng: Huy
# Tổng tiền: 2700000 VND
# Sau giảm 5%: 2565000.0 VND


### ==========================================================
# Bài tập 4: Kế thừa - Tạo class SpecialCustomer từ Customer
### ==========================================================

# Yêu cầu:
# - Kế thừa từ Customer
# - Thêm: loyalty_points, loyalty_level (Bronze/Silver/Gold)
# - Override __init__() dùng super()
# - add_loyalty_points(points): tích lũy điểm
# - get_discount(): trả về % giảm giá theo level (Bronze 5%, Silver 10%, Gold 15%)
# - __str__(): in thông tin khác với Customer thường

class Customer:

    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

    def __str__(self):
        return f"Khách hàng: {self.name} (ID: {self.customer_id})"


class SpecialCustomer(Customer):
    """Class khách hàng VIP kế thừa từ Customer."""

    def __init__(self, customer_id, name, loyalty_points, loyalty_level):
        super().__init__(customer_id, name)
        self.loyalty_points = loyalty_points
        self.loyalty_level = loyalty_level

    def add_loyalty_points(self, points):
        """Tích lũy điểm thành viên."""
        if points > 0:
            self.loyalty_points += points
            print("Tích thêm", points, "điểm. Tổng điểm:", self.loyalty_points)

    def get_discount(self):
        """Trả về % giảm giá theo loyalty_level."""
        if self.loyalty_level == "Bronze":
            return 5
        elif self.loyalty_level == "Silver":
            return 10
        elif self.loyalty_level == "Gold":
            return 15
        else:
            return 0

    def __str__(self):
        return f"Khách VIP: {self.name} | Level: {self.loyalty_level} | Điểm: {self.loyalty_points}"


print("=== Bài tập 4: Class SpecialCustomer (Inheritance) ===")

customer1 = SpecialCustomer(1, "Tien", 100, "Gold")
print(customer1)

customer1.add_loyalty_points(50)
print("Mức giảm giá:", customer1.get_discount(), "%")

print()

customer2 = SpecialCustomer(2, "Huy", 30, "Silver")
print(customer2)

customer2.add_loyalty_points(20)
print("Mức giảm giá:", customer2.get_discount(), "%")

# Output:
# === Bài tập 4: Class SpecialCustomer (Inheritance) ===
# Khách VIP: Tien | Level: Gold | Điểm: 100
# Tích thêm 50 điểm. Tổng điểm: 150
# Mức giảm giá: 15 %
#
# Khách VIP: Huy | Level: Silver | Điểm: 30
# Tích thêm 20 điểm. Tổng điểm: 50
# Mức giảm giá: 10 %



### =================================================================
# Bài tập 5: Polymorphism - Tạo class cho các loại sản phẩm khác nhau
### =================================================================

# Yêu cầu:
# 3 class kế thừa từ Product:
# 1. PhysicalProduct: thêm weight, shipping_fee
#    -> calculate_final_price() = giá + shipping_fee
# 2. DigitalProduct: thêm file_size, license_type
#    -> calculate_final_price() = nếu one-time thì giảm 20%, không thì giá gốc
# 3. ServiceProduct: thêm duration_days, renewal_fee
#    -> calculate_final_price() = giá + renewal_fee
# - Tạo danh sách hỗn hợp, duyệt và in giá cuối cùng

class Product:
    """Class cha cho tất cả loại sản phẩm."""

    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def calculate_final_price(self):
        return self.price


class PhysicalProduct(Product):
    """Sản phẩm vật lý: có trọng lượng và phí vận chuyển."""

    def __init__(self, product_id, name, price, weight, shipping_fee):
        super().__init__(product_id, name, price)
        self.weight = weight
        self.shipping_fee = shipping_fee

    def calculate_final_price(self):
        return self.price + self.shipping_fee


class DigitalProduct(Product):
    """Sản phẩm số: file tải về, có license."""

    def __init__(self, product_id, name, price, file_size, license_type):
        super().__init__(product_id, name, price)
        self.file_size = file_size       # Đơn vị: MB
        self.license_type = license_type  # "one-time" hoặc "lifetime"

    def calculate_final_price(self):
        # Nếu one-time thì giảm 20%
        if self.license_type == "one-time":
            return self.price * 0.8
        else:
            return self.price














