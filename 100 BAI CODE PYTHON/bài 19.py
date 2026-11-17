# Nhập vào số xe (có năm chữ số) trong biển số xe máy của bạn. Cho biết số xe của bạn được mấy nút. Bạn là người may mắn nếu số nút=9. Bạn có may mắn không?Ví dụ: số xe là 45046, tổng các chữ số là 4+ 5 +0+ 4 + 6 = 19 thì 19 mod 10 =9. Số nútlà 9: may man. Số xe 12340, tổng các chữ số là 1+2+3+4+0=10 thì 10 mod 10=0. Số nút là 0: chua may man Dữ liệu vào Một số nguyên x có 5 chữ số Dữ liệu ra Dòng 1 là số nút, dòng 2 là “may man” hoặc “chua may man
n = input()
tong = 0
for i in n:
    tong += int(i)
    mod = tong % 10
if mod == 9:
    print('may man')
else:
    print('chua may man')


