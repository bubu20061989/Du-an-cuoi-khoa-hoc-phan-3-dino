import tkinter as tk
class MyProject:
    def __init__(self, root):
        # Thiết lập cửa sổ màn hình
        self.root = root
        # Thiết lập tiêu đề cho cửa sổ
        self.root.title('Ứng dụng Tkinter OOP')
        # Thiết lập kích thước của cửa sổ
        self.root.geometry('170x150')

        # Định nghĩa vị trí
        self.x = 15
        self.y = 10

        #label - lbl
        #entry - ety
        #Button - btn
        self.lblUsername = tk.Label(self.root, text="Username")
        # Đặt vị trí cho lblUsername
        self.lblUsername.place(x=self.x, y=self.y)
        self.etyUsername = tk.Entry(self.root)
        self.etyUsername.place(x=self.x, y=self.y + 20)
        
        self.lblPassword = tk.Label(self.root, text='Password')
        self.lblPassword.place(x=self.x, y=self.y + 40)
        self.etyPassword = tk.Entry(self.root)
        self.etyPassword.place(x=self.x, y=self.y + 60)

        self.btnLogin = tk.Button(self.root, text = 'Login')
        self.btnLogin.place(x=self.x, y=self.y+ 100)



# Chạy ứng dụng
if __name__=='__main__':
    # Tạo cửa sổ chính
    root = tk.Tk()
    # Khởi tạo đối tượng MyProject với cửa sổ chính
    app = MyProject(root)
    # Cho người dùng điều khiển cửa sổ
    root.mainloop()
