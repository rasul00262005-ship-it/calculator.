import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Калькулятор")
        self.window.geometry("400x550")
        self.window.resizable(False, False)
        self.window.configure(bg='#ffffff')
        
        # Поле ввода
        self.display_frame = tk.Frame(self.window, bg='#ffffff')
        self.display_frame.pack(pady=20)
        
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        
        self.display = tk.Entry(
            self.display_frame,
            textvariable=self.display_var,
            font=('Segoe UI', 32),
            justify='right',
            bg='#f8f9fa',
            fg='#000000',  # ЧЕРНЫЙ ТЕКСТ
            borderwidth=2,
            relief='groove'
        )
        self.display.pack(fill=tk.BOTH, ipady=15, padx=20)
        
        self.current = ""
        
        # Кнопки
        buttons = [
            ['C', '⌫', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '√', '^'],
            ['=']
        ]
        
        button_frame = tk.Frame(self.window, bg='#ffffff')
        button_frame.pack(expand=True, fill='both', padx=20, pady=10)
        
        for i, row in enumerate(buttons):
            frame_row = tk.Frame(button_frame, bg='#ffffff')
            frame_row.pack(expand=True, fill='both', pady=5)
            
            for j, text in enumerate(row):
                if text == '=':
                    btn = tk.Button(
                        frame_row,
                        text=text,
                        font=('Segoe UI', 18, 'bold'),
                        bg='#28a745',
                        fg='#ffffff',  # белый текст на зеленой кнопке
                        borderwidth=0,
                        command=self.calculate
                    )
                elif text in ['C', '⌫']:
                    btn = tk.Button(
                        frame_row,
                        text=text,
                        font=('Segoe UI', 16),
                        bg='#dc3545',
                        fg='#ffffff',  # белый текст
                        borderwidth=0,
                        command=lambda t=text: self.click(t)
                    )
                elif text in ['%', '√']:
                    btn = tk.Button(
                        frame_row,
                        text=text,
                        font=('Segoe UI', 16),
                        bg='#6c757d',
                        fg='#ffffff',  # белый текст
                        borderwidth=0,
                        command=lambda t=text: self.click(t)
                    )
                elif text in ['/', '*', '-', '+', '^']:
                    btn = tk.Button(
                        frame_row,
                        text=text,
                        font=('Segoe UI', 18, 'bold'),
                        bg='#ff9500',
                        fg='#ffffff',  # белый текст
                        borderwidth=0,
                        command=lambda t=text: self.click(t)
                    )
                else:
                    btn = tk.Button(
                        frame_row,
                        text=text,
                        font=('Segoe UI', 18),
                        bg='#e9ecef',
                        fg='#000000',  # ЧЕРНЫЙ ТЕКСТ для цифр
                        borderwidth=0,
                        command=lambda t=text: self.click(t)
                    )
                
                btn.pack(side=tk.LEFT, expand=True, fill='both', padx=3)
        
        self.update_display()
        self.window.bind('<Key>', self.key_press)
    
    def click(self, value):
        if value == 'C':
            self.current = ""
        elif value == '⌫':
            self.current = self.current[:-1]
        elif value == '√':
            try:
                num = float(self.current) if self.current else 0
                if num < 0:
                    messagebox.showerror("Ошибка", "Нельзя извлечь корень из отрицательного числа")
                    return
                result = math.sqrt(num)
                self.current = str(round(result, 10))
            except:
                messagebox.showerror("Ошибка", "Некорректное число")
                return
        elif value == '%':
            try:
                num = float(self.current) if self.current else 0
                result = num / 100
                self.current = str(round(result, 10))
            except:
                messagebox.showerror("Ошибка", "Некорректное число")
                return
        else:
            self.current += value
        
        self.update_display()
    
    def calculate(self):
        if not self.current:
            return
        try:
            expression = self.current.replace('^', '**')
            if '/0' in expression:
                messagebox.showerror("Ошибка", "Деление на ноль!")
                self.current = ""
                self.update_display()
                return
            result = eval(expression)
            if isinstance(result, float):
                if result.is_integer():
                    result = int(result)
                else:
                    result = round(result, 10)
            self.current = str(result)
            self.update_display()
        except ZeroDivisionError:
            messagebox.showerror("Ошибка", "Деление на ноль!")
            self.current = ""
            self.update_display()
        except:
            messagebox.showerror("Ошибка", "Некорректное выражение!")
            self.current = ""
            self.update_display()
    
    def key_press(self, event):
        key = event.char
        if key.isdigit() or key == '.':
            self.click(key)
        elif key in ['+', '-', '*', '/', '^']:
            self.click(key)
        elif key == '\r':
            self.calculate()
        elif key == '\x08':
            self.click('⌫')
        elif key == '\x1b':
            self.click('C')
    
    def update_display(self):
        if not self.current:
            self.display_var.set("0")
        else:
            self.display_var.set(self.current)
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()