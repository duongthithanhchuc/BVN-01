# Viết chương trình nhập vào 1 tháng và năm, cho biết tháng đó có bao nhiêu ngày (Năm nhuận là năm chia hết cho 400 hoặc chia hết cho 4 nhưng không chia hết cho 100). Dữ liệu vào Hai số nguyên tháng và năm cách nhau bởi dấu cách Dữ liệu ra Kết quả tháng đó có bao nhiêu ngày
a, b = map(int, input().split())
match a:
    case 1|3|5|7|10|11|12:
        print(31)
    case 4|6|9|11:
        print(30)
    case 2:
        if ( b % 4 == 0 and b % 100 != 0) or b % 400 == 0:
             print(29)
        else:
            print(28)