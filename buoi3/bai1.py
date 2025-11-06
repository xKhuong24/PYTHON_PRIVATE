n = int(input("Nhap so phan tu : "))
a = []
for i in range(n):
    x = int(input(f"Nhap phan tu {i+1}: "))
    a.append(x)
print("Mang ban dau: ", a)
b = []
seen = set()
for x in a:
    if x not in seen:
        seen.add(x)
        b.append(x)
print("Bo trung lap :", b)
c = [x**2 if x % 2 == 0 else x**3 for x in b]
print("Bien doi:", c)
d = a[::2]
if d:
    tb = sum(d) / len(d)
    print("TBC vi tri chan :", tb)
else:
    print("Khong co")
e = []
tmp = b[:]
while tmp:
    m = tmp[0]
    for x in tmp:
        if abs(x) < abs(m):
            m = x
    e.append(m)
    tmp.remove(m)
print("Sap xep theo abs tang dan: ", e)