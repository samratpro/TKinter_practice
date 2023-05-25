from tkinter import *
from tkinter import messagebox
import pyshorteners


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Link Shortner")
        self.bg_color = "#A7C1B5"
        self.geometry("300x400")
        self.configure(bg=self.bg_color)

        self.frame = Frame(bg=self.bg_color)  # Frame is for responsive
        # Widgets
        self.title_label = Label(self.frame, text="Link Shotner", bg=self.bg_color, fg='black', font=('Arial', 12))
        self.place_link = Label(self.frame, text="Enter Your Link", bg=self.bg_color)
        self.link_entry = Entry(self.frame)
        self.shortlink_label = Label(self.frame, text="Output Link", bg=self.bg_color)
        self.shortlink = Entry(self.frame)
        self.copy_link = Button(self.frame, text="Copy Link", command=self.short_url)


        # Placing
        self.title_label.grid(row=0, column=0, columnspan=5, pady=20)
        self.place_link.grid(row=1, column=0, columnspan=5)
        self.link_entry.grid(row=2, column=0, columnspan=5)
        self.shortlink_label.grid(row=3, column=0)
        self.shortlink.grid(row=4, column=0)
        self.copy_link.grid(row=5, column=0, pady=20)


        self.frame.pack() # Frame has been packed, pack is auto responsive

    def short_url(self):
        s = pyshorteners.Shortener()
        link = self.link_entry.get()
        if link and 'http' in link:
            short_url = s.tinyurl.short(link)
            self.shortlink.insert(0, short_url)
        else:
            messagebox.showerror(title="Error", message="Please input a vaild link")


if __name__ == "__main__":
    app = App()
    app.mainloop()
