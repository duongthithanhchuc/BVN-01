#Tính $x^y$ (Với $x, y$ là số thực).
x, y = map(float, input("Nhập vào 2 số thức x, y: ").split())
ket_qua = pow(x,y)
print(f"Kết quả {ket_qua}")
#Cách 2
print( x**y )