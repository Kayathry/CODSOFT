from tkinter import *
from tkinter import ttk
from views import *
from tkinter import messagebox

# colors
color1 = '#ffffff'  # white
color2 = '#000000'  # Black
color3 = '#4456F0'  # Blue

window = Tk()
window.title('Contact Book')
window.geometry('487x450')
window.configure(background=color1)
window.resizable(width=False, height=False)

# Frames
frame_up = Frame(window, width=500, height=50, bg=color3)
frame_up.grid(row=0, column=0, padx=0, pady=1)

frame_down = Frame(window, width=500, height=150, bg=color1)
frame_down.grid(row=1, column=0, padx=0, pady=1)

frame_table = Frame(window, width=500, height=100, bg=color1, relief='flat')
frame_table.grid(row=2, column=0, columnspan=2, padx=10, pady=2, sticky=NW)


# functions
def show():
    global display_data

    listheader = ['Name', 'Gender', 'Phone Number', 'Email']
    demo_list = view()
    display_data = ttk.Treeview(frame_table, selectmode='extended', columns=listheader, show='headings')
    vsb = ttk.Scrollbar(frame_table, orient='vertical', command=display_data.yview)
    hsb = ttk.Scrollbar(frame_table, orient='horizontal', command=display_data.xview)

    display_data.configure(yscrollcommand=vsb, xscrollcommand=hsb.set)

    display_data.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    display_data.heading(0, text='Name', anchor=NW)
    display_data.heading(1, text='Gender', anchor=NW)
    display_data.heading(2, text='Phone Number', anchor=NW)
    display_data.heading(3, text='Email', anchor=NW)

    display_data.column(0, width=120, anchor='nw')
    display_data.column(1, width=50, anchor='nw')
    display_data.column(2, width=120, anchor='nw')
    display_data.column(3, width=180, anchor='nw')

    for item in demo_list:
        display_data.insert('', 'end', values=item)


show()


def insert():
    Name = entry_name.get()
    Gender = c_gender.get()
    Phone_Number = entry_telephone.get()
    Email = entry_email.get()

    data = [Name, Gender, Phone_Number, Email]
    if Name == '' or Gender == '' or Phone_Number == '' or Email == '':
        messagebox.showwarning('data', 'Please Fill all fields!')
    else:
        add(data)
        messagebox.showinfo('data', 'Data added successfully!')

        entry_name.delete(0, 'end')
        c_gender.set('')
        entry_telephone.delete(0, 'end')
        entry_email.delete(0, 'end')
        show()


def to_update():
    try:
        tree_data = display_data.focus()
        tree_dict = display_data.item(tree_data)
        tree_list = tree_dict['values']

        Name = str(tree_list[0])
        Gender = str(tree_list[1])
        Phone_Number = str(tree_list[2])
        Email = str(tree_list[3])

        entry_name.delete(0, 'end')
        entry_name.insert(0, Name)
        c_gender.set(Gender)
        entry_telephone.delete(0, 'end')
        entry_telephone.insert(0, Phone_Number)
        entry_email.delete(0, 'end')
        entry_email.insert(0, Email)

        global button_confirm
        def confirm():
            new_name = entry_name.get()
            new_gender = c_gender.get()
            new_mobile_num = entry_telephone.get()
            new_email = entry_email.get()

            data = [Phone_Number, new_name, new_gender, new_mobile_num, new_email]
            update(data)

            messagebox.showinfo('Data', 'Data Updated Successfully!')

            try:
                button_confirm.destroy()
            except:
                pass

            entry_name.delete(0, 'end')
            c_gender.set('')
            entry_telephone.delete(0, 'end')
            entry_email.delete(0, 'end')

            show()

        button_confirm = Button(frame_down, text="Update", width=10, height=1, bg=color3, fg=color1, font=('Ivy', 8, 'bold'), command=confirm)
        button_confirm.place(x=290, y=50)

    except IndexError:
        messagebox.showerror("Error", 'Select one data from the table')


def to_remove():
    try:
        tree_data = display_data.focus()
        tree_dict = display_data.item(tree_data)
        tree_list = tree_dict['values']
        Phone_Number = str(tree_list[2])
        remove([Phone_Number])

        messagebox.showinfo('data', 'Data Successfully deleted!')

        show()

    except IndexError:
        messagebox.showerror("Error", 'Select one data from the table')


def to_search():
    phonenum = entry_search.get()
    if phonenum == '':
        messagebox.showwarning('Search', 'Please enter a phone number to search!')
    else:
        result = search([phonenum])
        if result:
            show()
        else:
            messagebox.showinfo('Search', 'No matching contact found.')


# frames_up widgets
app_name = Label(frame_up, text="Contact Book", height=1, font=('verdana', 17, 'bold'), fg=color1, background=color3)
app_name.place(x=5, y=5)

l_name = Label(frame_down, text='Name *', width=20, height=1, font=('Ivy', 12), background=color1, anchor=NW)
l_name.place(x=10, y=20)
entry_name = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief='solid')
entry_name.place(x=80, y=20)

l_gender = Label(frame_down, text='Gender *', width=20, height=1, font=('Ivy', 12), background=color1, anchor=NW)
l_gender.place(x=10, y=50)
c_gender = ttk.Combobox(frame_down, width=22, background=color1)
c_gender['values'] = ['', 'Female', 'Male']
c_gender.place(x=80, y=50)

l_telephone = Label(frame_down, text='PhoneNumber *', width=20, height=1, font=('Ivy', 12), background=color1, anchor=NW)
l_telephone.place(x=10, y=80)
entry_telephone = Entry(frame_down, width=20, justify='left', highlightthickness=1, relief='solid')
entry_telephone.place(x=125, y=80)

l_email = Label(frame_down, text='Email *', width=22, height=1, font=('Ivy', 12), background=color1, anchor=NW)
l_email.place(x=10, y=110)
entry_email = Entry(frame_down, width=27, justify='left', highlightthickness=1, relief='solid')
entry_email.place(x=80, y=110)

button_search = Button(frame_down, text="Search", width=6, height=1, bg=color3, fg=color1, font=('Ivy', 8, 'bold'), command=to_search)
button_search.place(x=290, y=20)
entry_search = Entry(frame_down, width=16, justify='left', font=('Ivy', 11), highlightthickness=1, relief='solid')
entry_search.place(x=347, y=20)

# button_view = Button(frame_down, text="View", width=6, height=1, bg=color3, fg=color1, font=('Ivy', 8, 'bold'))
# button_view.place(x=290, y=50)

button_add = Button(frame_down, text="Add", width=10, height=1, bg=color3, fg=color1, font=('Ivy', 8, 'bold'), command=insert)
button_add.place(x=400, y=50)

button_update = Button(frame_down, text="Edit", width=10, height=1, bg=color3, fg=color1, font=('Ivy', 8, 'bold'), command=to_update)
button_update.place(x=400, y=80)

button_delete = Button(frame_down, text="Delete", width=10, height=1, bg=color3, fg=color1, font=('Ivy', 8, 'bold'), command=to_remove)
button_delete.place(x=400, y=110)

show()

if __name__ == "__main__":
    window.mainloop()
