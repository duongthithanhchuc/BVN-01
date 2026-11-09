# Viết chương trình nhập vào một số nguyên $n$. Kiểm tra xem số đó có chữ số tận cùng là $5$ hay không. Nếu đúng in ra "True", nếu sai in ra "False".

n = int(input("Nhập một số nguyên: "))

if abs(n) % 10 == 5:
    print("True")
else:
    print("False")