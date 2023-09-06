from tkinter import*
from tkinter import messagebox


root=Tk()
root.title("To do List")
root.geometry("350x450")

def add_task():
     temp = new_entry.get()
     if temp!= "":
          msg_box.insert(END,temp)
          new_entry.delete(0,END)
     else:
          messagebox.showwarning("ERROR","Task cannot be empty")
def delete_task():
          selected_task=msg_box.curselection()
          if selected_task:
               msg_box.delete(selected_task)
          else:
               messagebox.showwarning("ERROR","Select any task")

def delete_all_tasks():
     msg_box.delete(0,END)


log=Label(root,text="To Do List :",font=("arial",20),fg="Black")
log.place(x=5,y=5)


new_entry=Entry(root,font=("arial"),bg="Orange",fg="Black")
new_entry.place(x=10,y=50)

btn_1=Button(root,text="ADD",font=("arial",10),height=1,width=12,bg="Black",fg="White",command=add_task)
btn_1.place(x=240,y=48)

msg_box=Listbox(root,height=15,width=49,font=("arial",10),bg="Black",fg="White")
msg_box.place(x=3,y=100)

btn_2=Button(root,text="Delete this task",height=1,width=12,bg="Black",fg="White",command=delete_task)
btn_2.place(x=130,y=370)

btn_3=Button(root,text="Delete all tasks",height=1,width=12,bg="Black",fg="White",command=delete_all_tasks)
btn_3.place(x=130,y=410)



root.mainloop()
