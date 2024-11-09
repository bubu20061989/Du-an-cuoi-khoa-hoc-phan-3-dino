# Code để tạo cửa sổ
import tkinter as tk
from tkinter import Menu
import ptBac1
class MyProject:
    def __init__(self, root):
        # Thiết lập cửa sổ màn hình
        self.root = root
        # Thiết lập tiêu đề cho cửa sổ
        self.root.title('Ứng dụng Tkinter OOP')
        # Thiết lập kích thước của cửa sổ
        self.root.geometry('400x300')

# Tạo Menu bar
        self.menuBar = Menu(root)
        self.root.config(menu=self.menuBar)
        
# Tạo monToan trong menuBar
        self.monToan = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label='Toán', menu=self.monToan)

# Tạo Toán 6 trong monToan
        self.toan6 = Menu(self.monToan, tearoff=0)
        self.monToan.add_cascade(label='Toán 6', menu=self.toan6)
    # Tạo thành phần chu vi, diện tích
        self.toan6.add_command(label='Chu vi và Diện tích', command=self.chuViDienTich)
    # Tạo thành phần tính toán cơ bản
        self.toan6.add_command(label='Tính toán cơ bản', command=self.tinhToanCoban)
    # Tạo thành phần tìm x,y,z
        self.toan6.add_command(label='Tìm x,y,z', command=self.timXYZ)
# Tạo toán nâng cao trong toán 6
        self.toanNangCao = Menu(self.monToan, tearoff=0)
        self.toan6.add_cascade(label='Toán nâng cao', menu=self.toanNangCao)
    # Tạo thành phần tính toán nâng cao
        self.toanNangCao.add_command(label="Tính toán nâng cao", command=self.tinhToanNangCao)
    # Tạo thành phần tìm số đối
        self.toanNangCao.add_command(label='Tìm số đối', command=self.timSoDoi)

# Tạo monLy trong menuBar
        self.monLy = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label='Lý', menu=self.monLy)
# Tạo Lý 6 trong monLy
        self.ly6 = Menu(self.monLy, tearoff=0)
        self.monLy.add_cascade(label='Lý 6', menu=self.ly6)
    # tạo thành phần cho Ly6
        self.ly6.add_command(label='Tìm S,V,T', command=self.timSVT)
        self.ly6.add_command(label='Tính m, P ', command=self.tinhMP)
        self.ly6.add_command(label='Tính độ biến dạng lò xo', command = self.tinhDBD)
        self.ly6.add_command(label='Tính cường độ trường hấp dẫn', command=self.tinhCuongDo)
        self.ly6.add_command(label='Chuyển đối đơn vị nhiệt độ', command=self.chuyenDoi)

# Tạo monHoa trong menuBar
        self.monHoa = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label='Hóa', menu=self.monHoa)
# tạo Hóa 8 trong monHoa
        self.hoa8 = Menu(self.menuBar, tearoff=0)
        self.monHoa.add_cascade(label='Hóa 8', menu=self.hoa8)
    # Tạo thành phần cho Hóa 8
        self.hoa8.add_command(label='Tính số mol', command=self.tinhSoMol)   
        self.hoa8.add_command(label='Tính nồng độ mol', command=self.tinhNongDoMol)
        self.hoa8.add_command(label='Tính khối lượng mol', command=self.tinhKLMol)
        self.hoa8.add_command(label='Tính tỉ khối', command=self.tinhTiKhoi)
        self.hoa8.add_command(label='Tính độ tan', command=self.tinhDoTan)    

     # Frame to hold the content
        self.content_frame = tk.Frame(self.root)
        self.content_frame.pack(fill=tk.BOTH, expand=True)


# Tạo hàm def cho thành phần thuộc monToan
    def chuViDienTich(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        # Load the attendance management interface
        app = ptBac1.PTB1(self.content_frame)   
    def tinhToanCoban(self):
        pass
    def timXYZ(self):
        pass
    def tinhToanNangCao(self):
        pass
    def timSoDoi(self):
        pass

# Tạo hàm def cho thành phần thuộc monLy
    def timSVT(self):
        pass
    def tinhMP(self):
        pass
    def tinhDBD(self):
        pass
    def tinhCuongDo(self):
        pass
    def chuyenDoi(self):
        pass

# Tạo hàm def cho thành phần monHoa
    def tinhSoMol(self):
        pass
    def tinhNongDoMol(self):
        pass
    def tinhKLMol(self):
        pass
    def tinhTiKhoi(self):
        pass
    def tinhDoTan(self):
        pass
 




# Chạy ứng dụng
if __name__=='__main__':
    # Tạo cửa sổ chính
    root = tk.Tk()
    # Khởi tạo đối tượng MyProject với cửa sổ chính
    app = MyProject(root)
    # Cho người dùng điều khiển cửa sổ
    root.mainloop()