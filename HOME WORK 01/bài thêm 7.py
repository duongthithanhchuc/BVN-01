# Nhập điểm (0–10), phân loại học lực theo quy tắc:$\ge 8$: Giỏi$\ge 6.5$ và $< 8$: Khá$\ge 5$ và $< 6.5$: Trung bình$< 5$: Yếu

diem = float(input("Nhập điểm (0 - 10): "))

if diem < 0 or diem > 10:
    print("Điểm không hợp lệ! Vui lòng nhập điểm từ 0 đến 10.")
else:   
    if diem >= 8:
        print("Học lực: Giỏi")
    elif diem >= 6.5:
        print("Học lực: Khá")
    elif diem >= 5:
        print("Học lực: Trung bình")
    else:
        print("Học lực: Yếu")