#Khai bao, dau vao
a= int(input("Nhap a = "))
b= int(input("Nhap b = "))
#Dau ra
print(f"{a}+{b} = {a+b}")
print(f"{a}-{b} = {a-b}")
print(f"{a}*{b} = {a*b}")
print(f"{a}:{b} = {a//b}")
print(f"{a} mu {b} = {a**b}")
print(f"{a}:{b} = {a//b} du {a%b}")
if (a>b):                           # so sanh
    print(f"{a} > {b}")
elif (b>a):
    print(f"{b} > {a}")
else :
    print(f"{a} = {b}")
print(bool(a and b))                #tra ve true neu ca hai khac 0
print(bool(a or b))                 #tra ve true 1 trong 2 khac 0
print(bool(a ^ b))                  #True neu a khac b
print(not (a == b))    
print(f"{a} dich phai 5 bit = {a >> 5}")
print(f"{a} dich trai 6 bit = {a << 6}")
bit = bin(a)[2:]                    #Chuyen sang nghi phan
kq = bit[::-1]
print(f"He cs2 dao nguoc {a} la {kq}")