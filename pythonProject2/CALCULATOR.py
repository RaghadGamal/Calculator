from tkinter import *
from tkinter import messagebox


window =Tk()

window.title("Calculator")
window.geometry("387x350+500+150")
window.resizable(False,False)
window.configure(bg="#ede2e6")

def press(key) :
    current = ent1.get()
    ent1.delete(0, END)
    ent1.insert(0, current + str(key))

def calculate():
    try:
        result = eval(ent1.get())
        ent1.delete(0,END)
        ent1.insert(0,str(result))
    except Exception as e :
        messagebox.showerror("Error","Invalid Input")

def delete():
    current = ent1.get()
    ent1.delete(len(current)-1,END)






lab1 = Label(text ="Calculator ",
bg="#ede2e6",
fg = "black",
font =(10),
width=20,
height=0
             )
lab1.grid(row=0,column=0,columnspan=5,pady=15,padx=5)


ent1 = Entry(
font=("Helvetica", 30),
bg="white",
width=17,
            )

ent1.grid(row=1,column=0,columnspan=5,padx=5,pady=15)

btn1 = Button(
text=("1"),
bg=("#cd8495"),
fg=("white"),
width=12,
height=2,
    command=lambda: press('1')
)

btn1.grid(row=2,column=0,pady=1,padx=1)

btn2 = Button(
text=("2"),
bg=("#cd8495"),
fg=("white"),
width=12,
height=2,
command=lambda: press('2')
)
btn2.grid(row=2,column=1,pady=1,padx=1)


btn3 = Button(
text=("3"),
bg=("#cd8495"),
fg=("white"),
width=12,
height=2,
command=lambda: press('3')
)
btn3.grid(row=2,column=2,pady=1,padx=1)


btn4 = Button(
text=("4"),
bg=("#cd8495"),
fg=("white"),
width=12,
height=2,
command=lambda: press('4')
)
btn4.grid(row=3,column=0,pady=1,padx=1)


btn5 = Button(
text=("5"),
bg=("#cd8495"),
fg=("white"),
width=12,
height=2,
command=lambda: press('5')
)
btn5.grid(row=3,column=1,pady=1,padx=1)

btn6 = Button(
text=("6"),
bg=("#cd8495"),
fg=("white"),
width=12,
height=2,
command=lambda: press('6')
)
btn6.grid(row=3,column=2,pady=1,padx=1)

btn7 = Button(
text=("7"),
bg=("#cd8495"),
fg=("white"),
width=12,
height=2,
command=lambda: press('7')
)
btn7.grid(row=4,column=0,pady=1,padx=1)


btn8 = Button(
text=("8"),
bg=("#cd8495"),
fg=("white"),
width=12,
height=2,
command=lambda: press('8')
)
btn8.grid(row=4,column=1,pady=1,padx=1)

btn9 = Button(
text=("9"),
bg=("#cd8495"),
fg=("white"),
width=12,
height=2,
command=lambda: press('9')
)
btn9.grid(row=4,column=2,pady=1,padx=1)

btn0 = Button(
text=("0"),
bg=("#cd8495"),
fg=("white"),
width=12,
height=2,
command=lambda: press('0')
)
btn0.grid(row=5,column=1,pady=1,padx=1)

btnc = Button(
text=("c"),
bg=("#c96883"),
fg=("black"),
width=12,
height=2,
command=delete
)
btnc.grid(row=2,column=3,pady=1,padx=1)

btneql = Button(
text=("="),
bg=("#c96883"),
fg=("black"),
width=12,
height=2,
command= calculate
)
btneql.grid(row=5,column=3,pady=1,padx=1)

btnsum = Button(
text=("+"),
bg=("#c96883"),
fg=("black"),
width=12,
height=2,
command=lambda: press('+')
)
btnsum.grid(row=3,column=3,pady=1,padx=1)

btnsub = Button(
text=("-"),
bg=("#c96883"),
fg=("black"),
width=12,
height=2,
command=lambda: press('-')
)
btnsub.grid(row=4,column=3,pady=1,padx=1)

btnmul = Button(
text=("x"),
bg=("#c96883"),
fg=("black"),
width=12,
height=2,
command=lambda: press('*')
)
btnmul.grid(row=5,column=2,pady=1,padx=1)

btndiv = Button(
text=("/"),
bg=("#c96883"),
fg=("black"),
width=12,
height=2,
command=lambda: press('/')
)
btndiv.grid(row=5,column=0,pady=1,padx=1)


window.mainloop()