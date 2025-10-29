n = int(input("n= "))
dem = 0
for i in range(2, n):
    if i * i < n:
        dem += 1
print(dem)
