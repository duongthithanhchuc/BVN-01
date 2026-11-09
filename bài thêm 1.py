# (Kiểm tra số chẵn lẻ): Viết chương trình nhập một số nguyên, kiểm tra và in ra số đó là số chẵn hay số lẻ.

n = int(input("Nhập vào một số nguyên: "))

if n % 2 == 0:
    print(f"{n} la so chan")
else:
    print(f"{n} la so le")