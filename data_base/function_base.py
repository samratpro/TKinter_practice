from tkinter import *
import sqlite3


root = Tk()
connection = sqlite3.connect('users.db')


def query_db():
    e = connection.cursor()
    e.execute("""SELECT * FROM users""")
    datas = e.fetchall()
    i = 1
    for data in datas:
        data_show = Label(frame, text=data, borderwidth=5)
        data_show.grid(row=4+i, column=0, columnspan=2, pady=5, padx=20)
        i += 1


def create_db():
    try:
        e = connection.cursor()
        e.execute("""CREATE TABLE users(
            name text,
            city text,
            age integer
        )""")
        connection.commit()
    except:
        pass

def submit_data():
    try:
        e = connection.cursor()
        e.execute("INSERT INTO users VALUES (:name, :city, :age)",
                        {
                            'name': name_entry.get(),
                            'city': city_entry.get(),
                            'age': age_entry.get()
                        }

                        )
        connection.commit()
    except:
        pass
    name_entry.delete(0, END)
    city_entry.delete(0, END)
    age_entry.delete(0, END)


bg_color = "#B7D3C6"
root.title("User List")
root.geometry("400x500")
root.config(bg=bg_color)

# Widget
frame = Frame(root, bg=bg_color)
name_leb = Label(frame, text="Full Name : ", font=15, bg=bg_color)
name_entry = Entry(frame)
city_leb = Label(frame, text="City Name : ", font=15, bg=bg_color)
city_entry = Entry(frame)
age_leb = Label(frame, text="Age : ", font=15, bg=bg_color)
age_entry = Entry(frame)
submit = Button(frame, text="Submit Data", font=('arial', 10), command=submit_data)
query = Button(frame, text="Query", font=('arial', 10), command=query_db)

# Placing
name_leb.grid(row=0, column=0, pady=10)
name_entry.grid(row=0, column=1)
city_leb.grid(row=1, column=0, pady=10)
city_entry.grid(row=1, column=1)
age_leb.grid(row=2, column=0, pady=10)
age_entry.grid(row=2, column=1)
submit.grid(row=3, column=0, columnspan=2, pady=10)
query.grid(row=4, column=0, columnspan=2, pady=10)
frame.pack()

myscrollbar=Scrollbar(root,orient="vertical")
myscrollbar.pack(side="right",fill="y")


def run():
    root.mainloop()


if __name__ == "__main__":
    run()
