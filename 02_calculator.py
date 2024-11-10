from tkinter import *

def main():
    app = Application()
    app.mainloop()

class Application(Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.iconbitmap(r'D:\7tsp\logo\Calculator.ico') 
        self.config(bg='Black')

        self.geometry("352x505")
        self.resizable(False, False)
        self.attributes('-alpha', 0.9)

        self.columnconfigure(0, weight=1)

        self.frame = InputForm(self)
        self.frame.grid(row=0, column=0, sticky=NSEW, padx=2, pady=2)

class InputForm(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="black")

        self.output_box = Label(self, height=2, width=17, bg='black', fg='white', anchor=E, font=('Calibri', 30))
        self.output_box.grid(row=0, column=0, columnspan=4, sticky=NSEW, padx=2, pady=2)

        l1 = ['AC', '∓', '%']
        for i, operator in enumerate(l1):
            self.btn = Button(self, text=operator, height=2, width=4, font=("calibri", 17), bg="#a5a5a5", fg='white', padx=2, pady=2, command=lambda op=operator: self.on_button_click(op))
            self.btn.grid(row=1, column=i, sticky=NSEW)

        l2 = ['7', '8', '9']
        for i, operator in enumerate(l2):
            self.btn = Button(self, text=operator, height=2, width=4, font=("calibri", 17), bg="#343434", fg='white', padx=2, pady=2, command=lambda op=operator: self.on_button_click(op))
            self.btn.grid(row=2, column=i, sticky=NSEW)

        l3 = ['4', '5', '6']
        for i, operator in enumerate(l3):
            self.btn = Button(self, text=operator, height=2, width=4, font=("calibri", 17), bg="#343434", fg='white', padx=2, pady=2, command=lambda op=operator: self.on_button_click(op))
            self.btn.grid(row=3, column=i, sticky=NSEW)

        l4 = ['1', '2', '3']
        for i, operator in enumerate(l4):
            self.btn = Button(self, text=operator, height=2, width=4, font=("calibri", 17), bg="#343434", fg='white', padx=2, pady=2, command=lambda op=operator: self.on_button_click(op))
            self.btn.grid(row=4, column=i, sticky=NSEW)

        l5 = ['.']
        for i, operator in enumerate(l5):
            self.btn = Button(self, text=operator, height=2, width=4, font=("calibri", 17), bg="#343434", fg='white', padx=2, pady=2, command=lambda op=operator: self.on_button_click(op))
            self.btn.grid(row=5, column=i+2, sticky=NSEW)

        l6 = ['0']
        for i, operator in enumerate(l6):
            self.btn = Button(self, text=operator, height=2, width=4, font=("calibri", 17), bg="#343434", fg='white', padx=2, pady=2, command=lambda op=operator: self.on_button_click(op))
            self.btn.grid(row=5, column=i, columnspan=2, sticky=NSEW)

        l7 = ['÷', '×', '–', '+', '=']
        for i, operator in enumerate(l7):
            self.btn = Button(self, text=operator, height=2, width=4, font=("calibri", 17), bg="#ff9f0a", fg='white', padx=2, pady=2, command=lambda op=operator: self.on_button_click(op))
            self.btn.grid(row=i+1, column=3, sticky=NSEW)

    def on_button_click(self, value):
        current_text = self.output_box.cget("text")
        if value == "AC":
            self.output_box.config(text="")
        elif value == "=":
            try:
                result = eval(current_text.replace('×', '*').replace('÷', '/').replace('–', '-'))
                self.output_box.config(text=str(result))
            except:
                self.output_box.config(text="Error")
        elif value == "∓":
            if current_text:
                # Invert the sign of the current number
                if current_text[0] == '–':
                    new_text = current_text[1:]  # Remove the negative sign
                else:
                    new_text = '-' + current_text  # Add a negative sign
                self.output_box.config(text=new_text)
        elif value == "%":
            try:
                new_text = str(eval(str(int(current_text)/100)))
                self.output_box.config(text=new_text)
            except:
                self.output_box.config(text="Error")

        else:
            new_text = current_text + value
            self.output_box.config(text=new_text)

if __name__ == "__main__":
    main()