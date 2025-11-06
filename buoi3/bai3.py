s = input("Nhap doan van ban: ")
t = ""
for ch in s.lower():
    if ch.isalpha() or ch == " ":
        t += ch
w = t.split()
print("Tat ca tu: ", w)
u = []
for x in w:
    if x not in u:
        u.append(x)
print("Tu duy nhat: ", u)
c = []
for x in u:
    dem = w.count(x)
    c.append(dem)
max_count = max(c)
for i in range(len(u)):
    if c[i] == max_count:
        print("Tu xuat hien nhieu nhat: ", u[i], "-", c[i], "lan")
max_len = len(max(u, key=len))
for x in u:
    if len(x) == max_len:
        print("Tu dai nhat:", x, "-", max_len, "ky tu")
tong = 0
for x in w:
    tong += len(x)
print("Tong ky tu cua tat ca tu: ", tong)
b = u[:]
sx = []
while b:
    m = b[0]
    for x in b:
        if len(x) > len(m):
            m = x
    sx.append(m)
    b.remove(m)
print("Sap xep giam dan theo do dai: ", sx)