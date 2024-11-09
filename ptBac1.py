import tkinter as tk
from tkinter import messagebox

class PTB1:
    def __init__(self, root):
        # Thiết lập cửa sổ màn hình
        self.root = root
        # self.root.title('Ứng dụng Tkinter OOP')
        # self.root.geometry('400x300')
        
        # Khởi tạo content_frame để tránh lỗi AttributeError
        self.content_frame = tk.Frame(self.root)
        self.content_frame.place(x=0, y=0, width=400, height=300)

        self.x = 10
        self.y = 10
        self.width = 30

        self.lblNhapA = tk.Label(self.root, text='Nhập a')
        self.lblNhapA.place(x=self.x, y=self.y)
        self.etyNhapA = tk.Entry(self.root, width=self.width)
        self.etyNhapA.place(x=self.x, y=self.y + 20)

        self.lblNhapB = tk.Label(self.root, text='Nhập b')
        self.lblNhapB.place(x=self.x, y=self.y + 40)
        self.etyNhapB = tk.Entry(self.root, width=self.width)
        self.etyNhapB.place(x=self.x, y=self.y + 60)

        self.btnTinh = tk.Button(self.root, text='Tính', command=self.ketQua)
        self.btnTinh.place(x=self.x + 200, y=self.y + 100)

    def ketQua(self):
        if not self.etyNhapA.get() or not self.etyNhapB.get():
            messagebox.showerror('Thông Báo', 'Bạn chưa nhập đầy đủ')
            return

        try:
            a = float(self.etyNhapA.get())
            b = float(self.etyNhapB.get())
        except ValueError:
            messagebox.showerror('Báo lỗi', 'Vui lòng nhập số hợp lệ cho a và b')
            return

        if a == 0:
            messagebox.showerror('Báo lỗi', 'Hãy nhập a khác 0')
        else:
            phepTinh = -b / a
            ketQua = f'x = {phepTinh:.2f}'
            messagebox.showinfo('Kết quả', ketQua)

    def chuViDienTich(self):
        # Xóa tất cả widget trong content_frame nếu có
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        # Thêm nội dung mới vào content_frame ở đây nếu cần

# Chạy ứng dụng
if __name__ == '__main__':
    root = tk.Tk()
    app = PTB1(root)
    root.mainloop()
