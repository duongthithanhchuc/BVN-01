# Nhập một tháng (tây), cho biết tháng đó thuộc mùa nào (Xuân, Hạ, Thu, Ðông), biết rằng tháng 2, 3, 4 là mùa Xuân, tháng 5, 6, 7: mùa Hạ, tháng 8, 9, 10: mùa Thu, và tháng 11, 12, 1: mùa Ðông. Dữ liệu vào Một số nguyên t là một tháng trong năm. Dữ liệu ra Kết quả tháng đó thuộc mùa nào trong năm
thang = int(input())
if thang in [ 2, 3, 4]:
    print(f'tháng {thang} là  mùa Xuân')
elif thang  in [ 5, 6, 7]:
    print(f'tháng {thang} là mùa Hạ')
elif thang in [ 8, 9, 10]:
    print(f'tháng {thang} là mùa Thu')
else:
    print(f'tháng {thang} là mùa Đông')
