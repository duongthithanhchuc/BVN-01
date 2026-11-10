# Nhập một số nguyên từ $0$ đến $9$, in ra tên chữ số tương ứng ($0 \rightarrow$ "Không", $1 \rightarrow$ "Một", ...).
# dùng match...case như gợi ý:
n = int(input("Nhập một số nguyên từ 0 đến 9: "))

match n:
    case 0:
        print("Không")
    case 1:
        print("Một")
    case 2:
        print("Hai")
    case 3:
        print("Ba")
    case 4:
        print("Bốn")
    case 5:
        print("Năm")
    case 6:
        print("Sáu")
    case 7:
        print("Bảy")
    case 8:
        print("Tám")
    case 9:
        print("Chín")
    case _:
        print("Số nhập vào không nằm trong khoảng từ 0 đến 9!")
# Dùng list và index:
n = int(input("Nhập một số nguyên từ 0 đến 9: "))

ten_so = ["Không", "Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"]

if 0 <= n <= 9:
    print(ten_so[n])
else:
    print("Số nhập vào không nằm trong khoảng từ 0 đến 9!")