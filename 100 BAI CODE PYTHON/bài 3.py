# Tính chu vi (cv) và diện tích (dt) hình chữ nhật với chiều dài a, chiều rộng b theo công thức cv = (a + b) * 2 và dt = a * b.
#Dữ liệu vào: Gồm 1 dòng có 2 số nguyên a, b cách nhau bởi dấu cách theo thứ tự là chiều dài và chiều rộng.
#Dữ liệu ra: Chu vi và diện tích nằm trên cùng một dòng, cách nhau bởi 1 dấu cách.

def tinh_hinh_chu_nhat(dai, rong):
    cv = ( dai + rong) * 2
    dt = dai * rong
    return cv, dt

a, b = map(int, input().split())
cv, dt = tinh_hinh_chu_nhat(a, b)
print(cv, dt)