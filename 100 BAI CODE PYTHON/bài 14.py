# Cho tuổi của một người (0 < tuổi <= 150), trả lời:   "Thieu nhi" nếu 0 < tuổi <= 11"Thieu nien" nếu 11 < tuổi <= 25"Trung nien" nếu 25 < tuổi <= 50"Lao nien" nếu tuổi > 50
# Dữ liệu vào: Một số nguyên t là tuổi của một người.  
tuoi = int(input())

if tuoi > 50:
    print("Lao nien")
elif tuoi > 25:
    print("Trung nien")
elif tuoi > 11:
    print("Thieu nien")
else:
    print("Thieu nhi")