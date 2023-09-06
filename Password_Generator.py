from tkinter import*
from random import randint
root=Tk()
root.title("Password Generator")
root.geometry("500x300")

my_password=chr(randint(1,120))

def new_rand():
    pw_entry.delete(0,END)

    pw_length= int(my_entry.get())

    my_password=''

    for i in range(pw_length):
        my_password+=chr(randint(1,120))

    pw_entry.insert(0,my_password)
def new_cpy():
     root.clipboard_clear()
     root.clipboard_append(pw_entry.get())

log = Label(root,text="Enter the number of characters:",font=("Times",15))
log.pack(padx=10,pady=10)

my_entry= Entry(root,font=("Times",20),bg=("Black"),fg="White")
my_entry.pack(padx=10)

log_sec= Label(root,text="Generated password:",font=("Times",15))
log_sec.pack(pady=20)

pw_entry=Entry(root,text="",font=("Times",20),bg=("Black"),fg="White")
pw_entry.pack(pady=0)

my_frame= Frame(root)
my_frame.pack(pady=20)

my_button= Button(my_frame,text="Generate",relief=RAISED,command=new_rand)
my_button.grid(row=0,column=0,padx=10)

pw_button=Button(my_frame,text="Copy to clipboard",relief=RAISED,command=new_cpy)
pw_button.grid(row=0,column=1,padx=10)



root.mainloop()
