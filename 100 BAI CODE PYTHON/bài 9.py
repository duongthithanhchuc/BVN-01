# Viết chương trình nhập vào điểm Toán, Văn, Anh văn của 1 học sinh là các số thực. Tính trung bình của học sinh đó, biết rằng điểm Toán, Văn là hệ số 2.   
# Dữ liệu vào: Gồm 1 dòng có 3 số thực cách nhau bởi dấu cách theo thứ tự là Toan, Van và Anh.   
# Dữ liệu ra: Là điểm trung bình làm tròn đến 1 chữ số thập phân.

toan, van, anh = map(float, input().split())

dtb = (toan * 2 + van * 2 + anh) / 5

print(f"{dtb:.1f}")