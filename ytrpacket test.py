import keyboard
import time
import tkinter as TK
import pywhatkit as kit

def browse(key):
    print("Topic:",key)
    root.destroy()
    kit.playonyt(key)
    accept()
    
def popup():
    Top=TK.Label(root,text="Search anything!",font=("Arial Bold",20),bg="White",fg="Red")
    Top.grid(column=1,row=1,sticky="e",padx=10,pady=20)
    keyword=TK.Entry(root,width=30)
    keyword.grid(column=1,row=2,sticky="w",padx=10,pady=20)
    go=TK.Button(root,text="Go!",font=("Arial",15),relief=TK.FLAT,bg="Red",fg="White",command=lambda:[browse(keyword.get())])
    go.grid(column=3,row=2,sticky="w",padx=10,pady=20)

def accept():
    global root,img
    while True:     #shortcut catcher
        if keyboard.read_key()=="y":
            time.sleep(0.15)
            if keyboard.read_key()=="t":
                time.sleep(0.15)
                if keyboard.read_key()=="r":
                    print("\"ytr\" command Detected!")#cmd
                    root=TK.Tk()
                    root.title("YTR")
                    root.geometry("350x300")
                    root.configure(bg="White")
                    img = TK.PhotoImage(file="background.png")
                    label = TK.Label(root,image=img)
                    label.place(x=-100, y=-5)
                    popup()
                    break
                

print("Module loaded...")
accept()
root.mainloop()
