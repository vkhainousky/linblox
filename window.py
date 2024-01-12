from tkinter import messagebox
try:
    from customtkinter import *
    from tkinter import *
    import os
    from CTkListbox import *
    from PIL import ImageTk, Image
    from pygame import mixer
    s = "Main"
    descs = ["LinBlox is a alt to Grapejuice and Vinegar but with simple gui\nYou can edit parameters in Settings tab!\nYou can also message me: waterdragon15102001@gmail.com\nTo players, from players.", "Attention!\nRoblox Player has been created by Roblox corp. not by the creator/creators of LinBlox!\nLinBlox Launcher created for you to play roblox on linux!", "Attention!\nRoblox Studio has been created by Roblox corp. not by the creator/creators of LinBlox!\nLinBlox Launcher created for you to play roblox on linux!\n(Requires MS Edge Web View 2 Runtime)", "Insert wine args"]
except Exception as ex:
    messagebox.showerror("Runtime error", ex)
    exit(2)
    
mixer.init()

def msweb2():
    try:
        print("0003: Install MS Edge Runtime")
        try:
            os.system("wine msedge/msw.exe")
        except:
            messagebox.showinfo("Make sure that you unzip msw.tar.xz file!")
    except Exception as ex:
        s = mixer.Sound('sound/error.mp3')
        s.play()
        messagebox.showerror("Error", ex)
def launch():
    try:
        print("0002: Roblox player exec")
        os.system("wine roblox/rp.exe " + args.get())
    except Exception as ex:
        s = mixer.Sound('sound/error.mp3')
        s.play()
        messagebox.showerror("Error", ex)
def studio():
    try:
        print("0002: Roblox studio exec")
        os.system("wine roblox/rs.exe " + args.get())
    except Exception as ex:
        s = mixer.Sound('sound/error.mp3')
        s.play()
        messagebox.showerror("Error", ex)
def change(c):
    try:
        global imgx
        s = profiles.get()
        print("0001:" + s)
        imgx = ImageTk.PhotoImage(Image.open("images/" + s + ".png").resize((64,64)))
        img.configure(image=imgx)
        title.configure(text=s)
        if (s == "Main"):
            title.configure(text="LinBlox")
            desc.configure(text=descs[0])
            args.place_forget()
            ststart.place_forget()
            rbstart.place_forget()
            mswebv.place_forget()
        if (s == "Player"):
            desc.configure(text=descs[1])
            args.place_forget()
            ststart.place_forget()
            rbstart.place(relx=0.60, rely=0.60, anchor=CENTER)
            mswebv.place_forget()
        if (s == "Studio"):
            desc.configure(text=descs[2])
            args.place_forget()
            ststart.place(relx=0.60, rely=0.60, anchor=CENTER)
            #mswebv.place(relx=0.60, rely=0.70, anchor=CENTER)
            rbstart.place_forget()
        if (s == "Settings"):
            desc.configure(text=descs[3])
            args.place(relx=0.60, rely=0.60, anchor=CENTER)
            ststart.place_forget()
            rbstart.place_forget()
            mswebv.place_forget()
    except Exception as ex:
        s = mixer.Sound('sound/error.mp3')
        s.play()
        messagebox.showerror("Runtime error", ex)
        exit(2)


root = CTk()
root.title("linblox launcher")
root.geometry("800x600")

profiles = CTkListbox(root,width=75, height=500, command=change)
profiles.place(relx=0.1,rely=0.5, anchor=CENTER)
profiles.insert(END, "Main")
profiles.insert(END, "Player")
profiles.insert(END, "Studio")
profiles.insert(END, "Settings")

imgx = ImageTk.PhotoImage(Image.open("images/Main.png").resize((64,64)))
img = CTkLabel(root, width=64, height=64, text="", image=imgx)
img.place(relx=0.60, rely=0.3, anchor=CENTER)

title = CTkLabel(root, text="LinBlox", font=CTkFont("Ubuntu", 32))
title.place(relx=0.60, rely=0.4, anchor=CENTER)

desc = CTkLabel(root, text="LinBlox is a alt to Grapejuice and Vinegar but with simple gui\nYou can edit parameters in Settings tab!\nYou can also message me: waterdragon15102001@gmail.com\nTo players, from players.", font=CTkFont("Ubuntu", 16), anchor="e", justify="left")
desc.place(relx=0.60, rely=0.5, anchor=CENTER)

args = CTkEntry(root, font=CTkFont("Ubuntu", 16))

ststart = CTkButton(root, font=CTkFont("Ubuntu", 16), text="Start Studio", command=studio)
mswebv = CTkButton(root, font=CTkFont("Ubuntu", 16), text="Install MS WebView2 (required)!", command=msweb2)
rbstart = CTkButton(root, font=CTkFont("Ubuntu", 16), text="Start Roblox", command=launch)

root.mainloop()

