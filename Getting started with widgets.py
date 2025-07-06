from tkinter import *
from datetime import date
root = Tk()
root.title('getting started with widgets')
root.geometry('300x400')
lbl = Label(text="hey there!", fg = "white", bg="#072F5F", height=1, width=300)
name_lbl = Label(text="full name", bg=  "#3895D3")
name_entry = Entry()
name = name_entry.get()
def display():
    name = name_entry.get()
    global message
    message = "welcome to the application! \nToday is:"
    greet = "hello "+name+"\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())
text_box = Text(height = 3)
btn = Button(text="begin", command=display, height=1, bg="#1261A0", fg='white')
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()