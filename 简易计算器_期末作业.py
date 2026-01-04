"""
主题：简易计算器
功能：基本四则运算
GUI：使用Tkinter库创建图形界面
学号：2025321024
作者：wyktt
"""

# 导入GUI界面模块并命名其为tk,导入信息弹窗
import tkinter as tk
from tkinter import messagebox

# 实例化一个窗口对象
root = tk.Tk()

# 设置窗口大小长宽为300X300并出现在距离左上角+700+400,也就是正中央(
root.geometry('295x280+700+400')

# 命名窗口标题为简易计算器
root.title('简易计算器')

# 设置背景参数
root.attributes("-alpha", 0.9)
root["background"] = "#ffffff"

# 字体参数
font = ('宋体', 20)
font_16 = ('宋体', 16)

# 结果初始化
result_num = tk.StringVar()
result_num.set('')

tk.Label(root,
		textvariable = result_num, font = font, height = 2,
		width = 20, justify = tk.LEFT, anchor = tk.SE
		).grid(row = 1, column = 1, columnspan = 4)

# 使用网格布局实现按钮
button_clear = tk.Button(root, text = 'C', width = 5, font = font_16, relief = tk.FLAT, bg = '#b1b2b2')
button_back = tk.Button(root, text = '←', width = 5, font = font_16, relief = tk.FLAT, bg = '#b1b2b2')
button_division = tk.Button(root, text = '➗', width = 5, font = font_16, relief = tk.FLAT, bg = '#b1b2b2')
button_multiplication = tk.Button(root, text = '✖️', width = 5, font = font_16, relief = tk.FLAT, bg = '#b1b2b2')

button_clear.grid(row = 2, column = 1, padx = 4, pady = 2)
button_back.grid(row = 2, column = 2, padx = 4, pady = 2)
button_division.grid(row = 2, column = 3, padx = 4, pady = 2)
button_multiplication.grid(row = 2, column = 4, padx = 4, pady = 2)

button_seven = tk.Button(root, text = '7', width = 5, font = font_16, relief = tk.FLAT, bg = '#eacda1')
button_eight = tk.Button(root, text = '8', width = 5, font = font_16, relief = tk.FLAT, bg = '#eacda1')
button_nine = tk.Button(root, text = '9', width = 5, font = font_16, relief = tk.FLAT, bg = '#eacda1')
button_subtraction = tk.Button(root, text = '➖', width = 5, font = font_16, relief = tk.FLAT, bg = '#b1b2b2')

button_seven.grid(row = 3, column = 1, padx = 4, pady = 2)
button_eight.grid(row = 3, column = 2, padx = 4, pady = 2)
button_nine.grid(row = 3, column = 3, padx = 4, pady = 2)
button_subtraction.grid(row = 3, column = 4, padx = 4, pady = 2)

button_four = tk.Button(root, text = '4', width = 5, font = font_16, relief = tk.FLAT, bg = '#eacda1')
button_five = tk.Button(root, text = '5', width = 5, font = font_16, relief = tk.FLAT, bg = '#eacda1')
button_six = tk.Button(root, text = '6', width = 5, font = font_16, relief = tk.FLAT, bg = '#eacda1')
button_addtion = tk.Button(root, text = '➕', width = 5, font = font_16, relief = tk.FLAT, bg = '#b1b2b2')

button_four.grid(row = 4, column = 1, padx = 4, pady = 2)
button_five.grid(row = 4, column = 2, padx = 4, pady = 2)
button_six.grid(row = 4, column = 3, padx = 4, pady = 2)
button_addtion.grid(row = 4, column = 4, padx = 4, pady = 2)

button_one = tk.Button(root, text = '1', width = 5, font = font_16, relief = tk.FLAT, bg = '#eacda1')
button_two = tk.Button(root, text = '2', width = 5, font = font_16, relief = tk.FLAT, bg = '#eacda1')
button_three = tk.Button(root, text = '3', width = 5, font = font_16, relief = tk.FLAT, bg = '#eacda1')
button_equal = tk.Button(root, text = '🟰', width = 5, height = 3, font = font_16, relief = tk.FLAT, bg = '#b1b2b2')

button_one.grid(row = 5, column = 1, padx = 4, pady = 2)
button_two.grid(row = 5, column = 2, padx = 4, pady = 2)
button_three.grid(row = 5, column = 3, padx = 4, pady = 2)
button_equal.grid(row = 5, column = 4, padx = 4, pady = 2, rowspan = 2)

button_zero = tk.Button(root, text = '0', width = 12, font = font_16, relief = tk.FLAT, bg = '#eacda1')
button_dot = tk.Button(root, text = '.', width = 5, font = font_16, relief = tk.FLAT, bg = '#eacda1')

button_zero.grid(row = 6, column = 1, padx = 4, pady = 2, columnspan = 2)
button_dot.grid(row = 6, column = 3, padx = 4, pady = 2)

"""点击事件"""
def click_button(x):
	print('x\t', x)
	result_num.set(result_num.get() + x)

def conculation():
	opt_str = result_num.get()
	result = eval(opt_str)
	result_num.set(str(result))

button_one.config(command = lambda : click_button('1'))
button_two.config(command = lambda : click_button('2'))
button_three.config(command = lambda : click_button('3'))
button_four.config(command = lambda : click_button('4'))
button_five.config(command = lambda : click_button('5'))
button_six.config(command = lambda : click_button('6'))
button_seven.config(command = lambda : click_button('7'))
button_eight.config(command = lambda : click_button('8'))
button_nine.config(command = lambda : click_button('9'))
button_zero.config(command = lambda : click_button('0'))
button_addtion.config(command = lambda : click_button('+'))
button_subtraction.config(command = lambda : click_button('-'))
button_multiplication.config(command = lambda : click_button('*'))
button_division.config(command = lambda : click_button('/'))
button_equal.config(command = lambda : click_button('='))
button_dot.config(command = lambda : click_button('.'))

button_equal.config(command = lambda : conculation())

def clear_display():
	result_num.set('')

def backspace():
	current = result_num.get()
	result_num.set(current[:-1])

button_clear.config(command = clear_display)
button_back.config(command = backspace)

# 弹窗说明书
def show_instructions():
	"""显示使用说明书"""
	instructions = """	             简易计算器 - Alpha内测版
    功能说明：目前实现了加减乘除四则运算，其他功能还在开发中

            祝您使用愉快！""" 
	messagebox.showinfo("计算器使用说明书", instructions)

# 在程序启动时显示说明书
root.withdraw()
show_instructions()
root.deiconify()
# 启动主循环

root.mainloop()
