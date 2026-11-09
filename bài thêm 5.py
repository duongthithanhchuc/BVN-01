# Viết chương trình nhập vào hai số, in ra số lớn hơn hoặc thông báo nếu hai số bằng nhau.

a = float(input("Nhập số thứ nhất (a): "))
b = float(input("Nhập số thứ hai (b): "))

if a > b:
    print(f"Số lớn hơn là: {a}")
elif b > a:
    print(f"Số lớn hơn là: {b}")
else:
    print("Hai số bằng nhau.")