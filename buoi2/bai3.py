n = int(input())

for i in range(1, n+1):
    ten = input()
    d1 = int(input())
    d2 = int(input())
    td = d1 + d2
    if td >= 200:
        xl = "Xuất sắc"
    elif td >= 150:
        xl = "Giỏi"
    elif td >= 100:
        xl = "Khá"
    else:
        xl = "Yếu"

    print(i, ten, td, xl)
