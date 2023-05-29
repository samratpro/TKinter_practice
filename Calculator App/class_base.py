from tkinter import *

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x270")
        self.title('Calculator')
        self.bg_color = '#CDCDCD'
        self.configure(bg=self.bg_color)

        # Widget
        self.frame = Frame(self, bg=self.bg_color)
        self.display = Entry(self.frame, borderwidth=3, width=30, font=15)
        self.sub_display = Entry(self.frame,borderwidth=3, width=8, font=('arial', 9))

        self.btn7 = Button(self.frame, text="7", width=8, font=10, command=lambda:self.btnclick(7))
        self.btn8 = Button(self.frame, text="8", width=8, font=10, command=lambda:self.btnclick(8))
        self.btn9 = Button(self.frame, text="9", width=8, font=10, command=lambda:self.btnclick(9))
        self.btn_pluse = Button(self.frame, text="+", width=8, font=10, command=self.pluse)

        self.btn4 = Button(self.frame, text="4", width=8, font=10, command=lambda:self.btnclick(4))
        self.btn5 = Button(self.frame, text="5", width=8, font=10, command=lambda:self.btnclick(5))
        self.btn6 = Button(self.frame, text="6", width=8, font=10, command=lambda:self.btnclick(6))
        self.btn_minus = Button(self.frame, text="-", width=8, font=10, command=self.minus)

        self.btn1 = Button(self.frame, text="1", width=8, font=10, command=lambda:self.btnclick(1))
        self.btn2 = Button(self.frame, text="2", width=8, font=10, command=lambda:self.btnclick(2))
        self.btn3 = Button(self.frame, text="3", width=8, font=10, command=lambda:self.btnclick(3))
        self.btn_mul = Button(self.frame, text="x", width=8, font=10, command=self.mul)

        self.btn0 = Button(self.frame, text="0", width=8, font=10, command=lambda:self.btnclick(0))
        self.btnclear = Button(self.frame, text="Clear", width=19, font=10, command=self.clear)
        self.btn_divsion = Button(self.frame, text="/", width=8, font=10, command=self.div)


        self.btn_equal = Button(self.frame, text="=", width=51, command=self.equal)

        # Placing
        self.display.grid(row=0,column=0, columnspan=3, padx=7,pady=10, ipady=3)
        self.sub_display.grid(row=0, column=3, padx=3,pady=10, ipady=3)

        self.btn7.grid(row=1, column=0, pady=5)
        self.btn8.grid(row=1, column=1)
        self.btn9.grid(row=1, column=2)
        self.btn_pluse.grid(row=1, column=3)

        self.btn4.grid(row=2, column=0, pady=5)
        self.btn5.grid(row=2, column=1)
        self.btn6.grid(row=2, column=2)
        self.btn_minus.grid(row=2, column=3)

        self.btn1.grid(row=3, column=0, pady=5)
        self.btn2.grid(row=3, column=1)
        self.btn3.grid(row=3, column=2)
        self.btn_mul.grid(row=3, column=3)

        self.btn0.grid(row=4, column=0, pady=5)
        self.btnclear.grid(row=4, column=1, columnspan=2)
        self.btn_divsion.grid(row=4,column=3)

        self.btn_equal.grid(row=5, column=0, columnspan=4, pady=5, ipady=4, padx=8)
        self.frame.pack()

        # Logic
        self.pluse = 0
        self.minus = 0
        self.mul = 0
        self.div = 0
        self.second_num = 0
        self.calculation = 0


    def btnclick(self, number):
        if self.calculation == 0:
            current = self.display.get()
            self.display.delete(0, END)  # Deleting value after assigning value in another variable
            self.display.insert(0, str(current) + str(number))
            self.sub_dis(number)
        else:
            self.display.delete(0, END)
            self.calculation = 0
            self.display.insert(0, str(number))
            self.sub_dis(number)


    def sub_dis(self, number):
        current = self.sub_display.get()
        self.sub_display.delete(0, END)  # Deleting value after assigning value in another variable
        self.sub_display.insert(0, str(current) + str(number))


    def pluse(self):
        try:
            self.pluse = int(self.display.get())
            self.display.delete(0, END)
            self.sub_dis(' + ')
        except:
            pass

    def minus(self):
        try:
            self.minus = int(self.display.get())
            self.display.delete(0, END)
            self.sub_dis(' - ')
        except:
            pass

    def mul(self):
        try:
            self.mul = int(self.display.get())
            self.display.delete(0, END)
            self.sub_dis(' x ')
        except:
            pass

    def div(self):
        try:
            self.div = int(self.display.get())
            self.display.delete(0, END)
            self.sub_dis(' / ')
        except:
            pass

    def equal(self):
        try:
            self.second_num = int(self.display.get())
            self.display.delete(0, END)
            self.sub_display.delete(0, END)
            if self.pluse > 0:
                self.display.insert(0, self.pluse + self.second_num)
                self.calculation = 1
            elif self.minus > 0:
                self.display.insert(0, self.minus-self.second_num)
                self.calculation = 1
            elif self.mul > 0:
                self.display.insert(0, self.mul * self.second_num)
                self.calculation = 1
            elif self.div > 0:
                self.display.insert(0, self.div / self.second_num)
                self.calculation = 1
            else:
                self.display.insert(0, self.second_num)
        except:
            pass

    def clear(self):
        self.display.delete(0, END)
        self.pluse = 0
        self.minus = 0
        self.mul = 0
        self.div = 0
        self.second_num = 0
        self.sub_display.delete(0, END)



if __name__ == "__main__":
    app = App()
    app.mainloop()
