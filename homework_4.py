# ===== HOMEWORK 4 - PYTHON BUỔI 4 =====
# Chủ đề: Cấu trúc dữ liệu: Stack & Queue
# Họ tên: [Trần Thị Thủy Tiên]_BrSE AI
# Ngày: 24/04-08/05/2026
# =======================================

### =======================================
# BÀI 1: Lịch sử điều hướng trang [STACK]
# Browser history service cần hỗ trợ nút "Back" và "Forward" khi user duyệt sản phẩm. 
### =======================================

class BrowserHistory:
    def __init__(self, homepage):
        self.back_stack = [homepage]
        self.forward_stack = []

    def visit(self, url):
        self.back_stack.append(url)
        self.forward_stack = []

    def back(self, steps):
        while steps > 0 and len(self.back_stack) > 1:
            self.forward_stack.append(self.back_stack.pop())
            steps -= 1

        return self.back_stack[-1]

    def forward(self, steps):
        while steps > 0 and self.forward_stack:
            self.back_stack.append(self.forward_stack.pop())
            steps -= 1


        return self.back_stack[-1]


h = BrowserHistory("trang-chu")

h.visit("san-pham/ao-thun")
h.visit("san-pham/quan-jean")
h.visit("gio-hang")

print(h.back(1))
print(h.back(1))
print(h.forward(1))
print(h.back(3))


### ============================================
# BÀI 2: Kiểm tra cú pháp JSON (ngoặc) hợp lệ [STACK]
# Chức năng gateway cần kiểm tra payload JSON (thông tin) trước khi xử lý đơn hàng.
### ============================================

class Solution:

    def is_valid_brackets(self, s):

        stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        opens = {'(', '[', '{'}

        for ch in s:

            if ch in opens:
                stack.append(ch)

            elif ch in pairs:

                if not stack or stack[-1] != pairs[ch]:
                    return False

                stack.pop()

        return len(stack) == 0


solution = Solution()

print(solution.is_valid_brackets('{"name": "An", "items": [1, 2]}'))
print(solution.is_valid_brackets('{"data": [{"id": 1}'))
print(solution.is_valid_brackets('(())'))
print(solution.is_valid_brackets('{"data": [{"id": 1]}'))


### =================================
# BÀI 3: Hàm Validate Transaction Order(events)
# Kiểm tra list event có tuân theo flow: INIT → PROCESSING → COMPLETED hoặc INIT → PROCESSING → FAILED. 
### =================================

class Solution:
    def validate_transaction_order(self, events):

        txn_state = {}

        valid_next = {
            None: ["INIT"],
            "INIT": ["PROCESSING"],
            "PROCESSING": ["COMPLETED", "FAILED"]
        }

        errors = []
        completed = 0

        for ev in events:

            txn_id = ev["txn_id"]
            event = ev["event"]

            current = txn_state.get(txn_id)

            allowed = valid_next.get(current, [])

            if event not in allowed:

                if current == "INIT" and event in ["COMPLETED", "FAILED"]:
                    errors.append(f"{txn_id}: thieu buoc PROCESSING")
                else:
                    errors.append(f"{txn_id}: sai thu tu su kien")

            txn_state[txn_id] = event

            if event == "COMPLETED":
                completed += 1

        return {
            "valid": len(errors) == 0,
            "completed": completed,
            "errors": errors
        }

events1 = [
    {"txn_id": "T1", "event": "INIT"},
    {"txn_id": "T2", "event": "INIT"},
    {"txn_id": "T2", "event": "PROCESSING"},
    {"txn_id": "T2", "event": "COMPLETED"},
    {"txn_id": "T1", "event": "PROCESSING"},
    {"txn_id": "T1", "event": "FAILED"},
]

events2 = [
    {"txn_id": "T3", "event": "INIT"},
    {"txn_id": "T3", "event": "COMPLETED"}, # thieu PROCESSING
]

solution = Solution()
print(solution.validate_transaction_order(events1))
print(solution.validate_transaction_order(events2))


### ======================================
# BÀI 4: Priority Shipping Queue [QUEUE]
# Shipping service ưu tiên đơn VIP và đơn Express trước đơn thường.
### ======================================

import heapq

class PriorityShippingQueue:

    def __init__(self):
        self.heap = []
        self.counter = 0
        self.priority_map = {
            "express": 1,
            "vip": 2,
            "normal": 3
        }

    def enqueue(self, order):
        priority = self.priority_map[order["type"]]
        heapq.heappush(
            self.heap,
            (priority, self.counter, order)
        )
        self.counter += 1

    def dequeue(self):
        if not self.heap:
            return None

        priority, counter, order = heapq.heappop(self.heap)
        return order

psq = PriorityShippingQueue()

psq.enqueue({"id": "S1", "type": "normal", "dest": "HN"})
psq.enqueue({"id": "S2", "type": "express", "dest": "HCM"})
psq.enqueue({"id": "S3", "type": "vip", "dest": "DN"})
psq.enqueue({"id": "S4", "type": "express", "dest": "HN"})

print(psq.dequeue())
print(psq.dequeue())
print(psq.dequeue())


### =========================
# BÀI 5: Simulate Checkout
# Mô phỏng hàng chờ thanh toán tại quầy [QUEUE] 
# POS system cần mô phỏng hàng chờ tại nhiều quầy thanh toán để tối ưu staffing.
### =========================

class Solution:
    def simulate_checkout(self, customers, n_counters):

        counters = {}

        for i in range(1, n_counters + 1):
            counters[f"counter_{i}"] = {
                "customers": [],
                "total_items": 0
            }

        for customer in customers:

            min_counter = min(
                counters,
                key=lambda c: len(counters[c]["customers"])
            )

            counters[min_counter]["customers"].append(customer["id"])
            counters[min_counter]["total_items"] += customer["items"]

        return counters


customers = [
    {"id": "C1", "items": 5},
    {"id": "C2", "items": 12},
    {"id": "C3", "items": 3},
    {"id": "C4", "items": 8},
    {"id": "C5", "items": 1},
]

print(Solution().simulate_checkout(customers, 2))


### =============================================================================
# 6. Graph và Tree khác nhau như thế nào? Khi nào dùng Graph, khi nào dùng Tree? 
### =============================================================================

# Tree là cây, Graph là mạng lưới.
# Tree là một dạng đặc biệt của Graph.
# Tree không có vòng lặp (cycle), còn Graph có thể có.
# Tree dùng cho dữ liệu phân cấp.
# Graph dùng cho dữ liệu dạng mạng lưới.

## Khi nào dùng Tree? 
# Dùng khi: Có cấp bậc, Có cha con, Có phân cấp (Folder, Cây gia đình, Sơ đồ công ty...)

## Khi nào dùng Graph? 
# Dùng khi: Nhiều kết nối, Quan hệ phức tạp, Có nhiều đường đi (Bạn bè Facebook, Network, Google Maps....)


### ============================================================================
# 7. Giải thích khái niệm và so sánh DFS và BFS. 
# Hãy suy nghĩ và đưa ra một ví dụ trong hệ thống thương mại điện tử trường hợp nào dùng DFS, trường hợp nào là BFS? 
### ============================================================================

## DFS(Depth First Search) là thuật toán duyệt đồ thị theo chiều sâu. Thuật toán sẽ ưu tiên đi sâu vào một nhánh trước, sau đó mới quay lui (backtrack) để duyệt các nhánh khác.

# DFS(Depth First Search) thường được dùng khi cần: duyệt toàn bộ các nhánh, tìm đường đi, hoặc phát hiện chu trình (detect cycle).
# DFS(Depth First Search) thường được cài đặt bằng: Stack hoặc Recursion.

## BFS(Breadth First Search) là thuật toán duyệt đồ thị theo chiều rộng. Thuật toán sẽ duyệt lần lượt từng tầng (level) từ gần đến xa.

# BFS(Breadth First Search) thường được dùng khi cần: tìm đường đi ngắn nhất trong graph không trọng số (weighted không có), hoặc xử lý dữ liệu theo từng cấp độ.
# BFS(Breadth First Search) thường sử dụng: Queue (hàng đợi) để duyệt theo từng tầng.

## Trong hệ thống thương mại điện tử:

# DFS(Depth First Search) phù hợp khi cần duyệt toàn bộ category tree hoặc folder sản phẩm.
# BFS(Breadth First Search) phù hợp khi cần tìm warehouse gần nhất hoặc tìm route giao hàng ngắn nhất.


### ============================================================================
# 8.  Binary Search Tree (BST) là đồ thị dạng cây, cây nhị phân
#                Đề sai nên học viên được bỏ qua.
### ============================================================================

## Binary Search Tree (BST) có tính chất:

# Node trái < node (Đỉnh Cha) hiện tại
# Node phải > node (Đỉnh Cha) hiện tại


### ============================================================================
# 9.  Đồ thị có thể biểu diễn bằng Adjacency List hoặc Adjacency Matrix. 
### ============================================================================

# Nên chọn Adjacency List vì hệ thống có 10,000 node nhưng mỗi node chỉ kết nối khoảng 5 node (= khoảng ~50,000 cạnh) , chỉ lưu các cạnh thật sự tồn tại, không cần lưu toàn bộ ma trận N x N, nên đây là sparse graph (đồ thị thưa).

# Nếu dùng Adjacency Matrix sẽ tốn rất nhiều bộ nhớ vì phải tạo ma trận 10,000 x 10,000 (= cần 100 triệu ô nhớ). Adjacency List sẽ tối ưu tiết kiệm RAM và phù hợp hơn cho DFS/BFS.


### ============================================================================
# 10. Chu trình trong Graph : Chu trình (Cycle) trong đồ thị (graph)
# Đề bài: Làm sao để kiểm tra một đồ thị có chu trình hay không? 
# Gợi ý: Sử dụng DFS, cần lưu thêm gì để phát hiện cycle?
### ============================================================================

# Để kiểm tra trong đồ thị (graph) có Chu trình (Cycle) hay không bằng DFS(Depth First Search) thì cần : dùng visited để đánh dấu node đã đi, lưu thêm parent, nếu gặp node đã visited và node đó không phải parent thì đồ thị (graph) có Chu trình (Cycle). 
# Một cách khác, Trong đồ thị (graph) vô hướng cần lưu parent để tránh hiểu nhầm cạnh quay ngược về cha là Chu trình (Cycle).
