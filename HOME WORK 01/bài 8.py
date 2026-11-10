# Nhập vào họ tên chủ hộ và chỉ số điện kế tháng trước, chỉ số điện kế tháng này. Tính tiền điện tháng này cho hộ biết các nấc giá:Từ 0 – 50 kWh: 1.984 đồng/kWhBậc 2: Từ 51 – 100 kWh: 2.050 đồng/kWhBậc 3: Từ 101 – 200 kWh: 2.380 đồng/kWhBậc 4: Từ 201 – 300 kWh: 2.998 đồng/kWhBậc 5: Từ 301 – 400 kWh: 3.350 đồng/kWhBậc 6: Từ 401 trở đi kWh: 3.460 đồng/kWhTính thêm tiền VAT 8%. Chỉ lấy đến đơn vị đồng.   

ho_ten = input("Nhập tên chủ hộ: ")
chi_so_cu = int(input("Nhập chỉ số cũ: "))
chi_so_moi = int(input("Nhập chỉ số mới: "))

so_dien = chi_so_moi - chi_so_cu

tien_dien = 0

if so_dien <= 50:
    tien_dien = so_dien * 1984
elif so_dien <= 100:
    tien_dien = (50 * 1984) + (so_dien - 50) * 2050
elif so_dien <= 200:
    tien_dien = (50 * 1984) + (50 * 2050) + (so_dien - 100) * 2380
elif so_dien <= 300:
    tien_dien = (50 * 1984) + (50 * 2050) + (100 * 2380) + (so_dien - 200) * 2998
elif so_dien <= 400:
    tien_dien = (50 * 1984) + (50 * 2050) + (100 * 2380) + (100 * 2998) + (so_dien - 300) * 3350
else:
    tien_dien = (50 * 1984) + (50 * 2050) + (100 * 2380) + (100 * 2998) + (100 * 3350) + (so_dien - 400) * 3460

tong_tien = round(tien_dien * 1.08)

print(f"Ho va ten: {ho_ten}")
print(f"Tien phai tra la: {tong_tien}")