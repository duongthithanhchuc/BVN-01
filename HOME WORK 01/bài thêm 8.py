# Viết chương trình nhập năm, kiểm tra xem năm đó có phải năm nhuận hay không.
#(Quy tắc: Năm nhuận là năm chia hết cho 400 hoặc chia hết cho 4 nhưng không chia hết cho 100)

nam = int(input("Nhập vào một năm: "))

if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
    print(f"Năm {nam} là năm nhuận.")
else:
    print(f"Năm {nam} không phải là năm nhuận.")
