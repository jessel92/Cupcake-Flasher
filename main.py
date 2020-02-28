'''
======================================================================================================================
Cupcake Flasher

by The Mad Noodle (Jesse Leventhal) & Roboto.NYC

v0.0.1 ALPHA

======================================================================================================================
'''



import os
import subprocess
import platform
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox as mb



def uploader():
    fw_var.get()
    print(fw_var.get())

    if fw_var.get() == "Motherboard Firmware v2.1":
         os.system("avrdude -c usbtiny -p m644p -U flash:w:firmware/MB-rrmbv12-v2.1r1.hex:a")

    elif fw_var.get() == "Motherboard Firmware v2.2":
         os.system("avrdude -c usbtiny -p m644p -U flash:w:firmware/MB-rrmbv12-v2.2r0.hex:a")

    elif fw_var.get() == "Motherboard Firmware v2.3":
         os.system("avrdude -c usbtiny -p m644p -U flash:w:firmware/MB-rrmbv12-v2.3r0.hex:a")

    elif fw_var.get() == "Motherboard Firmware v2.4":
         os.system("avrdude -c usbtiny -p m644p -U flash:w:firmware/MB-rrmbv12-v2.4.hex:a")

    elif fw_var.get() == "Motherboard Firmware v3.0":
         os.system("avrdude -c usbtiny -p m644p -U flash:w:firmware/MB-rrmbv12-v3.0.hex:a")

    elif fw_var.get() == "Motherboard Firmware v3.5":
        os.system("avrdude -c usbtiny -p m644p -U flash:w:firmware/MB-rrmbv12-v3.5.hex:a")

    elif fw_var.get() == "Extruder Controller Firmware v2.6 (Stepper | No Relay)":
        os.system("avrdude -c usbtiny -p m168 -U flash:w:firmware/EC-ecv22-v2.6-stepper-no-relays.hex:a")

    elif fw_var.get() == "Extruder Controller Firmware v2.6 (Stepper | Relay)":
        os.system("avrdude -c usbtiny -p m168 -U flash:w:firmware/EC-ecv22-v2.6-stepper-relays.hex:a")

    elif fw_var.get() == "Extruder Controller Firmware v3.0 (No Relay)":
        os.system("avrdude -c usbtiny -p m168 -U flash:w:firmware/EC-ecv22-v3.0-no-relays.hex:a")

    elif fw_var.get() == "Extruder Controller Firmware v3.0 (Relay)":
        os.system("avrdude -c usbtiny -p m168 -U flash:w:firmware/EC-ecv22-v3.0-relays.hex:a")

    elif fw_var.get() == "Extruder Controller Firmware v3.0 (Stepper | No Relay)":
        os.system("avrdude -c usbtiny -p m168 -U flash:w:firmware/EC-ecv22-v3.0-stepper-no-relays.hex:a")

    elif fw_var.get() == "Extruder Controller Firmware v3.0 (Stepper | Relay)":
        os.system("avrdude -c usbtiny -p m168 -U flash:w:firmware/EC-ecv22-v3.0-stepper-relays.hex:a")

    mb.showinfo("DONE!", "Flashing is Complete!")

window = Tk()

window.title("Cupcake Flasher v0.0.1")
#window.geometry('200x150')
window.iconbitmap('img/cf_icon.ico')

main_frame = Frame(window)
main_frame.pack()


logo_img = PhotoImage(file='img/logo.png')
title_lbl = Label(main_frame, image=logo_img, font='courier')
title_lbl.grid(columnspan=2, row=0, padx=5, pady=5)

fw_var = StringVar(main_frame)
fw_var.set("Motherboard Firmware v2.1") # initial value

option = OptionMenu(main_frame, fw_var,
                    "Motherboard Firmware v2.1",
                    "Motherboard Firmware v2.2",
                    "Motherboard Firmware v2.3",
                    "Motherboard Firmware v2.4",
                    "Motherboard Firmware v3.0",
                    "Motherboard Firmware v3.5",
                    "Extruder Controller Firmware v2.6 (Stepper | No Relay)",
                    "Extruder Controller Firmware v2.6 (Stepper | Relay)",
                    "Extruder Controller Firmware v3.0 (No Relay)",
                    "Extruder Controller Firmware v3.0 (Relay)",
                    "Extruder Controller Firmware v3.0 (Stepper | No Relay)",
                    "Extruder Controller Firmware v3.0 (Stepper | Relay)")
option.grid(column=1, row=1, padx=5, pady=5)


flash_btn = Button(main_frame, text="Flash", command=uploader)
flash_btn.grid(column=1, row=2, padx=5, pady=5)


window.mainloop()