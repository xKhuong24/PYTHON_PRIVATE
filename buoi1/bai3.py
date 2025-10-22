#Khai bao
a = "Chao mung den CLB Tin Hoc HIT"
print(a)
b = "CLB Tin Hoc HIT truc thuoc Khoa CNTT"
print(b + " 10 diem") 
#In chu in hoa
for i in b:
    if i.isupper():
        print(i, end=" ")
print()
#In chu thuong
for i in b:
    if i.islower():
        print(i, end=" ")
print()
if ("CNTT" in b):
    print("Yes")
else:
    print("No")
c = ""
for i in b:
    if i.isupper():
        c += i.lower()
    elif i.islower():
        c += i.upper()
    else:
        c += i
print(c)
