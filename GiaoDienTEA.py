from tkinter import *
from tkinter import messagebox as mess
from datetime import datetime
from PIL import ImageTk, Image

class Drink:
    def __init__(self, id, name, size, price):
        self.id = id
        self.name = name
        self.size = size
        self.price = price

    def __str__(self,font_size=13):
        return f"{self.id.ljust(10)} - {self.name.rjust(15)}     -{self.size.rjust(10)}   - {self.price.rjust(10)} VND"

def get_datetime():
    current_time = str(datetime.now())
    current_time = current_time[0:16]
    return current_time

def append_to_file(drink):
    with open("abc.txt", "a", encoding="utf-8") as file:
        file.write(f"{drink.id},{drink.name},{drink.size},{drink.price}\n")

def add_to_list():
    # Lấy thông tin từ các ô nhập liệu
    id_value = id_entry.get()
    name_value = name_entry.get()
    size_value = size_entry.get()
    price_value = price_entry.get()

    # Kiểm tra xem các ô nhập liệu có trống hay không
    if id_value == "" or name_value == "" or size_value == "" or price_value == "":
        mess.showerror("Lỗi", "Vui lòng nhập đủ thông tin thức uống.")
    else:
        # Thêm thức uống vào danh sách và hiển thị trên listbox1
        drink = Drink(id_value, name_value, size_value, price_value)
        listbox1.insert(END, str(drink))

        # Lưu thông tin thức uống vào file
        append_to_file(drink)

        # Xóa nội dung trong các ô nhập liệu sau khi thêm vào danh sách
        id_entry.delete(0, END)
        name_entry.delete(0, END)
        size_entry.delete(0, END)
        price_entry.delete(0, END)

def read_from_file():
    # Xóa hết các mục có sẵn trong listbox1
    listbox1.delete(0, END)

    # Đọc thông tin từ tệp và hiển thị lên listbox1
    with open("abc.txt", "r",encoding='utf-8') as file:
        for line in file:
            data = line.strip().split(',')
            drink = Drink(data[0], data[1], data[2], data[3])
            listbox1.insert(END, str(drink))

def order_drink():
    # Đọc thông tin từ tệp trước khi hiển thị lên listbox1
    read_from_file()

def add_to_cart():
    selected_drink = listbox1.get(ACTIVE)
    cart_listbox.insert(END, selected_drink)

def calculate_total():
    total = 0
    for item in cart_listbox.get(0, END):
        price = int(item.split('-')[-1].strip().split(' ')[0])
        total += price
    mess.showinfo("Tổng Tiền", f"Tổng tiền là: {total} VND")
def reset_cart():
    cart_listbox.delete(0, END)
    mess.showinfo("Thông báo", "Giỏ hàng đã được đặt lại thành trống!")
def remove_from_cart():
    selected_index = cart_listbox.curselection()
    if selected_index:
        cart_listbox.delete(selected_index)

root = Tk()
root.title('Quản lý CHIDORI')
root.geometry("1220x600")  # Đặt kích thước cửa sổ
root.minsize(height=600, width=1220)

Label(root, text='ỨNG DỤNG QUẢN LÝ CHIDORI', fg='#ff4500', font=('cambria',16), width=100).grid(row=0, columnspan=8, padx=10, pady=10)

# Hiển thị thời gian hiện tại
lbdatetime = Label(root, text=get_datetime(), bd=4)
lbdatetime.grid(row=0, column=0, sticky="nw")

# Vùng nhập dữ liệu cho thức uống mới
f1 = Frame(root, relief=GROOVE, bd=2, padx=3, width=100, height=80)
f1.grid(row=1, column=0, columnspan=1, rowspan=3, sticky="w")
id_label = Label(f1, text='ID', pady=3, bd=3, fg='#ff4500')
id_label.grid(row=0, column=0, sticky=W)
name_label = Label(f1, text='Tên Thức uống', pady=3, bd=3, fg='#ff4500')
name_label.grid(row=1, column=0, sticky=W)
size_label = Label(f1, text='Size', pady=3, bd=3, fg='#ff4500')
size_label.grid(row=2, column=0, sticky=W)
price_label = Label(f1, text='Giá', pady=3, bd=3, fg='#ff4500')
price_label.grid(row=3, column=0, sticky=W)
id_entry = Entry(f1, bd=2)
id_entry.grid(row=0, column=1, sticky=W)
name_entry = Entry(f1, bd=2)
name_entry.grid(row=1, column=1, sticky=W)
size_entry = Entry(f1, bd=2)
size_entry.grid(row=2, column=1, sticky=W)
price_entry = Entry(f1, bd=2)
price_entry.grid(row=3, column=1, sticky=W)

# Nút "Thêm vào danh sách"
add_to_list_button = Button(root, text="Thêm vào danh sách", font=('cambria',10), command=add_to_list, width=20, height=2, bg='#00BFFF', fg='black')
add_to_list_button.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Danh sách thức uống và nút "Oder Thức uống"
Label(root,text='MENU - CHIDORI TEA',fg='#ff4500',font=('cambria',13),width=20).grid(row=4,column=1, padx=10, pady=10)
# Tạo một Frame với màu cam và viền kích thước 10 pixel
orange_frame = Frame(root, bg="orange", bd=10)
orange_frame.grid(row=5, column=1, padx=10, pady=10)

# Tạo Listbox và đặt nó vào trong Frame màu cam
listbox1 = Listbox(orange_frame, width=100, height=20)
listbox1.pack()


order_button = Button(root, text="Oder Thức uống", font=('cambria',10), command=order_drink, width=20, height=2, bg='#00BFFF', fg='black')
order_button.grid(row=2, column=1, padx=5, pady=5, sticky="w")

# Khung cho giỏ hàng
cart_frame = Frame(root, bg="orange", bd=1)
cart_frame.grid(row=5, column=2, padx=5, pady=5,sticky="nw")

# Danh sách giỏ hàng
cart_label = Label(cart_frame, text='GIỎ HÀNG', font=('cambria',13), bg="orange")
cart_label.grid(row=0, column=0, padx=10, pady=10)

cart_listbox = Listbox(cart_frame, width=50, height=10)
cart_listbox.grid(row=1, column=0, padx=5, pady=5)


# Nút thêm vào giỏ hàng
add_to_cart_button = Button(root, text="Thêm vào giỏ hàng", font=('cambria',10), command=add_to_cart, width=20, height=2, bg='#00BFFF', fg='black')
add_to_cart_button.grid(row=4, column=2, padx=5, pady=5, sticky="w")

# Nút tính tổng tiền
calculate_total_button = Button(root, text="Tính Tổng Tiền", font=('cambria',10), command=calculate_total, width=20, height=2, bg='#00BFFF', fg='black')
calculate_total_button.grid(row=4, column=2, padx=5, pady=5, sticky="e")

# Load ảnh
reset_image = ImageTk.PhotoImage(Image.open("reload black.jpg"))

# reset
reset_button = Button(cart_frame, image=reset_image, command=reset_cart)
reset_button.grid(row=2, column=0, padx=5, pady=5, sticky="w")

#  xoá
remove_button = Button(cart_frame, text="Xoá", font=('cambria',10), command=remove_from_cart, width=10, height=2, bg='#FF6347', fg='black')
remove_button.grid(row=2, column=0, padx=5, pady=5, sticky="e")

# ảnh chidori
chidori = ImageTk.PhotoImage(Image.open("chidori.jpg"))
chidori_label = Label(root, image=chidori,width=220,height=400)
chidori_label.grid(row=5, column=0, padx=5)
# logo = ImageTk.PhotoImage(Image.open("logo.jpg"))
# logo_label = Label(root, image=logo,width=300,height=110)
# logo_label.grid(row=0, column=2)
root.mainloop()
