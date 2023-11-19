import subprocess
import tkinter
from commands import *

root = tkinter.Tk()

root.geometry("300x200")
root.resizable(False, False)
root.title("LinuxHarbor")

def discordInstall():
    subprocess.call(discord_install, shell=True)    
    
def chromiumInstall():
    subprocess.call(chromium_install, shell=True)

button_pip = tkinter.Button(
    root, 
    text="Install Discord", 
    font=('Arial', 18),
    command=discordInstall
)

button_tk = tkinter.Button(
    root, 
    text="Install Chromium", 
    font=('Arial', 18),
    command=chromiumInstall
)

button_pip.pack()
button_tk.pack()

root.mainloop()
