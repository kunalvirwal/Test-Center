#webb browser
import webbrowser
import keyboard
import time

while True:     #shortcut catcher
        if keyboard.read_key()=="w":
            time.sleep(0.15)
            if keyboard.read_key()=="a":
                time.sleep(0.15)
                if keyboard.read_key()=="p":
                    print("\"wap\" command Detected!")#cmd
                    webbrowser.open("https://web.whatsapp.com/")
