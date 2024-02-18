import keyboard
import time
import tkinter as TK
import psutil



def update():
    global Cpu,Ram
    ram=str(psutil.virtual_memory()[2])+'%'
    cpu=str(psutil.cpu_percent())+'%'
    Ram.config(text=ram)
    Cpu.config(text=cpu)
    Ram.after(200,update)
    
    
def popup2():
    global Cpu,Ram
    Top2=TK.Label(root,text="CPU:",font=("Arial Bold",20),bg="White",fg="Blue")
    Top2.grid(column=1,row=1,sticky="e",padx=10,pady=20)

    Cpu=TK.Label(root,font=("Arial Bold",20),bg="White",fg="Red")
    Cpu.grid(column=2,row=1,sticky="e",padx=10,pady=20)

    Top3=TK.Label(root,text="Ram:",font=("Arial Bold",20),bg="White",fg="Blue")
    Top3.grid(column=1,row=2,sticky="e",padx=10,pady=20)

    Ram=TK.Label(root,font=("Arial Bold",20),bg="White",fg="Red")
    Ram.grid(column=2,row=2,sticky="e",padx=10,pady=20)

    update()

def accept():
    global root,img
    while True:     #shortcut catcher
        if keyboard.read_key()=="s":
            time.sleep(0.15)
            if keyboard.read_key()=="s":
                time.sleep(0.15)
                if keyboard.read_key()=="d":
                    print("\"sssdytrsd\" command Detected!")#cmd
                    root=TK.Tk()
                    root.title("SSD")
                    root.geometry("350x300")
                    root.configure(bg="White")
                    img = TK.PhotoImage(file="background2.png")
                    label = TK.Label(root,image=img)
                    label.place(x=-100, y=-5)
                    popup2()
                    break
accept()
root.mainloop()
