s = input("Nhap: ")
p = s.split(",")
a = []
for x in p:
    x = x.strip()
    if ":" in x:
        t = x.split(":")
        ten = t[0].strip()
        diem = float(t[1].strip())
        a.append((ten, diem))
n = []
for ten, diem in a:
    if ten not in n:
        n.append(ten)
tb = []
for ten in n:
    tong = 0
    dem = 0
    for t2, d2 in a:
        if t2 == ten:
            tong = tong + d2
            dem = dem + 1
    tb.append((ten, tong / dem))
max_diem = tb[0][1]
min_diem = tb[0][1]
for ten, diem in tb:
    if diem > max_diem:
        max_diem = diem
    if diem < min_diem:
        min_diem = diem
for ten, diem in tb:
    if diem == max_diem:
        print("Cao nhat: ", ten, "-", diem)
    if diem == min_diem:
        print("Thap nhat: ", ten, "-", diem)
b = tb[:]
sx = []
while b:
    m = b[0]
    for x in b:
        if x[1] > m[1]:
            m = x
    sx.append(m)
    b.remove(m)
print("Sap xep: ", sx)
