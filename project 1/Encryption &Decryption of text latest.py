from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    password = code.get()
    
    # Use birthdate (password) for decryption
    if password == birthdate.get():
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x400")
        screen2.config(bg="light gray")
        
        message = text1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt_message = base64_bytes.decode("ascii")
        
        Label(screen2, text="DECRYPT", font="arial", fg="white", bg="light gray").place(x=10, y=0)
        
        text2 = Text(screen2, font="Roboto 20", bg="white", relief=GROOVE, fg="black", undo=True, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        
        text2.insert(END, decrypt_message)
    elif password == "":
        messagebox.showerror("decryption", "Enter password")
    else:
        messagebox.showerror("decryption", "Invalid password")


def encrypt():
    password = code.get()
    
    # Use birthdate (password) for encryption
    if password == birthdate.get():
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x400")
        screen1.config(bg="light gray")
        
        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt_message = base64_bytes.decode("ascii")
        
        Label(screen1, text="ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
        
        text2 = Text(screen1, font="Roboto 20", bg="white", relief=GROOVE, fg="black", undo=True, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        
        text2.insert(END, encrypt_message)
    elif password == "":
        messagebox.showerror("encryption", "Enter password")
    else:
        messagebox.showerror("encryption", "Invalid password")


def main_screen():
    global screen
    global code
    global text1
    global birthdate
    
    screen = Tk()
    screen.geometry("375x398")
    screen.config(bg="light gray")
    
    # Icon
    image_icon = PhotoImage(file="Key.png")  # Make sure the image file exists
    screen.iconphoto(False, image_icon)
    screen.title("Text Encryption & Decryption App")
    
    def reset():
        code.set("")
        text1.delete(1.0, END)
    
    Label(text="Enter text for Encryption & Decryption", fg="black", font=("Plus Jakarta Sans", 12)).place(x=10, y=10)
    text1 = Text(font="Roboto 20", bg="white", relief=GROOVE, fg="black", undo=True, wrap=WORD)
    text1.place(x=10, y=50, width=355, height=100)
    
    Label(text="Enter your birthdate (DDMMYYYY) as password", fg="black", font=("Plus Jakarta Sans", 13)).place(x=10, y=170)
    
    birthdate = StringVar()  # Variable to store the birthdate (password)
    Entry(textvariable=birthdate, font="Roboto 20", bg="white", fg="black").place(x=10, y=200, width=355)
    
    code = StringVar()  # Variable for user input (password)
    Entry(textvariable=code, font="Roboto 20", bg="white", fg="black", show="*").place(x=10, y=230, width=355)
    
    Button(text="ENCRYPT", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=280)
    Button(text="DECRYPT", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=280)
    Button(text="RESET", height="2", width=50, bg="#f7b731", fg="white", bd=0, command=reset).place(x=10, y=330)
    
    screen.mainloop()

main_screen()
