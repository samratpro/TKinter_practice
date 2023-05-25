from tkinter import *
from tkinter import messagebox


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Project")
        self.geometry("400x500")
        self.bg_color = "#91FFFF"
        self.configure(bg=self.bg_color)

        # These all properties are is for frame
        self.frame = Frame(bg=self.bg_color)

        # Widgets
        self.home_label = Label(self.frame, text="Login Form", bg=self.bg_color, font=('Arial', 15))  # Home Label
        self.username_label = Label(self.frame, text=" User Name ", bg=self.bg_color, fg="red", font=20)
        self.username_entry = Entry(self.frame)
        self.pass_label = Label(self.frame, text=" Password ", bg=self.bg_color, fg="red", font=20)
        self.pass_entry = Entry(self.frame)
        self.login_button = Button(self.frame, text="Login", command=self.login)

        # Placing location
        self.home_label.grid(row=0, column=0, columnspan=3, pady=40)  # grid, pack can't use same screen
        self.username_label.grid(row=1, column=0);
        self.username_entry.grid(row=1, column=1)
        self.pass_label.grid(row=2, column=0);
        self.pass_entry.grid(row=2, column=1)
        self.login_button.grid(row=3, column=0, pady=30)
        self.frame.pack()

    def login(self):
        username = 'sam'
        password = "123"
        if self.username_entry.get() == username and self.pass_entry.get() == password:
            messagebox.showinfo(title="Success", message="You have logined")
        else:
            messagebox.showerror(title="Failed", message="Failed try again")


if __name__ == "__main__":
    app = App()
    app.mainloop()