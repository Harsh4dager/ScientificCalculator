from tkinter import *
from PIL import Image, ImageTk
import math as m


root = Tk()
root.title("Scientific Calculator")
root.config(bg="white")
# config function used to set the background to any colour.
# 600 is width 486 is height 100 is distance away from x axis and 100 is away from y axis
# root.geometry('600x400+100+100')

# ******************************functions************************************************


def click(value):
    ex = entryField.get()  # so that we can the content of entryfield in all the if blocks

    try:
        if value == 'C':
            ex = ex[0:len(ex) - 1]
            # using slicing we are deleting the last variable from the entryfield
            # it will delete everything from 0 index to the end.
            entryField.delete(0, END)
            entryField.insert(0, ex)
        elif value == 'CE':
            entryField.delete(0, END)
        elif value == '√':
            # this eval function will evaluate anything which is in string and convert it into int or float if necessary.
            ans = m.sqrt(eval(ex))
            entryField.delete(0, END)
            entryField.insert(0, ans)
        elif value == 'π':
            entryField.insert(0, m.pi)
        elif value == 'cos':
            ans = m.cos(m.radians(eval(ex)))
            entryField.delete(0, END)
            entryField.insert(0, ans)
        elif value == 'sin':
            ans = m.sin(m.radians(eval(ex)))
            entryField.delete(0, END)
            entryField.insert(0, ans)
        elif value == 'tan':
            ans = m.tan(m.radians(eval(ex)))
            entryField.delete(0, END)
            entryField.insert(0, ans)
        elif value == '2π':
            ans = 2*m.pi
            entryField.delete(0, END)
            entryField.insert(0, ans)
        elif value == 'cosh':
            ans = m.cosh(eval(ex))
            entryField.delete(0, END)
            entryField.insert(0, ans)
        elif value == 'sinh':
            ans = m.sinh(eval(ex))
            entryField.delete(0, END)
            entryField.insert(0, ans)
        elif value == 'tanh':
            ans = m.tanh(eval(ex))
            entryField.delete(0, END)
            entryField.insert(0, ans)
        elif value == chr(8731):
            ans = eval(ex)**(1/3)
            entryField.delete(0, END)
            entryField.insert(0, ans)
        elif value == "x\u02b8":
            entryField.insert(END, '**')

        elif value == 'x\u00b3':
            ans = eval(ex)**(3)
            entryField.delete(0, END)
            entryField.insert(0, ans)
        elif value == 'x\u00b2':
            ans = eval(ex)**(2)
            entryField.delete(0, END)
            entryField.insert(0, ans)
        elif value == 'ln':
            ans = m.log2(eval(ex))
            entryField.delete(0, END)
            entryField.insert(0, ans)
        elif value == 'deg':
            ans = m.degrees(eval(ex))
            entryField.delete(0, END)
            entryField.insert(0, ans)
        elif value == 'rad':
            ans = m.radians(eval(ex))
            entryField.delete(0, END)
            entryField.insert(0, ans)
        elif value == 'e':
            ans = m.e
            entryField.delete(0, END)
            entryField.insert(0, ans)
        elif value == 'lg':
            ans = m.log10(eval(ex))
            entryField.delete(0, END)
            entryField.insert(0, ans)
        elif value == 'x!':
            ans = m.factorial(eval(ex))
            entryField.delete(0, END)
            entryField.insert(0, ans)
        elif value == chr(247):
            entryField.insert(END, "/")

        elif value == '=':
            ans = eval(ex)
            entryField.delete(0, END)
            entryField.insert(0, ans)
        else:
            entryField.insert(END, value)
    except SyntaxError:
        pass


# ******************************functions************************************************
# logo
# Load the image using Pillow (PIL)
logo_image = Image.open("logo.jpg")
# Set the desired width and height
desired_width = 50
desired_height = 50
# Resize the image to the desired dimensions using BILINEAR mode
logo_image = logo_image.resize((desired_width, desired_height), Image.BILINEAR)
logo_photo = ImageTk.PhotoImage(logo_image)
# Create a Label to display the resized image
logo_label = Label(root, image=logo_photo)
logo_label.grid(row=0, column=0)


# Entry field
# to create it we can use entry function given to us.
# root specify tthat we want to put it inside the root window
entryField = Entry(root, font=('arial', 20, 'bold'), bg='gray',
                   fg='white', bd=10, relief=SUNKEN, width=30)
# fg specify the text colour, bd is border , relief is the styling of the border
entryField.grid(row=0, column=0, columnspan=8)


# buttons
button_text_list = [
    'C', 'CE', '√', '+', 'π', 'cos', 'tan', 'sin',
    '1', '2', '3', '-', '2π', 'cosh', 'tanh', 'sinh',
    '4', '5', '6', '*', chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
    "7", '8', '9', chr(247), "ln", "deg", "rad", 'e',
    "0", ".", "%", "=", "lg", "(", ")", "x!"
]
rowv = 1
colv = 0
for i in button_text_list:
    button = Button(root, width=5, height=2, bd=2, relief=SUNKEN,
                    text=i, fg='white', font=('arial', 16, 'bold'), bg='black', activebackground='gray', command=lambda button=i: click(button))
    # activebackground is the colour when we click the button
    # in command the annon lambda functin puts every button text inside the button variable and then this click function will be called.
    button.grid(row=rowv, column=colv)
    colv += 1
    if (colv > 7):
        rowv += 1
        colv = 0

root.mainloop()
