import tkinter as tk
from tkinter import messagebox
import math

class MyProject:
    def __init__(self, root):
        # Thiết lập cửa sổ màn hình
        self.root = root
        # Thiết lập tiêu đề cho cửa sổ
        self.root.title('Chương trình Toán học')
        # Thiết lập kích thước của cửa sổ
        self.root.geometry('400x300')

        self.x = 10
        self.y = 10
        self.width = 63

        self.lblCạnh = tk.Label(self.root, text = 'Cạnh Đáy △')
        self.lblCạnh.place (x=self.x, y = self.y )
        self.etyCạnh = tk.Entry(self.root, width= self.width)
        self.etyCạnh.place (x = self.x, y = self.y +20)
        
        self.btnTinhChuViTG = tk.Button (self.root, text='Chu Vi', command= self.ChucNang1)
        self.btnTinhChuViTG.place (x=self.x + 200, y=self.y + 100)
        self.btnTinhDienTichTG = tk.Button (self.root, text='Dien Tich', command= self.ChucNang2)
        self.btnTinhDienTichTG.place (x=self.x + 250, y=self.y + 100)

    def ChucNang1(self):
        Canh = float(self.etyCạnh.get())

        if Canh =='':
            messagebox.showerror('Error','You have not typed the length or the width')
        elif Canh <=0:
            messagebox.showerror('Error', 'The length or the Width must be >0')
        else:
            messagebox.showinfo('kết quả ',Canh*3)
    
    def ChucNang2(self):
        Canh = float(self.etyCạnh.get())

        if Canh =='' :
            messagebox.showerror('Error', 'You have not typed the length or the width')
        elif Canh <=0:
            messagebox.showerror('Error', 'The length or the Width must be >0')
        else:
            messagebox.showinfo('Kết quả', math.sqrt(3)/4*Canh*Canh)








        # Chạy ứng dụng
if __name__=='__main__':
    # Tạo cửa sổ chính
    root = tk.Tk()
    # Khởi tạo đối tượng MyProject với cửa sổ chính
    app = MyProject(root)
    # Cho người dùng điều khiển cửa sổ
    root.mainloop()
