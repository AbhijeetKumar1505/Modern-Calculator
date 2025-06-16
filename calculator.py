import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Calculator")
        self.root.geometry("320x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        # Style configuration
        style = ttk.Style()
        style.configure("TButton", padding=10, font=('Arial', 12))
        style.configure("Display.TEntry", padding=10, font=('Arial', 20))

        # Variable to store current calculation
        self.current = ""
        self.result_var = tk.StringVar()
        self.result_var.set("0")

        # Create display
        self.create_display()
        # Create buttons
        self.create_buttons()

    def create_display(self):
        display_frame = tk.Frame(self.root, bg="#f0f0f0")
        display_frame.pack(expand=True, fill="both", padx=10, pady=10)

        display = ttk.Entry(
            display_frame,
            textvariable=self.result_var,
            justify="right",
            style="Display.TEntry",
            state="readonly"
        )
        display.pack(expand=True, fill="both")

    def create_buttons(self):
        buttons_frame = tk.Frame(self.root, bg="#f0f0f0")
        buttons_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Button layout
        buttons = [
            ('C', 0, 0), ('±', 0, 1), ('%', 0, 2), ('÷', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('×', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('0', 4, 0, 2), ('.', 4, 2), ('=', 4, 3)
        ]

        # Configure grid
        for i in range(5):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)

        # Create and place buttons
        for button in buttons:
            if len(button) == 4:  # Special case for '0' button
                btn = ttk.Button(
                    buttons_frame,
                    text=button[0],
                    command=lambda x=button[0]: self.button_click(x)
                )
                btn.grid(row=button[1], column=button[2], columnspan=button[3],
                        sticky="nsew", padx=2, pady=2)
            else:
                btn = ttk.Button(
                    buttons_frame,
                    text=button[0],
                    command=lambda x=button[0]: self.button_click(x)
                )
                btn.grid(row=button[1], column=button[2],
                        sticky="nsew", padx=2, pady=2)

    def button_click(self, value):
        if value == 'C':
            self.current = ""
            self.result_var.set("0")
        elif value == '=':
            try:
                # Replace × with * and ÷ with / for evaluation
                expression = self.current.replace('×', '*').replace('÷', '/')
                result = eval(expression)
                self.result_var.set(str(result))
                self.current = str(result)
            except:
                self.result_var.set("Error")
                self.current = ""
        elif value == '±':
            try:
                if self.current.startswith('-'):
                    self.current = self.current[1:]
                else:
                    self.current = '-' + self.current
                self.result_var.set(self.current)
            except:
                pass
        elif value == '%':
            try:
                result = float(self.current) / 100
                self.current = str(result)
                self.result_var.set(self.current)
            except:
                pass
        else:
            self.current += value
            self.result_var.set(self.current)

def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main() 