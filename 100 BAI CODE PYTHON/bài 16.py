# Viết chương trình nhập vào điểm trung bình học kỳ I và trung bình học kỳ II, tính trung bình cả năm theo công thức:  TBCN=(TBHKI+TBHKII*2)/3. Xếp lọai theo cách:
# “Gioi” nếu TBCN>=8
# “Kha” nếu 6.5<=TBCN <8
#“Trung binh” nếu 5.0<=TBCN <6.5
#“Yeu” nếu 3.5<=TBCN <5
#“Kem” nếu TBCN<3.5
#Dữ liệu vào Một dòng có 2 số thực cách nhau bởi dấu cách theo thứ tự là TBHKI và TBHKII
#Dữ liệu ra Dòng đầu là TBCN, làm tròn đến 1 chữ số thập phân; dòng thứ hai là xếp loại
a, b = map(float, input().split())
diem = (a + b * 2) / 3
print(f'{diem:.2f}')
if diem >= 8:
    print('Gioi')
elif diem >= 6.5:
    print('Kha')
elif diem >= 5.0:
    print('Trung binh')
elif diem >= 3.5:
    print('Yeu')
else:
    print('Kem')