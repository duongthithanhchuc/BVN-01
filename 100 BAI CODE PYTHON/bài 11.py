# iết chương trình nhập vào tổng số giây là một số nguyên, in ra giờ:phút:giây.   
# Dữ liệu vào: Một số nguyên là tổng số giây.   
# Dữ liệu ra: Kết quả đổi được theo dạng giờ:phút:giây.

tong_giay = int(input())

gio = tong_giay // 3600
phut = (tong_giay % 3600) // 60
giay = tong_giay % 60

print(f"{gio}:{phut}:{giay}")