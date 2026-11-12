# Nhập vào thời gian 1 công việc nào đó là x giây. Hãy chuyển đổi và viết ra màn hình số thời gian trên dưới dạng bằng bao nhiêu giờ, bao nhiêu phút, bao nhiêu giây.
#Cách 1: Dùng hàm divmod(a, b)

x = int(input("Nhập thời gian ( giây): "))
gio, giay_du = divmod(x, 3600)
phut, giay = divmod(giay_du, 60)
print(f"{gio} giờ, {phut} phút, {giay} giây")

#Cách 2:dùng def
def quy_doi_thoi_gian(tong_giay):
    gio, giay_du = divmod(tong_giay, 3600)
    phut, giay = divmod(giay_du, 60)
    return gio, phut, giay
x = int(input("Nhập vào thời gian ( giây): "))
h, m, s = quy_doi_thoi_gian(x)
print(f"Thời gian hoàn thành:{h} giờ, {m} phút, {s} giây")

#Cách 3:Dùng thư viện chuẩn
import datetime
x = int(input("Nhập tổng số giây: "))
thoi_gian = datetime.timedelta(seconds=x)
print(f"Định dạng Giờ: Phút: Giây là:", thoi_gian)
        

