# Cho một số nguyên có 3 chữ số. In ra 2 chữ số cuối và 2 chữ số đầu của số vừa nhập.   
# Dữ liệu vào: Một số nguyên n có 3 chữ số.   
# Dữ liệu ra: Là 2 chữ số đầu và 2 chữ số cuối của n, cách nhau bởi dấu cách (nếu 2 chữ số là 0 thì in 00, nếu 2 chữ số mà có 0 phía trước thì vẫn in, vd 05).   

n = input().strip()

hai_so_dau = n[:2]
hai_so_cuoi = n[-2:]

print(hai_so_dau, hai_so_cuoi)
 # cách 2

n = int(input())

hai_so_dau = n // 10
hai_so_cuoi = n % 100

print(f"{hai_so_dau:02d} {hai_so_cuoi:02d}")