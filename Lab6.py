from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("400x200+10+20")
window.title("Grade Calculator")


class MyWindow:
    def __init__(self, window):
        self.lbl0 = Label(window, text="Semestral Grade Calculator:")
        self.lbl0.grid(row=0, column=0)
        self.lbl1 = Label(window, text="Enter Prelim Grade:")
        self.lbl1.grid(row=1, column=0)
        self.txtfld2 = Entry(window, bd=3, justify="center")
        self.txtfld2.grid(row=1, column=1, padx=2)
        self.lbl3 = Label(window, text="Enter Midterm Grade")
        self.lbl3.grid(row=2, column=0)
        self.txtfld3 = Entry(window, bd=3, justify="center")
        self.txtfld3.grid(row=2, column=1, padx=2)
        self.lbl3 = Label(window, text="Enter Finals Grade")
        self.lbl3.grid(row=3, column=0)
        self.txtfld4 = Entry(window, bd=3, justify="center")
        self.txtfld4.grid(row=3, column=1, padx=2)
        self.btn1 = Button(window, text="Compute", command=self.compute)
        self.btn1.grid(row=4, column=0, padx=2)
        self.lbl5 = Label(window, text="Result:")
        self.lbl5.grid(row=6, column=0)
        self.txtfld6 = Entry(window, bd=3)
        self.txtfld6.grid(row=6, column=1)

    def compute(self):
        self.txtfld6.delete(0, 'end')
        num1 = float(self.txtfld2.get())
        num2 = float(self.txtfld3.get())
        num3 = float(self.txtfld4.get())
        answer = round((num1 + num2 + num3) / 3, 2)
        self.txtfld6.insert(END, answer)


mywin = MyWindow(window)

window.mainloop()