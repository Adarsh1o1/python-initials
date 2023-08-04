import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.display = tk.Entry(master, width=30,bg='#5689c0', fg='#eaebed',borderwidth=3, font=('Arial', 14))
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=15)

        # Create buttons for digits
        digits = ['7', '8', '9', '4', '5', '6', ' 1', ' 2', '3', '0', '.', '+/-','sin','cos','tan']
        for i, digit in enumerate(digits):
            button = tk.Button(master, text=digit, width=5, height=2, bg='#46a094', fg='#c4e8c2', relief="groove", font=('Arial', 12), command=lambda digit=digit: self.append_digit(digit))
            button.grid(row=i//3+1, column=i%3, padx=5, pady=5)

        # Create buttons for operators
        operators = ['+', '-', '*', '/', '(', ')','%', '=','AC' ,'DEL']
        for i, operator in enumerate(operators):
            button = tk.Button(master, text=operator, width=5, height=2, bg='#46a094', fg='#c4e8c2', font=('Arial', 12), command=lambda operator=operator: self.handle_operator(operator))
            button.grid(row=i//2+1, column=i%2+3, padx=5, pady=5)

    def append_digit(self, digit):
        self.display.insert(tk.END, digit)

    def handle_operator(self, operator):
        if operator == 'AC':
            self.display.delete(0, tk.END)
        elif operator == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, 'Syntax Error')
        elif operator == 'DEL':
            self.display.delete(len(self.display.get())-1)
        else:
            self.display.insert(tk.END, operator)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
