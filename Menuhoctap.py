# Code để tạo cửa sổ
import tkinter as tk
from tkinter import Menu
class MyProject:
    def __init__(self, root):
        # Thiết lập cửa sổ màn hình
        self.root = root
        # Thiết lập tiêu đề cho cửa sổ
        self.root.title('Ứng dụng Tkinter OOP')
        # Thiết lập kích thước của cửa sổ
        self.root.geometry('400x300')

# Tạo Menu bar
        self.menu = Menu(root)
        self.root.config(menu=self.menu)
        
        # Tạo File Menu
        self.fileMenu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='Toán', menu=self.fileMenu)
        self.fileMenu.add_cascade(label='Toán 6' , menu=self.fileMenu)

    def Toan6():
        pass




# Chạy ứng dụng
if __name__=='__main__':
    # Tạo cửa sổ chính
    root = tk.Tk()
    # Khởi tạo đối tượng MyProject với cửa sổ chính
    app = MyProject(root)
    # Cho người dùng điều khiển cửa sổ
    root.mainloop()