# ính tam giácNhập vào ba số $a, b, c$ bất kỳ.Kiểm tra xem $a, b, c$ có thể là độ dài ba cạnh của một tam giác hay không. Nếu không, in ra màn hình thông báo: 'Khong la ba canh cua mot tam giac'.Ngược lại (nếu là ba cạnh tam giác), hãy kiểm tra và xác định đó là loại tam giác gì: Đều, Cân, Vuông, hay Tam giác thường.Tính diện tích, chu vi của tam giác đó và in kết quả ra màn hình.
import math
a = int(input("Nhập vào số thứ nhất:"))
b = int(input("Nhập vào số thứ hai: "))
c = int(input("nhập vào số thứ ba: "))
p = ( a + b + c)/2

if (a + b < c) or (a + c < b) or ( b + c < a):
    print("Không là ba cạnh của một tam giác")
else:
    if a == b == c:
        print("tam giác đều")
    elif a == b or b == c or a == c:
        print("Tam giác cân")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Tam giác vuông")
    else:
        print("Tamm giác thường")
    dien_tich =math.sqrt(p*(p-a)*(p-b)*(p-c))
    chu_vi = (a + b + c)
    print(f"Diện tích là {dien_tich:.2f}")
    print(f"Chu vi là {chu_vi}")
