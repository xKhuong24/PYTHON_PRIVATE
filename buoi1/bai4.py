#Nhập tt
ten = input("Nhập tên: ")
tuoi = int(input("Nhập tuổi: "))
gioi_tinh = input("Nhập giới tính (Nam/Nữ): ")
ny = input("Bạn có người yêu chưa (Rồi/Chưa): ")
if (ny != "Rồi" and ny != "Chưa"):
    ny = "Chưa"
#In tt
print(f"Tên: {ten}")
print(f"Tuổi: {tuoi}")
print(f"Giới tính: {gioi_tinh}")
print(f"Tình trạng hôn nhân: {ny}")
if (gioi_tinh == "Nữ" and ny == "Chưa"):            #Ktra điệu kiện 
    print("+1")
else:
    print("-1")
