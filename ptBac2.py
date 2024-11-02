# Code để tạo cửa sổ
import tkinter as tk
from tkinter import messagebox
import math
class MyProject:
    def __init__(self, root):
        # Thiết lập cửa sổ màn hình
        self.root = root
        # Thiết lập tiêu đề cho cửa sổ
        self.root.title('Phương trình bậc 2')
        # Thiết lập kích thước của cửa sổ
        self.root.geometry('400x300')

        self.x = 10
        self.y = 10
        self.width = 60
        
        self.lblNhapA = tk.Label(self.root, text='Nhập a')
        self.lblNhapA.place(x=self.x, y=self.y)
        self.etyNhapA = tk.Entry(self.root, width=self.width)
        self.etyNhapA.place(x=self.x, y=self.y + 20)

        self.lblNhapB = tk.Label(self.root, text='Nhập b')
        self.lblNhapB.place(x=self.x, y=self.y + 40)
        self.etyNhapB = tk.Entry(self.root, width=self.width)
        self.etyNhapB.place(x=self.x, y=self.y + 60)

        self.lblNhapC = tk.Label(self.root, text='Nhập c')
        self.lblNhapC.place(x=self.x, y=self.y + 80)
        self.etyNhapC = tk.Entry(self.root, width=self.width)
        self.etyNhapC.place(x=self.x, y=self.y + 100)

        self.btnLogin = tk.Button(self.root, text = 'Tính', command=self.ketQua)
        self.btnLogin.place(x=self.x + 200, y=self.y + 140)

    def ketQua(self):
        if not self.etyNhapA.get() or not self.etyNhapB.get() or not self.etyNhapC.get():
            messagebox.showerror('Thông Báo', 'Bạn chưa nhập đầy đủ')

        a = float(self.etyNhapA.get())
        b = float(self.etyNhapB.get())
        c = float(self.etyNhapC.get())

        delta=b*b-4*a*c
        if delta < 0:
            messagebox.showinfo('Kết quả', 'Phương trình vô nghiệm')
        elif delta == 0:
            nghiem = -b/2*a
            messagebox.showinfo('Kết quả', 'Phương trình có nghiệm kép x1 = x2 =' + str(nghiem))
        else:
            nghiem1 = (-b + math.sqrt(delta))/2*a
            nghiem2 = (-b - math.sqrt(delta))/2*a
            ketQua = 'Phương Trình có 2 nghiệm phân biệt \n x = '+ str(nghiem1) +'\n y = '+ str(nghiem2)
            messagebox.showinfo('Kết quả', ketQua)


    






# Chạy ứng dụng
if __name__=='__main__':
    # Tạo cửa sổ chính
    root = tk.Tk()
    # Khởi tạo đối tượng MyProject với cửa sổ chính
    app = MyProject(root)
    # Cho người dùng điều khiển cửa sổ
    root.mainloop()