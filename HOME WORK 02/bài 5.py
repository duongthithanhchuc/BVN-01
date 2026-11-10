# Viết chương trình giải phương trình bậc 2
import math
a, b, c = map(float, input("Nhập vào các hệ số a, b, c: ").split())
delta = (b**2) - 4*a*c
if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    x = (-b)/(2*a)
    print(f"Phương trình có nghiệm kép: {x}")
else:
    d = math.sqrt(delta)
    x = (-b-d)/(2*a)
    y = (-b+d)/(2*a)
    print(f"Phương trình có 2 nghiệm phân biệt: {x:.2f} và {y:.2f}")