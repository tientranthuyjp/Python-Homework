# ===== HOMEWORK 3 - PYTHON BUỔI 3 =====
# Chủ đề: Data Structures trong Python.
# List, Dict (Dictionary), Set.
# Họ tên: [Trần Thị Thủy Tiên]_BrSE AI
# Ngày: 21-28/04/2026
# =======================================

##### Bài 1: Lọc sản phẩm còn hàng [LIST]
def filter_available(products):
    result = []
    for product in products:
        if product["stock"] > 0 and product["is_active"] == True:
            result.append(product)
    return result


products = [
    {"id": 1, "name": "Áo thun", "stock": 10, "is_active": True},
    {"id": 2, "name": "Quần jean", "stock": 0, "is_active": True},
    {"id": 3, "name": "Giày", "stock": 5, "is_active": False},
    {"id": 4, "name": "Nón", "stock": 3, "is_active": True},
]

print(filter_available(products))


##### Bài 2: Tính tổng giá trị giỏ hàng [LIST]
def cart_total(cart, discount_percent=0):
    total = sum(item["price"] * item["quantity"] for item in cart)
    final = total * (1 - discount_percent / 100)
    return f"{int(final):,} VND"
cart = [
        {"price": 100000, "quantity": 2},
        {"price": 50000, "quantity": 1}
    ]
print(cart_total(cart, 10))


##### Bài 3: Gợi ý sản phẩm liên quan [LIST]
def related_products(product_id, products, limit=3):
    # Tìm category của sản phẩm hiện tại
    current_product = None
    for p in products:
        if p["id"] == product_id:
            current_product = p
            break

    if not current_product:
        return []

    # Lấy category
    category = current_product["category"]

    # Related sản phẩm cùng category, loại chính nó khác id
    related = []
    for p in products:
        if p["category"] == category and p["id"] != product_id:
            related.append(p)

    # (Sort)Sắp xếp theo rating giảm dần
    related.sort(key=lambda x: x["rating"], reverse=True)

    # Lấy limit
    return related[:limit]

products2 = [
        {"id": 1, "category": "A", "rating": 5},
        {"id": 2, "category": "A", "rating": 4},
        {"id": 3, "category": "A", "rating": 3},
        {"id": 4, "category": "B", "rating": 5},
    ]
print(related_products(1, products2))


##### Bài 4: Phát hiện đơn hàng bất thường [LIST]
def detect_anomalies(orders, threshold=2.5):
    if not orders:
        return []

    total_sum = sum(order.get("total", 0) for order in orders)
    avg = total_sum / len(orders)

    anomalies = []
    for order in orders:
        if order.get("total", 0) > threshold * avg:
            anomalies.append(order)

    return anomalies

orders = [{"total": 100}, {"total": 200}, {"total": 1000}]
print(detect_anomalies(orders))


##### Bài 5: Xếp hạng sản phẩm bán chạy theo tuần [LIST]
def top_selling(items, top_n=2):
    # Stats data
    stats = {}

    for item in items:
        pid = item["product_id"]

        if pid not in stats:
            stats[pid] = {
                "product_id": pid,
                "name": item["name"],
                "total_qty": 0,
                "revenue": 0
            }

        # Cộng dồn
        stats[pid]["total_qty"] += item["qty"]
        stats[pid]["revenue"] += item["qty"] * item["price"]

    # Convert sang list
    result = list(stats.values())

    # Sort giảm dần theo total_qty
    result.sort(key=lambda x: x["total_qty"], reverse=True)

    # Lấy top N
    return result[:top_n]

items = [
        {"product_id": 1, "name": "A", "qty": 2, "price": 100},
        {"product_id": 1, "name": "A", "qty": 3, "price": 100},
        {"product_id": 2, "name": "B", "qty": 5, "price": 50},
    ]
print(top_selling(items))


##### Bài 6: Xây dựng catalog sản phẩm [DICT]
def build_catalog(products):
    catalog = {}
    for product in products:
        catalog[product["id"]] = product
    return catalog

print(build_catalog(products))


##### Bài 7: Thống kê đơn hàng theo trạng thái [DICT]
def count_by_status(statuses):
    result = {}
    for status in statuses:
        if status in result:
            result[status] += 1
        else:
            result[status] = 1
    return result
print(count_by_status(["new", "done", "new"]))

##### Bài 8: Áp dụng mã giảm giá [DICT]
def apply_coupon(total_amount, code, coupon_db):
    if code not in coupon_db:
        return {
            "valid": False,
            "message": "Mã không tồn tại"
        }

    coupon = coupon_db[code]

    if total_amount < coupon.get("min_order", 0):
        return {
            "valid": False,
            "message": "Không đủ điều kiện"
        }

    if coupon["type"] == "percent":
        discount_amount = total_amount * coupon["value"] / 100
        message = f"Áp dụng thành công {code} (-{coupon['value']}%)"
    else:
        discount_amount = coupon["value"]
        message = f"Áp dụng thành công {code} (-{coupon['value']:,} VND)"

    discount_amount = min(discount_amount, total_amount)
    final_price = total_amount - discount_amount

    return {
        "valid": True,
        "discount_amount": f"{int(discount_amount):,} VND",
        "final_price": f"{int(final_price):,} VND",
        "message": message
    }

coupon_db = {
        "SALE10": {"type": "percent", "value": 10, "min_order": 100000}
    }
print(apply_coupon(200000, "SALE10", coupon_db))

##### Bài 9: Tổng hợp báo cáo doanh thu theo ngày [DICT]
def daily_report(transactions):
    report = {}

    for tx in transactions:
        date = tx["date"]
        amount = tx["amount"]

        if date not in report:
            report[date] = {
                "total": 0,
                "count": 0,
                "avg": 0
            }

        report[date]["total"] += amount
        report[date]["count"] += 1

    for date in report:
        avg = report[date]["total"] / report[date]["count"]

        report[date]["total"] = f"{report[date]['total']:,} VND"
        report[date]["avg"] = f"{int(avg):,} VND"

    return report    
 
tx = [
        {"date": "2026-01-01", "amount": 100},
        {"date": "2026-01-01", "amount": 200}
    ]
print(daily_report(tx))


##### Bài 10: Quản lý phiên đăng nhập [DICT]
import time

class SessionStore:
    def __init__(self, timeout=1800):
        """
        timeout: thời gian sống của session (giây)
        """
        self.timeout = timeout
        self.store = {}

    def create(self, user_id, data):
        """
        Tạo session mới
        """
        now = int(time.time())

        session = {
            "user_id": user_id,
            "data": data,
            "created_at": now,
            "expires_at": now + self.timeout
        }

        self.store[user_id] = session

    def get(self, user_id):
        """
        Lấy session nếu còn hạn
        """
        session = self.store.get(user_id)

        # Không tồn tại
        if session is None:
            return None

        now = int(time.time())

        # Hết hạn
        if now > session["expires_at"]:
            del self.store[user_id]
            return None

        return session

    def delete(self, user_id):
        if user_id in self.store:
            del self.store[user_id]

store = SessionStore()
store.create(1, {"name": "Tien"})
print(store.get(1))


##### Bài 11: Hệ thống phân quyền RBAC [DICT]
def can_access(role, resource, action, rbac):
    if role not in rbac:
        return False
    
    role_permissions = rbac[role]
    if resource not in role_permissions:
        return False
    
    return action in role_permissions[resource]

rbac = {
        "admin": {"product": ["create", "delete"]},
        "user": {"product": ["view"]}
    }
print(can_access("admin", "product", "create", rbac))


##### Bài 12: Tính phí vận chuyển theo vùng [DICT]
def calc_shipping(city, weight_kg, order_total, zones):
    if city in zones:
        zone = zones[city]
    else:
        zone = zones["other"]
        city = "other"

    if order_total >= zone["free_threshold"]:
        return {
            "fee": 0,
            "free_shipping": True,
            "message": f"Miễn phí ship đến {city}"
        }

    fee = zone["zone_rate"] * weight_kg

    if fee < zone["min_fee"]:
        fee = zone["min_fee"]

    fee_int = int(fee)

    return {
        "fee": fee_int,
        "free_shipping": False,
        "message": f"Phí ship đến {city}: {fee_int:,} VND"
    }

zones = {
        "HCM": {"zone_rate": 10000, "min_fee": 20000, "free_threshold": 500000},
        "other": {"zone_rate": 15000, "min_fee": 30000, "free_threshold": 700000}
    }
print(calc_shipping("HCM", 2, 300000, zones))


##### Bài 13: Kiểm tra sản phẩm trong wishlist [SET]
def is_wishlisted(product_id, wishlist):
    return product_id in wishlist

print(is_wishlisted(1, {1, 2, 3}))


##### Bài 14: Tìm sản phẩm chưa được xem [SET]
def get_unviewed(all_products, viewed_products):
    return all_products - viewed_products
products3 = [
        {"category": "A"},
        {"category": "B"},
        {"category": "A"}
    ]

print(get_unviewed({1, 2, 3, 4}, {2, 3}))


##### Bài 15: Lấy danh sách danh mục duy nhất [SET]
def unique_categories(products):
    result = set()
    for p in products:
        result.add(p["category"])
    return result

products3 = [
        {"category": "A"},
        {"category": "B"},
        {"category": "A"}
    ]
print(unique_categories(products3))


##### Bài 16: Gợi ý sản phẩm cùng mua (cross-sell) [SET]
def cross_sell(product_id, order_history, current_cart):
    related = set()
    for order in order_history:
        items = order["items"]
        if product_id in items:
            for item in items:
                if item != product_id:
                    related.add(item)
    
    return related - current_cart

order_history = [
        {"items": {1, 2, 3}},
        {"items": {1, 4}}
    ]
print(cross_sell(1, order_history, {2}))


##### Bài 17: Phát hiện sản phẩm bị xóa khỏi flash sale [SET]
def sale_diff(old_sale, new_sale):
    return {
        "removed": old_sale - new_sale,
        "added": new_sale - old_sale,
        "kept": old_sale & new_sale
    }

print(sale_diff({1, 2, 3}, {2, 3, 4}))


##### Bài 18: Lọc review hợp lệ theo người dùng đã mua [SET]
def filter_verified_reviews(reviews, verified_buyers):
    result = []
    for review in reviews:
        if review["user_id"] in verified_buyers:
            result.append(review)
    return result

reviews = [
        {"user_id": 1, "content": "ok"},
        {"user_id": 2, "content": "good"}
    ]
print(filter_verified_reviews(reviews, {1}))


##### Bài 19: Phân tích hành vi mua hàng theo segment [SET]
def segment_users(order_counts):
    result = {
        "one_time": set(),
        "repeat": set(),
        "vip": set()
    }
    
    for user_id, count in order_counts.items():
        if count == 1:
            result["one_time"].add(user_id)
        elif count >= 2 and count <= 4:
            result["repeat"].add(user_id)
        else:  # count >= 5
            result["vip"].add(user_id)
    
    return result

print(segment_users({1: 1, 2: 3, 3: 5}))


##### Bài 20: Kiểm tra xung đột kho hàng trong flash sale [SET]
def check_conflicts(flash_sale_items, active_campaigns):
    flash_sale_items = set(flash_sale_items)

    conflicts = {}
    conflicting_items = set()

    for item in flash_sale_items:
        for campaign_name, campaign_items in active_campaigns.items():
            if item in campaign_items:
                conflicts.setdefault(item, []).append(campaign_name)
                conflicting_items.add(item)

    safe_items = flash_sale_items - conflicting_items

    return {
        "has_conflict": len(conflicts) > 0,
        "conflicts": conflicts,
        "safe_items": safe_items
    }

campaigns = {
        "camp1": {1, 2},
        "camp2": {2, 3}
    }
print(check_conflicts({1, 2, 4}, campaigns))

