
import tkinter as tk
from tkinter import messagebox
class MyProject:
    def __init__(self, root):
        # Thiết lập cửa sổ màn hình
        self.x = 15
        self.y = 10
        self.width = 370
        self.root = root
        # Thiết lập tiêu đề cho cửa sổ
        self.root.title('Ứng dụng Tkinter OOP')
        # Thiết lập kích thước của cửa sổ
        self.root.geometry('400x300')
        self.lblspeed=tk.Label(self.root,text="Speed(v)")
        self.lbltime=tk.Label(self.root,text="Time(t)")
        self.lbldisplacement=tk.Label(self.root,text="Displacemant(s)")
        self.btntinh=tk.Button(self.root,text="Tính",command=self.Caculate)
        self.lblexplanation=tk.Label(self.root,text="Speed=km/h\n Time=hour \n S=km")


        self.etyspeed=tk.Entry(self.root,text="Speed(v)")
        self.etytime=tk.Entry(self.root,text="Time(t)")
        self.etydisplacement=tk.Entry(self.root,text="Displacemant(s)")


        self.lbldisplacement.place(x=self.x   ,y=self.y)
        self.etydisplacement.place(x=self.x   ,y=self.y+20, width=self.width)
        self.lblspeed.place(x=self.x   ,y=self.y+40)
        self.etyspeed.place(x=self.x   ,y=self.y+60, width=self.width)
        self.lbltime.place(x=self.x   ,y=self.y+80)
        self.etytime.place(x=self.x   ,y=self.y+100, width=self.width)
        self.btntinh.place(x=self.x +200  ,y=self.y+160, width=self.width-240)
        self.lblexplanation.place(x=self.x +240  ,y=self.y+200,)


    def Caculate(self):

        if not  self.etydisplacement.get():
            v=float(self.etyspeed.get())
            t=float(self.etytime.get())
            if  v<0 or t<0:
                messagebox.showerror('ERROR',"S,V,T must be greater than 0" )
            else:
                ketquaS=t*v
                KetQuaCuoiCung = 'S='+ str(ketquaS)
                messagebox.showinfo('Info',KetQuaCuoiCung )
            

        if not  self.etyspeed.get():
            s=float(self.etydisplacement.get())
            t=float(self.etytime.get())
            if  s<0 or t<0:
                messagebox.showerror('ERROR',"S,V,T must be greater than 0" )
            else:
                ketquaV=s/t
                KetQuaCuoiCung = 'V='+ str(ketquaV)
                messagebox.showinfo('Info',KetQuaCuoiCung )
            

        if not  self.etytime.get():              
            s=float(self.etydisplacement.get())
            v=float(self.etyspeed.get())
            if  v<0 or s<0:
                messagebox.showerror('ERROR',"S,V,T must be greater than 0" )
            else:
                ketquaT=s/v
                KetQuaCuoiCung = 'T='+ str(ketquaT)
                messagebox.showinfo('Info',KetQuaCuoiCung )


        if not self.etyspeed.get() and not self.etydisplacement.get():
                messagebox.showerror('ERROR',"S,V must fill " )
        if not self.etyspeed.get() and not self.etytime.get():
                messagebox.showerror('ERROR',"V,T must fill " )
        if not self.etytime.get() and not self.etydisplacement.get():
                messagebox.showerror('ERROR',"S,T must fill " )

        
# Chạy ứng dụng
if __name__=='__main__':
    # Tạo cửa sổ chính
    root = tk.Tk()
    # Khởi tạo đối tượng MyProject với cửa sổ chính
    app = MyProject(root)
    # Cho người dùng điều khiển cửa sổ
    root.mainloop()
