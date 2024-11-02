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
        self.width = 50

        self.lblNhapX = tk.Label(self.root, text='Nhập X')
        self.lblNhapX.place(x=self.x, y=self.y)
        self.etyNhapX = tk.Entry(self.root, width=self.width)
        self.etyNhapX.place(x=self.x, y=self.y+20)

        self.btnLogin = tk.Button(self.root, text = 'Tìm', command=self.ketQua)
        self.btnLogin.place(x=self.x + 200, y=self.y + 60)

    def ketQua(self): 
        x = float(self.etyNhapX.get())
        if not self.etyNhapX.get():
            messagebox.showerror('Thông Báo', 'Bạn chưa nhập đầy đủ')
        else:
            messagebox.showinfo('Kết quả', x-x*2)
        
  



# Chạy ứng dụng
if __name__=='__main__':
    # Tạo cửa sổ chính
    root = tk.Tk()
    # Khởi tạo đối tượng MyProject với cửa sổ chính
    app = MyProject(root)
    # Cho người dùng điều khiển cửa sổ
    root.mainloop()