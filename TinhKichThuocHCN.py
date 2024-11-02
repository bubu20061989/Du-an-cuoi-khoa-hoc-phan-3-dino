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

        self.lblChieuDaiHCN = tk.Label(self.root, text = 'Chiều dài HCN')
        self.lblChieuDaiHCN.place (x = self.x, y= self.y)
        self.etyChieuDaiHCN = tk.Entry(self.root, width= self.width)
        self.etyChieuDaiHCN.place (x = self.x, y = self.y +20)

        self.lblChieuRongHCN = tk.Label(self.root, text = 'Chiều rộng HCN')
        self.lblChieuRongHCN.place (x=self.x, y = self.y + 40)
        self.etyChieuRongHCN = tk.Entry(self.root, width= self.width)
        self.etyChieuRongHCN.place (x = self.x, y = self.y + 60)



        self.btnTinhChuViHCN = tk.Button (self.root, text='Chu Vi', command= self.ChucNang1)
        self.btnTinhChuViHCN.place (x=self.x + 200, y=self.y + 100)
        self.btnTinhDienTichHCN = tk.Button (self.root, text='Dien Tich', command= self.ChucNang2)
        self.btnTinhDienTichHCN.place (x=self.x + 250, y=self.y + 100)

    def ChucNang1(self):
        ChieuDaiHCN = float(self.etyChieuDaiHCN.get())
        ChieuRongHCN = float(self.etyChieuRongHCN.get())

        if ChieuDaiHCN =='' or ChieuRongHCN =='':
            messagebox.showerror('Error','You have not typed the length or the width')
        else:
            messagebox.showinfo('kết quả ',(ChieuDaiHCN + ChieuRongHCN)*2)
    
    def ChucNang2(self):
        ChieuDaiHCN = float(self.etyChieuDaiHCN.get())
        ChieuRongHCN = float(self.etyChieuRongHCN.get())

        if ChieuDaiHCN =='' or ChieuRongHCN =='':
            messagebox.showerror('Error', 'You have not typed the length or the width')
        else:
            messagebox.showinfo('Kết quả', ChieuDaiHCN * ChieuRongHCN)
        

    







        # Chạy ứng dụng
if __name__=='__main__':
    # Tạo cửa sổ chính
    root = tk.Tk()
    # Khởi tạo đối tượng MyProject với cửa sổ chính
    app = MyProject(root)
    # Cho người dùng điều khiển cửa sổ
    root.mainloop()
