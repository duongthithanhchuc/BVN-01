# Nhập năm sinh, tính tuổi hiện tại (giả sử năm hiện tại là 2025 theo yêu cầu cụ thể của đề bài), và kiểm tra xem người đó đã đủ 18 tuổi hay chưa.

nam_sinh = int(input("Nhập năm sinh của bạn: "))

nam_hien_tai = 2025

tuoi = nam_hien_tai - nam_sinh

print(f"Tuổi hiện tại của bạn là: {tuoi} tuổi.")

if tuoi >= 18:
    print("Kết luận: Bạn ĐÃ ĐỦ 18 tuổi.")
else:
    print("Kết luận: Bạn CHƯA ĐỦ 18 tuổi.")