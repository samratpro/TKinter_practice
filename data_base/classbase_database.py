from tkinter import *
import sqlite3


class Users:
    def __init__(self):
        self.root = Tk()
        self.connection = sqlite3.connect('users.db')

        self.bg_color = "#B7D3C6"
        self.root.title("User List")
        self.root.geometry("400x500")
        self.root.config(bg=self.bg_color)

        # Widget
        self.frame = Frame(self.root, bg=self.bg_color)
        self.name_leb = Label(self.frame, text="Full Name : ", font=15, bg=self.bg_color)
        self.name_entry = Entry(self.frame)
        self.city_leb = Label(self.frame, text="City Name : ", font=15, bg=self.bg_color)
        self.city_entry = Entry(self.frame)
        self.age_leb = Label(self.frame, text="Age : ", font=15, bg=self.bg_color)
        self.age_entry = Entry(self.frame)
        self.submit = Button(self.frame, text="Submit Data", font=('arial', 10), command=self.submit_data)
        self.query = Button(self.frame, text="Query", font=('arial', 10), command=self.query_db)

        # Placing
        self.name_leb.grid(row=0, column=0, pady=10)
        self.name_entry.grid(row=0, column=1)
        self.city_leb.grid(row=1, column=0, pady=10)
        self.city_entry.grid(row=1, column=1)
        self.age_leb.grid(row=2, column=0, pady=10)
        self.age_entry.grid(row=2, column=1)
        self.submit.grid(row=3, column=0, columnspan=2, pady=10)
        self.query.grid(row=4, column=0, columnspan=2, pady=10)
        self.frame.pack()

        myscrollbar=Scrollbar(self.root,orient="vertical")
        myscrollbar.pack(side="right",fill="y")


    def query_db(self):
        e = self.connection.cursor()
        e.execute("""SELECT * FROM users""")
        datas = e.fetchall()
        i = 1
        for data in datas:
            data_show = Label(self.frame, text=data, borderwidth=5)
            data_show.grid(row=4+i, column=0, columnspan=2, pady=5, padx=20)
            i += 1


    def create_db(self):
        try:
            e = self.connection.cursor()
            e.execute("""CREATE TABLE users(
                name text,
                city text,
                age integer
            )""")
            self.connection.commit()
        except:
            pass

    def submit_data(self):
        try:
            e = self.connection.cursor()
            e.execute("INSERT INTO users VALUES (:name, :city, :age)",
                          {
                              'name': self.name_entry.get(),
                              'city': self.city_entry.get(),
                              'age': self.age_entry.get()
                          }

                          )
            self.connection.commit()
        except:
            pass

        self.name_entry.delete(0, END)
        self.city_entry.delete(0, END)
        self.age_entry.delete(0, END)


    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = Users()
    app.run()
