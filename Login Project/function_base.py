from tkinter import *
from tkinter import messagebox

window = Tk()  # main object
window.geometry("400x500")  # screen area
window.title("Login Project")  # main title
bg_color = "#91FFFF"        # global bg color
window.configure(bg=bg_color)  # main body configure


def login():
    username = 'sam'
    password = "123"
    if username_entry.get() == username and pass_entry.get() == password:
        messagebox.showinfo(title="Success!", message="You have loged in")
    else:
        messagebox.showerror(title="Error", message="Failed, try again")


# These all properties are is for frame
frame = Frame(bg=bg_color)  # Responsive frame

# Widgets
home_label = Label(frame, text="Login Form", bg=bg_color, font=('Arial', 15))  # Home Label
username_label = Label(frame, text=" User Name ", bg=bg_color, fg="red", font=20)
username_entry = Entry(frame)
pass_label = Label(frame, text=" Password ", bg=bg_color, fg="red", font=20)
pass_entry = Entry(frame)
login_button = Button(frame, text="Login", command=login)

# Placing location
home_label.grid(row=0, column=0, columnspan=3, pady=40)  # grid, pack can't use same screen
username_label.grid(row=1, column=0); username_entry.grid(row=1, column=1)
pass_label.grid(row=2, column=0); pass_entry.grid(row=2, column=1)
login_button.grid(row=3, column=0, pady=30)

if __name__ == "__main__":
    frame.pack()  # Frame object packing
    window.mainloop()  # Main object ending