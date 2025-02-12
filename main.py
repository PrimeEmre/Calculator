import tkinter
window = tkinter.Tk()
window.title("Tkinter")
window.minsize(width=1000, height=1000)

def first_num_entery():
    pass


calculator_title = tkinter.Label(window,text="Calculator", font=(25,),bg='black',fg='white')
calculator_title.pack(pady=13)
# Setting the label for enter_number_entry
first_num_lable=tkinter.Label(window, text="Enter first number",font=('Arial', 15))
first_num_lable.pack(pady=3)
# Setting the 1rst entry
enter_number_entry = tkinter.Entry(window, font=("Arial",12,'italic'), width=13, bg='black', fg='white', bd=2, justify='center', relief='solid', invalidcommand=first_num_entery)
enter_number_entry.pack()
num_label_second = tkinter.Label(window, text="Enter second number",font=("Arial", 15,'italic'),)
num_label_second.pack(pady=3)

window.mainloop()