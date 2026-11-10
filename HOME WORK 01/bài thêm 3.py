# Viết chương trình nhập vào một số nguyên $n$. Kiểm tra xem số đó có chia hết cho cả $3$ và $5$ hay không. Nếu đúng in ra "True", nếu sai in ra "False".

n = int(input("Nhập vào một số nguyên n: "))

if n % 3 == 0 and n % 5 == 0:
    print("True")
else:
    print("False")