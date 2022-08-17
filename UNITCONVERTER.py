from tkinter import *
measure1=""
measure2=""
def convert_SI(value, unit_input, unit_output):
    SI = {'Meter':1, 'Kilometer':1000, 'Centimeter':0.01, 'Millimeter':0.001,
          'Micrometer':0.000001, 'Mile':1609.35, 'Yard':0.9144, 'Foot':0.3048,
          'Inch':0.0254}
    return value*SI[unit_input]/SI[unit_output]


def select_input():
    global measure1
    measure1 = listbox.get(listbox.curselection())

def select_output():
    global measure2
    measure2 = listbox1.get(listbox1.curselection())

def converter():
    try:
        global measure1, measure2
        result.set(str(convert_SI(float(inputEntry.get()), measure1, measure2)))

    except:
        result.set("Error")




root=Tk()
root.title("Unit Converter")
root.geometry("500x400+500+400")
root.configure(background="black")
root.resizable(0,0)
canvas=Canvas(root,bg="White",height=325,width=400)
canvas.pack(pady=30)
title=lbl1=Label(canvas,text="UNIT  CONVERTER",font="Algerian",fg="Black",bg="White")
lbl1.place(x=120,y=20)
result=StringVar()
inputEntry = Entry(canvas,bg="Light grey",fg="Black")
inputEntry.place(x=40, y=80)
arrow = Label(canvas, text="---->", font="Calibri 20 bold",bg="White",fg="Black",relief=FLAT,)
arrow.place(x=190,y=120)
outputEntry = Entry(canvas,bg="Light grey",fg="Black", textvariable=result)
outputEntry.place(x=260,y=80)
convertButton = Button(canvas, text='Convert',bg="Light grey",fg="Black",relief=RIDGE, command=converter)
convertButton.place(x=190,y=160)

listbox = Listbox(canvas,bg="light grey",fg="black",exportselection=False)   #left listbox
listbox.place(x=40,y=120)
measurement_list = ['Meter', 'Kilometer', 'Centimeter', 'Millimeter',
                    'Micrometer', 'Mile', 'Yard', 'Foot', 'Inch']
for measure in measurement_list:
    listbox.insert(END, measure)
listbox.bind("<<ListboxSelect>>",lambda x: select_input())
listbox1 = Listbox(canvas,bg="light grey",fg="black", exportselection=False)   #right listbox
listbox1.place(x=260,y=120)

for measure in measurement_list:
    listbox1.insert(END, measure)
listbox1.bind( "<<ListboxSelect>>",lambda x: select_output())

root.mainloop()