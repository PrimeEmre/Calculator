import tkinter

window = tkinter.Tk()
window.title("Tkinter")
window.minsize(width=1000, height=1000)


# # Function to get first number
def first_num_entery():
    return first_num_entery.get()


# # Function to get first number
def second_num_entry():
    return second_num_entry.get()

# Setting the sctoins
def dropdwon(selection):
    selected_calc_options.set(selection)


def reslut():
    try:
        # Setting the variables of each entry and options
        num1=float (first_num_entery())
        num2 = float (second_num_entry())
        operation = selected_calc_options.get()

        # Setting the opratoin (+,=,*,/)
        if operation == '+':
            res = num1+num2
        elif operation =="-":
            res = num1-num2




calculator_title = tkinter.Label(window, text="Calculator", font=(25,), bg='black', fg='white')
calculator_title.pack(pady=13)

first_num_lable = tkinter.Label(window, text="Enter first number", font=('Arial', 15, 'bold'))
first_num_lable.pack(pady=3)

enter_number_entry = tkinter.Entry(window, font=("Arial", 12, 'italic'), width=13, bg='black', fg='white', bd=2,
                                   justify='center', relief='solid', invalidcommand=first_num_entery)
enter_number_entry.pack()

# Setting the dropdown
selected_calc_options = tkinter.StringVar()
selected_calc_options.set("Select a calc option")

# Added dropdown menu 
calc_options = ['+', '-', '*', '/']
dropdown = tkinter.OptionMenu(window, selected_calc_options, *calc_options, command='dropdwon')
dropdown.pack(pady=5)  # Add this line to display it

num_label_second = tkinter.Label(window, text="Enter second number", font=("Arial", 15, 'bold'))
num_label_second.pack(pady=3)

second_num_entry = tkinter.Entry(window, font=('Arial', 12, 'italic'), bg='black', fg='white', width=13, bd=2,
                                 justify='center', invalidcommand=second_num_entry)
second_num_entry.pack(pady=3)
# Result button
result_button = tkinter.Button(window, font=("Arial", 12, 'italic'), bg='black', fg='white', text="Result",
                               command=reslut)
result_button.pack(pady=5)
window.mainloop()
