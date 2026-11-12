# Nhập vào tâm và bán kính của một đường tròn. Sau đó nhập vào một điểm $A(x, y)$ bất kì và kiểm tra xem nó có thuộc đường tròn hay không?
import math
x_I, y_I = map(float, input("Nhập vào tọa độ tâm I(x,y): ").split())
r = int(input(f"Nhập vào bán kính đtr (r):"))
x_A, y_A = map(float, input("Nhập vào tọa độ điểm A(x,y): ").split())

tam_I = [x_I, y_I]
diem_A = [x_A, y_A]

khoang_cach = math.dist([x_I,y_I], [x_A, y_A] )

if math.isclose(khoang_cach, r):
    print(f"{diem_A} thuộc đường tròn")
else:
    print(f"{diem_A} không thuộc đường tròn")
    