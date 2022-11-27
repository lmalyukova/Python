from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog


def main():
  root = Tk()
  root.title('Malyukova Elena ...')
  root.geometry('500x300+400+200')
  root.minsize(500, 300)
  root.resizable(False, False)


  style = ttk.Style()
  style.theme_create('tabs', parent='alt', settings={
    'TNotebook': {
      'configure': {
        'tabmargins': [2, 5, 2, 0],
      },
    },
    'TNotebook.Tab': {
      'configure': {
        'padding': [52, 0],
      },
    },
  })
  style.theme_use('tabs')

  tab_control = ttk.Notebook(root)
  calculator_tab = ttk.Frame(tab_control)
  tab_control.add(calculator_tab, text='Calculator')
  checkboxes_tab = ttk.Frame(tab_control)
  tab_control.add(checkboxes_tab, text='Checkboxes')
  text_tab = ttk.Frame(tab_control)
  tab_control.add(text_tab, text='Text')
  tab_control.pack(expand=1, fill='both')

  
  calculator_tab.grid_rowconfigure(0, weight=1)
  for i in range(5):
    calculator_tab.grid_columnconfigure(i, weight=1)
  n1 = ttk.Entry(calculator_tab, width=5)
  n1.grid(row=0, column=0)
  oper = ttk.Combobox(calculator_tab, value=['+', '-', '/', '*'], width=5)
  oper.grid(row=0, column=1)
  n2 = ttk.Entry(calculator_tab, width=5)
  n2.grid(row=0, column=2)
  answer = ttk.Label(calculator_tab, text='0')
  answer.grid(row=0, column=4)
  style.configure('TButton', background='#fff')
  ttk.Button(calculator_tab, text='=', command=calculate(answer, n1, n2, oper), style='TButton').grid(row=0, column=3)


  checkboxes_tab.grid_columnconfigure(0, weight=1)
  for i in range(4):
    checkboxes_tab.grid_rowconfigure(i, weight=1)
  ch1_var = BooleanVar()
  ch1_var.set(0)
  ch1 = ttk.Checkbutton(checkboxes_tab, text='First', variable=ch1_var, onvalue=1, offvalue=0)
  ch1.grid(row=0, column=0)
  ch2_var = BooleanVar()
  ch2_var.set(0)
  ch2 = ttk.Checkbutton(checkboxes_tab, text='Second', variable=ch2_var, onvalue=1, offvalue=0)
  ch2.grid(row=1, column=0)
  ch3_var = BooleanVar()
  ch3_var.set(0)
  ch3 = ttk.Checkbutton(checkboxes_tab, text='Third', variable=ch3_var, onvalue=1, offvalue=0)
  ch3.grid(row=2, column=0)
  ttk.Button(checkboxes_tab, text='Press me', command=check_boxes(ch1_var, ch2_var, ch3_var)).grid(row=3, column=0)


  scrollbar = ttk.Scrollbar(text_tab)
  scrollbar.pack(side='right', fill='y')
  text = Text(text_tab, yscrollcommand=scrollbar.set)
  text.pack(fill='both')
  scrollbar.config(command=text.yview)
  menu = Menu()
  menu.add_command(label='Open', command=open_file(text))
  menu.add_command(label='Save', command=save_file(text))
  root.config(menu=menu)


  root.mainloop()


def calculate(answer, n1, n2, oper):
  def inner():
    n1_val = float(n1.get())
    n2_val = float(n2.get())
    oper_val = oper.get()
    if oper_val == '+':
      answer['text'] = n1_val + n2_val
    if oper_val == '-':
      answer['text'] = n1_val - n2_val
    if oper_val == '*':
      answer['text'] = n1_val * n2_val
    if oper_val == '/':
      answer['text'] = n1_val / n2_val
  return inner


def check_boxes(*variables):
  def inner():
    text = ''
    for i in range(len(variables)):
      if variables[i].get() == 1:
        text += f'You\'ve chosen the {i + 1} option.\n'
    messagebox.showinfo('Your options', text)
  return inner


def open_file(text):
  def inner():
    path = filedialog.askopenfilename()
    with open(path, 'r') as file:
      text.delete('1.0', 'end')
      text.insert('0.end', file.read())
  return inner


def save_file(text):
  def inner():
    path = filedialog.asksaveasfilename()
    with open(path, 'w') as file:
      file.write(text.get('1.0', 'end'))
  return inner


if __name__ == '__main__':
  main()
