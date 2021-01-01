from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import emailSend
import json


def test():
    emailSend.check_time()
    window.after(60000, test)


# ---------------------------- SAVE TIME TABLE ------------------------------- #
def save():
    class_name = class_name_entry.get()
    s_time = start_time_entry.get()
    day = day_chosen.get()
    new_data = (class_name, s_time)

    if len(class_name) == 0 or len(s_time) == 0 or len(day) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        except json.decoder.JSONDecodeError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data[day].append(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            class_name_entry.delete(0, END)
            class_name_entry.focus()
            start_time_entry.delete(0, END)
            day_chosen.delete(0, END)


# ---------------------------- SHOW TIME TABLE ------------------------------- #
def show_timetable():
    day = day_chosen.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            try:
                if data[day]:
                    classes = ""
                    for i in data[day]:
                        classes += f"Class: {i[0]} Time: {i[1]}\n"
                    messagebox.showinfo(title=day,
                                        message=classes)
                else:
                    messagebox.showinfo(title="YAY!", message="No classes today.")
            except KeyError:
                messagebox.showinfo(title="Error!", message="Select a day and the retry.")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")


# ---------------------------- UI SETUP ------------------------------- #
# Creating window

window = Tk()
window.title("VIT CLASS MANAGER")
window.config(padx=50, pady=50)

# Canvas for logo
canvas = Canvas(height=100, width=300)
logo_img = PhotoImage(file="vit-logo.png")
canvas.create_image(150, 50, image=logo_img)
canvas.grid(row=0, column=1, columnspan=1)

# Labels
day_label = Label(text="Day : ")
day_label.grid(row=1, column=0)
class_name_label = Label(text="Class Name : ")
class_name_label.grid(row=2, column=0)
start_time_label = Label(text="Start Time(hh:mm) : ")
start_time_label.grid(row=3, column=0)

# Buttons
search = Button(text="Search", command=show_timetable)
search.grid(row=1, column=2)
add = Button(text="Add", width=32, command=save)
add.grid(row=4, column=1, columnspan=2)

# Dropdowns
n = StringVar()
day_chosen = ttk.Combobox(window, width=27, textvariable=n)

# Adding combobox drop down list
day_chosen['values'] = ('Monday',
                        'Tuesday',
                        'Wednesday',
                        'Thursday',
                        'Friday',
                        'Saturday',
                        'Sunday')

day_chosen.grid(row=1, column=1)
day_chosen.current()

# Entry
class_name_entry = Entry(width=30)
class_name_entry.focus()
class_name_entry.grid(row=2, column=1)
start_time_entry = Entry(width=30)
start_time_entry.grid(row=3, column=1)

test()

window.mainloop()
