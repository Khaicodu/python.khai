# Bài 11 hướng đối tuợng
class nhanVien:
    def __init__(self,hoten,tuoi,luong):
        self.hoten = hoten
        self.tuoi = tuoi
        self.luong = luong
def nhapthongtin(n):
    danhsachNV = []
    for i in range(n):
        print(f"Nhập thông tin cho nhân viên thứ {i+1}:")
        hoten = input("Họ và tên: ")
        tuoi = int(input("Tuổi: "))
        luong = float(input("Lương: "))
        nv = nhanVien(hoten, tuoi, luong)
        danhsachNV.append(nv)
    return danhsachNV
def sapxepGiam(danhsach):
    return sorted(danhsach, key=lambda nv: nv.tuoi, reverse=True)

def ghiflieNV(danhsachNV,NhanVien):
    with open(NhanVien, 'w',encoding='utf-8') as f:
        for nv in danhsachNV:
            f.write(f"Họ và tên: {nv.hoten}\n")
            f.write(f"Tuổi: {nv.tuoi}\n")
            f.write(f"Lương: {nv.luong} vnđ\n\n")
    print("Thông tin đã được ghi vào file NhanVien.txt")
def dpcfileNV(taptin):
    ds = []
    with open(taptin, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                key, value = line.strip().split(': ')
                if key == "Họ và tên":
                    hoten = value
                elif key == "Tuổi":
                    tuoi = int(value)
                elif key == "Lương":
                    luong = float(value.split()[0])
                    nv = nhanVien(hoten, tuoi, luong)
                    ds.append(nv)
    return ds
soluong = int(input("Nhập số lượng nhân viên: "))
danhsachNV = nhapthongtin(soluong)
print("\nThông tin các nhân viên:")
danhsachSX = sapxepGiam(danhsachNV)
for i, nv in enumerate(danhsachSX):
    print(f"Nhân viên {i+1}:")
    print(f"Họ và tên: {nv.hoten}")
    print(f"Tuổi: {nv.tuoi}")
    print(f"Lương: {nv.luong} vnđ\n")
ghiflieNV(danhsachNV, "NhanVien.txt")
#Đọc file
danhsachNVfile = dpcfileNV("NhanVien.txt")
print("\nDanh sách nhân viên từ tập tin:")
for i, nv in enumerate(danhsachNVfile):
    print(f"Nhân viên {i+1}:")
    print(f"Họ và tên: {nv.hoten}")
    print(f"Tuổi: {nv.tuoi}")
    print(f"Lương: {nv.luong} vnđ\n")
