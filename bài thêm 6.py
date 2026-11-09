# Viết chương trình nhập một ký tự, kiểm tra xem ký tự đó là chữ cái hay chữ số.
ki_tu = input('Nhập vào một kí tự: ')
if ki_tu.isalpha():
    print(f"Kí tự {ki_tu} là chữ cái")
elif ki_tu.isdigit():
    print(f"Kí tự {ki_tu} là chữ số")
else:
    print(f"Kí tự {ki_tu} không là chữ cái, chữ số")
    