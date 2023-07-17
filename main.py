import tkinter
import cryptocode
from tkinter import messagebox

# window
window = tkinter.Tk()
window.title("Secret Notes")
window.minsize(width=500, height=500)
window.config(padx=20,pady=20)

# photo_label
img = tkinter.PhotoImage(file='secret.png')
photo_label = tkinter.Label(image=img,width=100, height=100)
photo_label.pack()

# title_label
title_label = tkinter.Label(text="Enter your title", font=('Arial', 10, 'normal'))
title_label.pack()

# title_entry
title_entry = tkinter.Entry(width=30)
title_entry.pack()

# secret_label
secret_label = tkinter.Label(text="Enter your secret", font=('Arial', 10, 'normal'))
secret_label.pack()

# secret_text
secret_text = tkinter.Text(width=40, height=10)
secret_text.pack()

# master_key_label
master_key_label = tkinter.Label(text="Enter master key", font=('Arial', 10, 'normal'))
master_key_label.pack()

# master_key_entry
master_key_entry = tkinter.Entry(width=30)
master_key_entry.pack()

# save function
def save_fnc():
    title = title_entry.get()
    secret = secret_text.get("1.0", tkinter.END)
    master = master_key_entry.get()

    if secret == "\n" or secret == "0" or master == "" or title == "":
        tkinter.messagebox.showerror("Error", "You should fill the Title, Secret and Master fields!")

    encrypted_string = cryptocode.encrypt(secret, master)

    with open("my_secret.txt", mode="a") as myFile:
        myFile.write(title)
        myFile.write("\n")
        myFile.write(encrypted_string)
        myFile.write("\n")
        myFile.close()

# decrypt function
def dec_fnc():

    secret = secret_text.get("1.0", tkinter.END)
    master = master_key_entry.get()

    if secret == "\n" or secret == "0" or master == "":
        tkinter.messagebox.showerror("Error", "You should fill the Secret and Master fields!")

    decrypted_string = cryptocode.decrypt(secret, master)
    secret_text.replace("1.0", tkinter.END, decrypted_string)

# save_button
save_button = tkinter.Button(text="Save & Encrypt", font=('Arial', 10, 'normal'), command=save_fnc)
save_button.pack()

# decrypt_button
decrypt_button = tkinter.Button(text="Decrypt", font=('Arial', 10, 'normal'), command=dec_fnc)
decrypt_button.pack()

window.mainloop()