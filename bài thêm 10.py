# Nhập điểm thi, nếu điểm $\ge 4$ thì in "Qua môn", ngược lại in "Học lại".

diem = float(input("Nhập điểm thi của bạn: "))

if diem >= 4:
    print("Qua môn")
else:
    print("Học lại")