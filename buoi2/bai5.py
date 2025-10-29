while True:
    n = int(input("Nhập ngày sinh: "))
    t = int(input("Nhập tháng sinh: "))
    chd = ""
    if (t == 3 and 21 <= n <= 31) or (t == 4 and 1 <= n <= 19):
        chd = "Bạch Dương"
    elif (t == 4 and 20 <= n <= 30) or (t == 5 and 1 <= n <= 20):
        chd = "Kim Ngưu"
    elif (t == 5 and 21 <= n <= 31) or (t == 6 and 1 <= n <= 20):
        chd = "Song Tử"
    elif (t == 6 and 21 <= n <= 30) or (t == 7 and 1 <= n <= 22):
        chd = "Cự Giải"
    elif (t == 7 and 23 <= n <= 31) or (t == 8 and 1 <= n <= 22):
        chd = "Sư Tử"
    elif (t == 8 and 23 <= n <= 31) or (t == 9 and 1 <= n <= 22):
        chd = "Xử Nữ"
    elif (t == 9 and 23 <= n <= 30) or (t == 10 and 1 <= n <= 22):
        chd = "Thiên Bình"
    elif (t == 10 and 23 <= n <= 31) or (t == 11 and 1 <= n <= 21):
        chd = "Bọ Cạp"
    elif (t == 11 and 22 <= n <= 30) or (t == 12 and 1 <= n <= 21):
        chd = "Nhân Mã"
    elif (t == 12 and 22 <= n <= 31) or (t == 1 and 1 <= n <= 19):
        chd = "Ma Kết"
    elif (t == 1 and 20 <= n <= 31) or (t == 2 and 1 <= n <= 18):
        chd = "Bảo Bình"
    elif (t == 2 and 19 <= n <= 29) or (t == 3 and 1 <= n <= 20):
        chd = "Song Ngư"
    else:
        chd = "Ngày hoặc tháng không hợp lệ"

    print("Cung hoàng đạo của bạn là:", chd)

    tl = input("Bạn có muốn tiếp tục không?(y/n): ")
    if tl == "n":
        print("Chương trình kết thúc")
        break
