# Viết chương trình nhập vào một "kí tự" c, nếu nó là chữ hoa thì in ra chữ thường tương ứng và ngược lại nếu nó là chữ thường thì in ra chữ hoa tương ứng của nó.
c = input("Nhập vào một kí tự: ")

if c.isupper():
    ket_qua = c.lower()
else:
    ket_qua = c.upper()

print(ket_qua)