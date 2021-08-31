from tkinter import *
from tkinter import filedialog
from ttkthemes import themed_tk as tk
from tkinter import messagebox
import os
from pydub import AudioSegment

def add_video():
    video = filedialog.askopenfilename(title='Select File', filetype=(('OGG files', '*.ogg'),))
    file_box.insert(END, video)

def delete():
    for item in reversed(file_box.curselection()):
        file_box.delete(item)

def convert():
    file_box.select_set(0, END)
    addresses = []
    for item in file_box.curselection():
        addresses.append(str(file_box.get(item)))
    for i in range(len(addresses)):
        filename = os.path.basename(addresses[i])
        filename = filename[:-3]+'mp3'
        ogg_audio = AudioSegment.from_ogg(addresses[i])
        ogg_audio.export(filename, format='mp3')
    if len(addresses) > 1:
        messagebox.showinfo("MP3 files Successfully Converted", "Your MP3 files were successfully created.\nCheck the folder where this program is located.")
    else:
        messagebox.showinfo("MP3 file Successfully Converted", "Your MP3 file was successfully created.\nCheck the folder where this program is located.")

screen = tk.ThemedTk()
screen.get_themes()
screen.set_theme("breeze")

width_of_window = 600
height_of_window = 430
screen_width = screen.winfo_screenwidth()
screen_height = screen.winfo_screenheight()
x_coordinate = int((screen_width/2) - (width_of_window/2))
y_coordinate = int((screen_height/2) - (height_of_window/2))
screen.geometry("{}x{}+{}+{}".format(width_of_window, height_of_window, x_coordinate, y_coordinate))

screen.title('OGG to MP3 Converter')
screen.iconbitmap('MP3.ico')
screen.config(background='#131260')

list_frame = Frame(screen)
list_frame.config(background='#131260')
my_scrollbar = Scrollbar(list_frame, orient=VERTICAL)
file_box = Listbox(list_frame, width=400, yscrollcommand=my_scrollbar.set, selectmode=MULTIPLE)
my_scrollbar.config(command=file_box.yview)
my_scrollbar.pack(side=RIGHT, fill=Y, pady=15)
list_frame.pack(padx=30)
file_box.pack(pady=15)

button_select = Button(screen, text='Select File', command=add_video, background='white', fg='black', font=('Helvetica', 16), borderwidth=5)
button_select.pack(pady=15)

button_delete = Button(screen, text='Delete File', command=delete, background='white', fg='black', font=('Helvetica', 12))
button_delete.pack(pady=15)

button_convert = Button(screen, text='CONVERT', command=convert, background='black', fg='white', font=('Helvetica', 18, 'bold'), borderwidth=6)
button_convert.pack(pady=15)

screen.mainloop()
