import tkinter as tk
from tkinter import messagebox

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


        self.lblBankinh = tk.Label(self.root, text = 'Bán kính ◯')
        self.lblBankinh.place (x=self.x, y = self.y )
        self.etyBankinh = tk.Entry(self.root, width= self.width)
        self.etyBankinh.place (x = self.x, y = self.y + 20)


        self.btnTinhChuViHT = tk.Button (self.root, text='Chu Vi', command= self.ChucNang1)
        self.btnTinhChuViHT.place (x=self.x + 200, y=self.y + 100)
        self.btnTinhDienTichHT = tk.Button (self.root, text='Dien Tich', command= self.ChucNang2)
        self.btnTinhDienTichHT.place (x=self.x + 250, y=self.y + 100)

    def ChucNang1(self):
        Bankinh = float(self.etyBankinh.get())

        if  Bankinh =='':
            messagebox.showerror('Error','You have not typed the length or the width')
        else:
            messagebox.showinfo('Kết quả ',(Bankinh*2*3.141592653589793238462643383279502884197169399375105821))
    
    def ChucNang2(self):
        Bankinh = float(self.etyBankinh.get())

        if Bankinh =='':
            messagebox.showerror('Error', 'You have not typed the length or the width')
        else:
            messagebox.showinfo('Kết quả',Bankinh*Bankinh*3.141592653589793238462643383279502884197169399375105821)
        

    







        # Chạy ứng dụng
if __name__=='__main__':
    # Tạo cửa sổ chính
    root = tk.Tk()
    # Khởi tạo đối tượng MyProject với cửa sổ chính
    app = MyProject(root)
    # Cho người dùng điều khiển cửa sổ
    root.mainloop()
