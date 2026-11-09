# Một khu đất hình chữ nhật có chiều rộng $a$, chiều dài $b$. Người ta xây công viên vui chơi hình tròn tại vị trí trung tâm khu đất như hình vẽ. Nhập vào $a, b$. Hãy tính diện tích còn lại để trồng cây xung quanh là bao nhiêu. Biết pi = 3.14, lấy kết quả làm tròn 2 chữ số phần thập phân.
a = float(input("Nhập chiều rộng a: "))
b = float(input(" Nhập chiều dài b: "))

r = a / 2

s_hcn = a * b
s_tron = 3.14 * (r ** 2)
s_trong_cay = s_hcn - s_tron

print(f"Diện tích trồng cây là: {s_trong_cay:.2f}")
