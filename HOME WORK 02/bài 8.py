# giải hệ phương trình tuyến tính ax+by=m và cx+dy=n
a, b, c, d, m, n = map(float, input("Nhập vào 6 số a, b, c, d, m, n:").split())
x = ( m*(d-b))/(a*d-b*c)
y = (m*(c-a))/(b*c-d*a)
print(f"Nghiệm của hệ phương trình tuyến tính là: {x} và {y} ")