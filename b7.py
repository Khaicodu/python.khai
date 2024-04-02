print('BÀI 7')
# Từ điển điểm số môn học
A = {"Toán": 10, "Văn": 5, "Sử": 8, "Địa": 7, "Hoá": 6, "Sinh": 9}
print(A)

# In ra điểm lớn nhất
def diemLonNhat():
    return max(A.values())

# In ra môn và điểm có điểm lớn nhất
def monAndDiemcao():
    diem_cao_nhat = diemLonNhat()
    for mon, diem in A.items():
        if diem == diem_cao_nhat:
            return mon, diem

# In ra các môn và điểm số lẻ tương ứng
def monAndDiemle():
    return {mon: diem for mon, diem in A.items() if diem % 2 != 0}

# d) Tính trung bình tất cả các điểm
def diemTB():
    return sum(A.values()) / len(A)

# Tạo từ điển mới với các môn lớn hơn 6 điểm
def tuDienDiemlon6():
    return {mon: diem for mon, diem in A.items() if diem > 6}

# Đảo ngược từ điển A, key thành value và ngược lại.
def daoNguocTD():
    return {diem: mon for mon, diem in A.items()}

# Viết chương trình chính gọi các hàm trên và in ra kết quả
if __name__ == "__main__":
    print("Điểm lớn nhất:", diemLonNhat())
    mon, diem = monAndDiemcao()
    print(f"Môn và điểm cao nhất: {mon} với {diem} điểm")
    print("Môn và điểm số lẻ:", monAndDiemle())
    print("Điểm trung bình của tất cả môn:", diemTB())
    print("Từ điển mới với điểm lớn hơn 6:", tuDienDiemlon6())
    print("Từ điển đảo ngược:", daoNguocTD())
