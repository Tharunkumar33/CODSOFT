from tkinter import*

root=Tk()
root.title("Simple Calculator")
root.geometry("290x400")

equation=""

def show(value):
    global equation
    equation+=value
    log.configure(text=equation)

def clear():
    global equation
    equation=""
    log.configure(text=equation)

def calculate():
    global equation
    result=""
    if equation!="":
        try:
            result=eval(equation)
        except:
            result="ERROR"
            equation=""
        log.configure(text=result)

log=Label(root,text="",font=("arial",9,"bold"),height=3,width=100,fg="White",bg="Black")
log.pack(pady=5)

btn_1=Button(root,text="Clr",font=("arial",9,"bold"),height=4,width=9,bg="Orange",fg="Black",command=lambda: clear()).place(x=0,y=55)
btn_1=Button(root,text="1",font=("arial",9,"bold"),height=4,width=9,bg="Black",fg="White",command=lambda: show("1")).place(x=72,y=55)
btn_1=Button(root,text="2",font=("arial",9,"bold"),height=4,width=9,bg="Black",fg="White",command=lambda: show("2")).place(x=144,y=55)
btn_1=Button(root,text="3",font=("arial",9,"bold"),height=4,width=9,bg="Black",fg="White",command=lambda: show("3")).place(x=216,y=55)


btn_1=Button(root,text="4",font=("arial",9,"bold"),height=4,width=9,bg="Black",fg="White",command=lambda: show("4")).place(x=0,y=126)
btn_1=Button(root,text="5",font=("arial",9,"bold"),height=4,width=9,bg="Black",fg="White",command=lambda: show("5")).place(x=72,y=126)
btn_1=Button(root,text="6",font=("arial",9,"bold"),height=4,width=9,bg="Black",fg="White",command=lambda: show("6")).place(x=144,y=126)
btn_1=Button(root,text="7",font=("arial",9,"bold"),height=4,width=9,bg="Black",fg="White",command=lambda: show("7")).place(x=216,y=126)


btn_1=Button(root,text="8",font=("arial",9,"bold"),height=4,width=9,bg="Black",fg="White",command=lambda: show("8")).place(x=0,y=197)
btn_1=Button(root,text="9",font=("arial",9,"bold"),height=4,width=9,bg="Black",fg="White",command=lambda: show("9")).place(x=72,y=197)
btn_1=Button(root,text="0",font=("arial",9,"bold"),height=4,width=9,bg="Black",fg="White",command=lambda: show("0")).place(x=144,y=197)
btn_1=Button(root,text="+",font=("arial",9,"bold"),height=4,width=9,bg="White",fg="Black",command=lambda: show("+")).place(x=216,y=197)


btn_1=Button(root,text="-",font=("arial",9,"bold"),height=4,width=9,bg="White",fg="Black",command=lambda: show("-")).place(x=0,y=268)
btn_1=Button(root,text="*",font=("arial",9,"bold"),height=4,width=9,bg="White",fg="Black",command=lambda: show("*")).place(x=72,y=268)
btn_1=Button(root,text="/",font=("arial",9,"bold"),height=4,width=9,bg="White",fg="Black",command=lambda: show("/")).place(x=144,y=268)
btn_1=Button(root,text=".",font=("arial",9,"bold"),height=4,width=9,bg="Black",fg="White",command=lambda: show(".")).place(x=216,y=268)



btn_1=Button(root,text="=",font=("arial",10,"bold"),height=4,width=35,bg="Orange",fg="Black",command=lambda: calculate()).place(x=0,y=339)





root.mainloop()
