from tkinter import *
root=Tk()
root.title("Calculator")


#display
Display=Entry(root, width=50, borderwidth=5, bg="#d9ecf2")
Display.grid(row=0, column=0, columnspan=4, padx=10, pady=10 )


#operation
def button_click(number):
    current=Display.get()
    Display.delete(0,END)
    Display.insert(0,str(current)+str(number))

def button_clear():
    Display.delete(0, END)

def button_add():
    global first_Num
    global MATH
    MATH="ADD"
    x=int(Display.get())
    first_Num= x
    Display.delete(0,END);

def button_subt():
    global first_Num
    global MATH
    MATH="SUBT"
    x=int(Display.get())
    first_Num= x
    Display.delete(0,END);

def button_MULT():
    global first_Num
    global MATH
    MATH="MULT"
    x=int(Display.get())
    first_Num= x
    Display.delete(0,END);

def button_div():
    global first_Num
    global MATH
    MATH = "DIVID"
    x = int(Display.get())
    first_Num = x
    Display.delete(0, END);

def button_equ():
    ans=Display.get()
    Display.delete(0,END);
    if (MATH == "ADD"):
        Display.insert(0, first_Num + int(ans));
    elif (MATH == "SUBT"):
        Display.insert(0, first_Num - int(ans));
    elif (MATH == "MULT"):
        Display.insert(0, first_Num * int(ans));
    elif (MATH == "DIVID"):
        Display.insert(0, first_Num / int(ans));




#button
button_1=Button(root, text="1", padx=40, pady=20, bg="#ffefa0" ,command=lambda: button_click(1))
button_2=Button(root, text="2", padx=40, pady=20, bg="#ffefa0" ,command=lambda: button_click(2))
button_3=Button(root, text="3", padx=40, pady=20, bg="#ffefa0" ,command=lambda: button_click(3))
button_4=Button(root, text="4", padx=40, pady=20, bg="#ffefa0" ,command=lambda: button_click(4))
button_5=Button(root, text="5", padx=40, pady=20, bg="#ffefa0" ,command=lambda: button_click(5))
button_6=Button(root, text="6", padx=40, pady=20, bg="#ffefa0" ,command=lambda: button_click(6))
button_7=Button(root, text="7", padx=40, pady=20, bg="#ffefa0" ,command=lambda: button_click(7))
button_8=Button(root, text="8", padx=40, pady=20, bg="#ffefa0" ,command=lambda: button_click(8))
button_9=Button(root, text="9", padx=40, pady=20, bg="#ffefa0" ,command=lambda: button_click(9))
button_0=Button(root, text="0", padx=40, pady=20, bg="#ffefa0" ,command=lambda: button_click(0))
button_addi=Button(root, text="+", padx=39.4, pady=20, bg="#a5ecd7" ,command=button_add)
button_Clr=Button(root, text="CLR", padx=32.5, pady=20, bg="#a5ecd7" ,command=button_clear)
button_equal=Button(root, text="=", padx=39, pady=20, bg="#a5ecd7" ,command=button_equ)
button_divid=Button(root, text="/", padx=41, pady=20, bg="#a5ecd7" ,command=button_div)
button_mult=Button(root, text="*", padx=40, pady=20, bg="#a5ecd7" ,command=button_MULT)
button_sub=Button(root, text="-", padx=41, pady=20, bg="#a5ecd7" ,command=button_subt)


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_addi.grid(row=3, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_sub.grid(row=2, column=3)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_Clr.grid(row=1, column=3)

button_0.grid(row=4, column=0)
button_divid.grid(row=4, column=3)
button_mult.grid(row=4, column=2)
button_equal.grid(row=4, column=1)




root.mainloop()