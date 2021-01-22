# importing Libraries

from tkinter import *
import random, string
import pyperclip

###initialize window

root = Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("HBL - PASSWORD GENERATOR")
root.configure(background='sea green')

# heading
heading = Label(root, text='PASSWORD GENERATOR', font='arial 15 bold',fg='white',bg='sea green').pack()
heading = Label(root, text='HBL', font='arial 15 bold',fg='white',bg='sea green').pack(side=BOTTOM)

###select password length
pass_label = Label(root, text='PASSWORD LENGTH', font='arial 10 bold',fg='black',bg='white').pack()
pass_len = IntVar()
length = Spinbox(root, from_=6, to_=25, textvariable=pass_len, width=15).pack()

#####define function


pass_str = StringVar()


def Generator():
    password = ''
    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(
            string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get() - 4):
        password = password + random.choice(
            string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)


###button

Button(root, text="GENERATE PASSWORD", command=Generator,fg='black',bg='white').pack(pady=5)

Entry(root, textvariable=pass_str,fg='black',bg='white').pack()


########function to copy

def Copy_password():
    pyperclip.copy(pass_str.get())


Button(root, text='COPY TO CLIPBOARD', command=Copy_password,fg='black',bg='white').pack(pady=5)

# loop to run program
root.mainloop()