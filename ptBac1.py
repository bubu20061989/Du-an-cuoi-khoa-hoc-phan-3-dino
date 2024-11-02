# Code để tạo cửa sổ
import tkinter as tk
from tkinter import messagebox
class MyProject:
    def __init__(self, root):
        # Thiết lập cửa sổ màn hình
        self.root = root
        # Thiết lập tiêu đề cho cửa sổ
        self.root.title('Ứng dụng Tkinter OOP')
        # Thiết lập kích thước của cửa sổ
        self.root.geometry('400x300')

        self.x = 10
        self.y = 10
        self.width = 60

        self.lblNhapA = tk.Label(self.root, text='Nhập a')
        self.lblNhapA.place(x=self.x, y=self.y)
        self.etyNhapA = tk.Entry(self.root, width=self.width)
        self.etyNhapA.place(x=self.x, y=self.y+20)

        self.lblNhapB = tk.Label(self.root, text='Nhập b')
        self.lblNhapB.place(x=self.x, y=self.y+40)
        self.etyNhapB = tk.Entry(self.root, width=self.width)
        self.etyNhapB.place(x=self.x, y=self.y+60)

        self.btnTinh = tk.Button(self.root, text='Tính', command=self.ketQua)
        self.btnTinh.place(x=self.x + 200, y=self.y+100)

    def ketQua(self):
        if not self.etyNhapA.get() or not self.etyNhapB.get():
            messagebox.showerror('Thông Báo', 'Bạn chưa nhập đầy đủ')
        
        a = float(self.etyNhapA.get())
        b = float(self.etyNhapB.get())

        if a == 0:
            messagebox.showerror('Báo lỗi', 'Hãy nhập a khác 0')
        else:
            phepTinh = -b/a
            ketQua = 'x =' + str(phepTinh)
            messagebox.showinfo('Kết quả', ketQua)





# Chạy ứng dụng
if __name__=='__main__':
    # Tạo cửa sổ chính
    root = tk.Tk()
    # Khởi tạo đối tượng MyProject với cửa sổ chính
    app = MyProject(root)
    # Cho người dùng điều khiển cửa sổ
    root.mainloop()