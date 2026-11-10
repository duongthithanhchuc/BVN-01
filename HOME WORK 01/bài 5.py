# Nhập vào chữ cái hoa A, in ra chữ cái thường liền trước chữ cái a thường tương ứng của A. Xét trường hợp đặc biệt khi c = 'A'.
c = input("Nhập vào chữ cái hoa: ")

c_thuong = c.lower()
if c == 'A':
    ket_qua = 'z'
else:
    ket_qua = chr(ord(c_thuong) - 1)
print(ket_qua)