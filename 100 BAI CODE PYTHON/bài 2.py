# Tính chu vi (cv) và diện tích (dt) hình tròn với bán kính r là số nguyên theo đúng công thức:
#cv = r * 2 * 3.14
#dt = r * r * 3.14
#Dữ liệu vào: Một số nguyên dương r.
#Dữ liệu ra: Chu vi và diện tích nằm trên cùng một dòng, cách nhau bởi 1 dấu cách, làm tròn đến 2 chữ số thập phân.

r = int(input())
cv = r * 2 * 3.14
dt = r * r * 3.14
print(f"{cv:.2f} {dt:.2f}")

#Cách 2
def tinh_hinh_tron(ban_kinh):
    PI = 3.14
    chu_vi = ban_kinh * 2 * PI
    dien_tich = (ban_kinh ** 2) * PI
    return chu_vi, dien_tich

r = int(input())
cv, dt = tinh_hinh_tron(r)
print(f"{cv:.2f} {dt:.2f}")