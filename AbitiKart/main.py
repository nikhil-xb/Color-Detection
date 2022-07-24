from tkinter import * 
import tkinter
from tkinter.filedialog import askopenfile
import time
from tkinter.ttk import *
BACKGROUND_COLOR= "#B1DDC6"

window= tkinter.Tk()
window.title("Color Detection Program- Abitikart")
window.config(padx=50, pady=50)

canvas= Canvas(width=200, height=200)
logo= PhotoImage(file= "Abitikart Logo.png")
canvas.create_image(100, 100, image= logo)
canvas.grid(row=0, column=1)

def open_file():
    file_path= askopenfile(mode='a',title="Select File", filetypes=[("PNG Files", "*.png"),("All Files", ".**")])
    if file_path is not None:
        pass    
def uploadFiles():
    pb= Progressbar(window, orient=HORIZONTAL, length= 300, mode='determinate')
    pb.grid(row=3, columnspan=3, pady=20)
    for i in range(5):
        window.update_idletasks()
        pb['value']+= 20
        time.sleep(1)
    pb.destroy()
    Label(window, text='File Uploaded Successfully',
    foreground='green').grid(row=3,column=1, columnspan=2)


#SETUP
pic_file= Label(text="Upload File in png form: ")
pic_file.grid(row=1, column=0)

pic_btn= Button(window, text="Choose File",width=40, command=lambda:open_file())
pic_btn.grid(row=1, column=1, columnspan=2)

upld= Button(window, text="Uplaod Files", command= uploadFiles)
upld.grid(row=2,column=1, columnspan=2)


window.mainloop()