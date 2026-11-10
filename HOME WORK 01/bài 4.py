# Viết chương trình nhập vào một "kí tự" c. Kiểm tra xem c có phải là kí tự chữ cái không (hoa hoặc thường). Nếu đúng thì in ra "{c} la ki tu alphabet", nếu sai in ra "{c} khong phai la ki tu alphabet".
c = input("Nhập vào một kí tự: ")

if c.isalpha():
    print(f"{c} la ki tu alphabet")
else:
    print(f"{c} khong phai la ki tu alphabet")

#Cách 2:
d = input("Nhập vào một kí tự: ")
if ('a' <= d <= 'z') or ('A' <= d <= 'Z'):
    print(f"{d} la ki tu alphabet")
else:
    print(f"{d} khong phai la ki tu alphabet")