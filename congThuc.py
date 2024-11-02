# Code để tạo cửa sổ
import tkinter as tk
from tkinter import ttk 
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

        self.lblCongThuc = tk.Label(self.root, text='Công thức')
        self.lblCongThuc.place(x=self.x,y=self.y)
        
        self.n = tk.StringVar()
        CongThuc = ttk.Combobox(self.root, width = 27, textvariable = self.n)
        CongThuc.place(x=self.x, y=self.y+20) 
        CongThuc['values'] = ('Phương trình bậc 1',
                              'Phương trình bậc 2',
                              'Tìm số đối',
                              'Kích thước hình tròn',
                              'Kích thước hình vuông',
                              'Kích thước hình tam giác')
        
        self.btnTim = tk.Button(self.root, text='Tra cứu', command=self.ThongTin)
        self.btnTim.place(x=self.x+200, y=self.y+100)

    def ThongTin(self):
        if not self.n.get():
            messagebox.showwarning('Cảnh báo','Hãy chọn thông tin bạn muốn tra cứu')
        
        if self.n.get() == 'Phương trình bậc 1':
            messagebox.showinfo('Công thức','Công thức là: -b/a')
        elif self.n.get() == 'Phương trình bậc 2':
            KQ1 = 'Δ < 0 => phương trình vô nghiệm'
            KQ2 = 'Δ = 0 => phương trình có nghiệm kép: x1 = x2 = -b/2a'
            KQ3 = 'Δ > 0 => phương trình có hai nghiệm phân biệt: x1 = (-b + √Δ)/ 2*a và x2 = (-b - √Δ)/ 2*a'
            messagebox.showinfo('Công thức','Hướng dẫn giải: \n Bước 1: Tính Δ = 2*b-4*a*c \n Bước 2: So sánh Δ với 0 \n'+ str(KQ1) + '\n'+ str(KQ2) +'\n'+ str(KQ2))
        elif self.n.get() == 'Tìm số đối':
            messagebox.showinfo('Công thức','Công thức là: x-x*2')
        elif self.n.get() == 'Kích thước hình tròn':
            messagebox.showinfo('Công thức',' Chu vi: r*2*pi hoặc d*3,14 \n Diện tích: r*r*3,14')
        elif self.n.get() == 'Kích thước hình vuông':
            messagebox.showinfo('Công thước',' Chu vi: a*4 \n Diện tích: a*a')
        else:
            messagebox.showinfo('Công thức', 'Chu vi: a+b+c \n Diện tích: a*h/2 hoặc (√3/4)*a^2(đối với tam giác đều)')

        







# Chạy ứng dụng
if __name__=='__main__':
    # Tạo cửa sổ chính
    root = tk.Tk()
    # Khởi tạo đối tượng MyProject với cửa sổ chính
    app = MyProject(root)
    # Cho người dùng điều khiển cửa sổ
    root.mainloop()