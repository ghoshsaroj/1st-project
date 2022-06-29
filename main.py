from tkinter import *
import string
import random
#import pyperclip

def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_charecters=string.punctuation

    all=small_alphabets+capital_alphabets+numbers+special_charecters
    password_length=int(length_box.get())

    if choice.get()==1:
        passwordfield.insert(0,random.sample(small_alphabets,password_length))

    if choice.get()==2:
        passwordfield.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))

    if choice.get()==3:
        passwordfield.insert(0,random.sample(all,password_length))

    '''password=random.sample(all,password_length)
    passwordfield.insert(0,password)'''

#def copy():
 #   random_password=passwordfield.get()
  #  pyperclip.copy(random_password)

root=Tk()
root.config(bg='red')
choice=IntVar()
Font=('arial','13','bold')
passwordlabel=Label(root,text='Saroj Password Generator',font=('times new roman','20','bold'),bg='red',fg='white')
passwordlabel.grid(pady=10)
weekradiobutton=Radiobutton(root,text='Week',value=1,variable=choice,font=Font)
weekradiobutton.grid(pady=5)

mediumradiobutton=Radiobutton(root,text='Medium',value=2,variable=choice,font=Font)
mediumradiobutton.grid(pady=5)

strongradiobutton=Radiobutton(root,text='Strong',value=3,variable=choice,font=Font)
strongradiobutton.grid(pady=5)

lengthlabel=Label(root,text='Password Length',font=Font,bg='red',fg='white')
lengthlabel.grid(pady=5)

length_box=Spinbox(root,from_=5,to_=20,width=5,font=Font)
length_box.grid(pady=5)

generatebutton=Button(root,text='Generate',font=Font,command=generator)
generatebutton.grid(pady=5)

passwordfield=Entry(root,width=25,bd=2,font=Font)
passwordfield.grid(pady=5)

copybutton=Button(root,text='Copy',font=Font)
copybutton.grid(pady=5)

root.mainloop()
