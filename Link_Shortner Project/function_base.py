from tkinter import *
from tkinter import messagebox
import pyshorteners

window = Tk()

window.title("Link Shortner")
bg_color = "#A7C1B5"
window.geometry("300x400")
window.configure(bg=bg_color)


def short_url():
    s = pyshorteners.Shortener()
    link = link_entry.get()
    if link and 'http' in link:
        short_url = s.tinyurl.short(link)
        shortlink.insert(0, short_url)
    else:
        messagebox.showerror(title="Error", message="Please input a vaild link")



frame = Frame(bg=bg_color)  # Frame is for responsive
# Widgets
title_label = Label(frame, text="Link Shotner", bg=bg_color, fg='black', font=('Arial', 12))
place_link = Label(frame, text="Enter Your Link", bg=bg_color)
link_entry = Entry(frame)
shortlink_label = Label(frame, text="Output Link", bg=bg_color)
shortlink = Entry(frame)
copy_link = Button(frame, text="Generate Link", command=short_url)


# Placing
title_label.grid(row=0, column=0, columnspan=5, pady=20)
place_link.grid(row=1, column=0, columnspan=5)
link_entry.grid(row=2, column=0, columnspan=5)
shortlink_label.grid(row=3, column=0)
shortlink.grid(row=4, column=0)
copy_link.grid(row=5, column=0, pady=20)


if __name__ == "__main__":
    frame.pack()  # Frame has been packed, pack is auto responsive
    window.mainloop()

