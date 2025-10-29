x = int(input("x = ")) 
n = int(input("n = "))
e = 1   # Tính e
t = 1
for i in range(1, n+1):
    t *= x/i
    e += t
S = 1   # Tính S
t = 1
for i in range(1, n+1):
    t /= i
    S += t
print("e^x =", e)
print("S =", S)
