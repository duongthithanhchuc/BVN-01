# Viết chương trình nhập vào 3 số nguyên a, b, c; in ra số lớn nhất, nếu 3 số bằng nhau thì in dấu "=".   
# Dữ liệu vào: Một dòng có 3 số nguyên cách nhau bởi dấu cách theo thứ tự là a, b và c.   
# Dữ liệu ra: Số lớn nhất trong 3 số a, b, c hoặc dấu =.  
a, b, c = map(float, input().split())
if a == b == c:
    print("=")
else:
    print( max(a, b, c))