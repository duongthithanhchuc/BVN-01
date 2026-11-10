# Nhập vào 3 số $a, b, c$. Kiểm tra xem đây có phải là cạnh của 1 tam giác không, nếu đúng thì tính diện tích của tam giác đó, in ra với 1 chữ số phần thập phân. Nếu nó không phải 3 cạnh của tam giác thì in ra "Khong phai 3 canh cua tam giac"
import math

a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    p = (a + b + c)/ 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"{s:.1f}")
else:
    print("Khong phai 3 canh cua tam giac")