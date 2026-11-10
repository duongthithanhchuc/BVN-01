# Viết chương trình nhập năm sinh của một người, kiểm tra xem người đó có đủ 18 tuổi để đi bầu cử hay không (tính đến năm hiện tại là 2026).
nam_sinh = int(input("Nhập năm sinh: "))
nam_hien_tai = 2026
tuoi = nam_hien_tai - nam_sinh
if tuoi >= 18:
    print(f"Bạn năm nay {tuoi} tuổi: Đủ điều kiện đi bầu cử")
else:
    print(f"Bạn năm nay {tuoi} tuổi: Chưa đủ tuổi đi bầu cử")
    