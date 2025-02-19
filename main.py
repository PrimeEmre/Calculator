import tkinter

# Setting tkinter
window = tkinter.Tk()
window.title("Tkinter")
window.minsize(width=1000, height=1000)


# Function to get first number
def get_first_num():
    return enter_number_entry.get()


# Function to get second number
def get_second_num():
    return second_num_entry.get()


# Handling dropdown selection
def dropdwon(selection):
    selected_calc_options.set(selection)


# Function to calculate result
def reslut():
    try:
        num1 = float(get_first_num())
        num2 = float(get_second_num())
        operation = selected_calc_options.get()

        # Operations
        if operation == '+':
            res = num1 + num2
        elif operation == "-":
            res = num1 - num2
        elif operation == "*":
            res = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result_label.config(text='Cannot divide by 0')
                return
            res = num1 / num2
        else:
            result_label.config(text='Select an operation')
            return

        # Display result
        result_label.config(text=f"Result: {res}")

    except ValueError:
        result_label.config(text="Enter valid numbers!")


# UI Elements
calculator_title = tkinter.Label(window, text="Calculator", font=(25,), bg='black', fg='white')
calculator_title.pack(pady=13)

first_num_label = tkinter.Label(window, text="Enter first number", font=('Arial', 15, 'bold'))
first_num_label.pack(pady=3)

enter_number_entry = tkinter.Entry(window, font=("Arial", 12, 'italic'), width=13, bg='black', fg='white', bd=2,
                                   justify='center', relief='solid')
enter_number_entry.pack()

# Setting the dropdown
selected_calc_options = tkinter.StringVar()
selected_calc_options.set("Select a calc option")

# Setting calc apoptosis
calc_options = ['+', '-', '*', '/']
dropdown = tkinter.OptionMenu(window, selected_calc_options, *calc_options, command=dropdwon)
dropdown.pack(pady=5)

# setting the second entry
num_label_second = tkinter.Label(window, text="Enter second number", font=("Arial", 15, 'bold'))
num_label_second.pack(pady=3)
second_num_entry = tkinter.Entry(window, font=('Arial', 12, 'italic'), bg='black', fg='white', width=13, bd=2,
                                 justify='center')
second_num_entry.pack(pady=3)

# Result button
result_button = tkinter.Button(window, font=("Arial", 12, 'italic'), bg='black', fg='white', text="Result",
                               command=reslut)
result_button.pack(pady=5)
result_label = tkinter.Label(window, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=5)

window.mainloop()
