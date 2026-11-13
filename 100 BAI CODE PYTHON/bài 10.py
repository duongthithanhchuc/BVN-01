# Viết chương trình nhập vào số học sinh của 1 lớp (HS) và số táo trong rổ (T). Hãy chia đều số táo cho tất cả học sinh trong lớp, mỗi bạn sẽ được bao nhiêu quả táo? Còn dư lại bao nhiêu quả?

hs, t = map(int, input().split())

moi_ban = t // hs
con_du = t % hs

print(moi_ban, con_du)