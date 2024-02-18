import keyboard
import time
import tkinter as TK
import psutil
import pywhatkit as kit
import webbrowser

###ytr
def browse(key):
    if key!="" or key.isspace():
        print("Topic:",key)
        root2.destroy()
        kit.playonyt(key)
        accept()
    
def popup():
    Top=TK.Label(root2,text="Search anything!",font=("Arial Bold",20),bg="White",fg="Red")
    Top.grid(column=1,row=1,sticky="e",padx=10,pady=20)
    keyword=TK.Entry(root2,width=30)
    keyword.grid(column=1,row=2,sticky="w",padx=10,pady=20)
    go=TK.Button(root2,text="Go!",font=("Arial",15),relief=TK.FLAT,bg="Red",fg="White",command=lambda:[browse(keyword.get())])
    go.grid(column=3,row=2,sticky="w",padx=10,pady=20)
    root2.protocol("WM_DELETE_WINDOW",lambda:[root2.destroy(),accept()])
    
#diagnostics
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
    root.protocol("WM_DELETE_WINDOW",lambda:[root.destroy(),accept()])

#shortcut
def accept():
    global root,img,img2,root2
    while True:     #shortcut catcher
        #dignostics
        if keyboard.read_key()=="s":
            time.sleep(0.15)
            if keyboard.read_key()=="s":
                time.sleep(0.15)
                if keyboard.read_key()=="d":
                    print("\"ssd\" command Detected!")#cmd
                    root=TK.Tk()
                    root.title("SSD")
                    root.geometry("350x300")
                    root.configure(bg="White")
                    img2 = TK.PhotoImage(file="background2.png")
                    label = TK.Label(root,image=img2)
                    label.place(x=-100, y=-5)
                    popup2()
                    break
        #ytr
        elif keyboard.read_key()=="y":
            time.sleep(0.15)
            if keyboard.read_key()=="t":
                time.sleep(0.15)
                if keyboard.read_key()=="r":
                    print("\"ytr\" command Detected!")#cmd
                    root2=TK.Tk()
                    root2.title("YTR")
                    root2.geometry("350x300")
                    root2.configure(bg="White")
                    img2 = TK.PhotoImage(file="background.png")
                    label = TK.Label(root2,image=img2)
                    label.place(x=-100, y=-5)
                    popup()
                    break
        elif keyboard.read_key()=="w":
            print("w")
            time.sleep(0.1)
            if keyboard.read_key()=="a":
                time.sleep(0.1)
                print('a')
                if keyboard.read_key()=="p":
                    time.sleep(0.1)
                print("\"wap\" command Detected!")#cmd
                webbrowser.open("https://web.whatsapp.com/")
                time.sssdleep(1)

print("Module loaded...")
accept()
try:
    root.mainloop()
except:
    try:
        root2.mainloop()
    except:
        print("n")
