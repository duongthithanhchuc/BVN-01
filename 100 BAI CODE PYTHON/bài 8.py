# Viết chương trình tính bán kính $R$ của đường tròn ngoại tiếp tam giác có ba cạnh $a, b, c$ là các số nguyên theo công thức:$$R = \frac{abc}{4S}$$ với $S$ là diện tích tam giác ($3$ số $a, b, c$ bảo đảm là $3$ cạnh của một tam giác).   
# Dữ liệu vào: Một dòng có $3$ số nguyên cách nhau bởi dấu cách theo thứ tự là $a, b$ và $c$.   
# Dữ liệu ra: Là $R$ làm tròn đến 3 chữ số thập phân.  
import math
a, b, c = map(int, input().split())
p = ( a + b + c)/ 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
r = ( a * b * c)/(4 * s)
print(f"{r:.3f}")