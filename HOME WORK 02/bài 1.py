# Nhập vào độ dài 2 cạnh của hình chữ nhật. In ra màn hình chu vi và diện tích của nó.
a = int(input("Nhập vào chiều dài: "))
b = int(input("Nhập vào chiều rộng:"))

chu_vi = (a + b) * 2
print(f"Chu vi của hình chữ nhật:{chu_vi}")
dien_tich = a * b
print(f"Diện tích của hình chữ nhật:{dien_tich}")
