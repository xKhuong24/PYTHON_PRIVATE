tong = 0
dem = 0
while True:
    ten = input("Nhập tên món: ")
    if ten == "x" or ten == "X":
        break
    elif ten == "skip":
        continue
    elif ten == "pass":
        pass
    else:
        try:
            gia = int(input("Nhập giá tiền: "))
            tong += gia
            dem += 1
        except:
            print("Giá tiền không hợp lệ, bỏ qua món này")
            continue
print("Tổng số món:", dem)
print("Tổng tiền:", tong)
if tong > 200000:
    giam = tong * 0.1
    print("Giảm giá 10%:", int(giam))
    print("Tổng sau giảm:", int(tong-giam))
