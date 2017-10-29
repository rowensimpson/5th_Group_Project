from tkinter import *


# StartPlane characteristics
StartPlane = Tk()
StartPlane.geometry('300x140')
StartPlane.title("Micro-grid control centre")


def mode_button_1_func():
    print("mode_button_1_func")


def mode_button_2_func():
    print("mode_button_2_func")


def mode_button_3_func():
    print("mode_button_3_func")


def mode_exe_func():
    print("mode_exe_func")


def unit1_call():
    print("unit1_clicked")
    unit_1_level = Toplevel()
    unit_1_level.title("Unit 1 viewer")


def unit2_call():
    print("unit2_clicked")
    unit_2_level = Toplevel()
    unit_2_level.title("Unit 2 viewer")


def unit3_call():
    print("unit3_clicked")
    unit_3_level = Toplevel()
    unit_3_level.title("Unit 3 viewer")


def unit4_call():
    print("unit4_clicked")
    unit_4_level = Toplevel()
    unit_4_level.title("Unit 4 viewer")


def mode_call():
    print("mode_clicked")
    mode_level = Toplevel()
    mode_level.geometry("200x200")
    mode_level.title("Mode selection")
    mode_button_1 = Button(mode_level, text="mode 1", command=mode_button_1_func).pack()
    mode_button_2 = Button(mode_level, text="mode 2", command=mode_button_2_func).pack()
    mode_button_3 = Button(mode_level, text="mode 3", command=mode_button_3_func).pack()
    mode_exe = Button(mode_level, text="execute", command=mode_exe_func).pack()


# button init
Unit1 = Button(StartPlane, text="Unit 1", command=unit1_call).place(x=10, y=10)
Unit2 = Button(StartPlane, text="Unit 2", command=unit2_call).place(x=10, y=40)
Unit3 = Button(StartPlane, text="Unit 3", command=unit3_call).place(x=10, y=70)
Unit4 = Button(StartPlane, text="Unit 4", command=unit4_call).place(x=10, y=100)
Mode = Button(StartPlane, text="Select Mode", command=mode_call).place(x=70, y=25)



# Label init
txt = StringVar()
Mode_Label = Label(StartPlane, text="Current Mode", anchor=CENTER, bg="red").place(x=70, y=55)
Mode_Txt = Label(StartPlane, text=txt, anchor=CENTER, bg="blue").place(x=80, y=80)

StartPlane.mainloop()
