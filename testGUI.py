# builds and shows the gui for the program
import pprint
import testMod as tm
from tkinter import ttk as ttk
import tkinter as tk
from PIL import ImageTk, Image
import ticketGUI
import itertools
# import sys
# print(sys.path)
# print(sys.version)


def testPotatoButton():
    print('The potato has landed')


def getSelection():
    selection = keyCombo.get()
    return selection


def getEntry():
    entry = field.get()
    return entry


def allEvents():
    # first will have to clear canvas
    print('---------------')
    results = tm.showAllEvents()
    print('In GUI')
    labelArray = ['', '', '', '', '', '', '', '']
    buttonArray = ['', '', '', '', '', '', '', '']
    tempFrame = ['', '', '', '', '', '', '', '']
    eventid = ['elvis', 'avengers', 'vikings', 'soundset', 'swan', 'paw', 'circus', 'twins', 'saints', 'godsmack', 'narnia', 'dolly', 'reagan', 'jefferies']
    i = 0
    for each in results:
        print(tm.formatEvents(each))
        tempFrame[i] = tk.Frame(bottomCanvas, height=80)
        tempFrame[i].pack(side='top', fill='x')
        labelArray[i] = tk.Label(tempFrame[i], text=(tm.formatEvents(each)))
        # labelArray[i] = tk.Label(tempFrame[i], text=(pprint.pformat(each,
        # indent=4)))
        labelArray[i].place(relx=0, relwidth=.9, relheight=1)
        buttonArray[i] = tk.Button(tempFrame[i], text=each.get('name'),
                                   command=ticketGUI.openTickets(each.get('name')))
        buttonArray[i].place(relx=.9, relwidth=.1, relheight=1)
        i = i+1


def search():
    print('---------------')
    key = keyCombo.get()
    entry = field.get()
    results = tm.searchEvents(key, entry)
    print('In GUI')

    for each in results:
        prettyText = pprint.pformat(each, indent=4)
        textArea.insert(tk.INSERT, prettyText + '\n\n')


XWIDTH = 600
YHEIGHT = 600
COLOR = '#4e83c9'
COLOR2 = '#8a00ad'
# main window and size
root = tk.Tk()
root.title('Events')
canvas = tk.Frame(root, height=YHEIGHT, width=XWIDTH)
canvas.pack()
# sections of window
welcomeArea = tk.Frame(root, bg=COLOR, padx=20, pady=5)
welcomeArea.place(relheight=.2, relwidth=1)
topArea = tk.Frame(root, bg=COLOR, padx=20, pady=10)
topArea.place(rely=.2, relheight=.1, relwidth=1)
bottomArea = tk.Frame(root, bg=COLOR, padx=20)
bottomArea.place(rely=.3, relheight=1, relwidth=1)
scroller = tk.Scrollbar(bottomArea)
scroller.place(relx=.95, relheight=1)

# welcome label shows logo
wel = tk.Canvas(welcomeArea)
wel.place(relwidth=1, relheight=1)
myFile = 'StubMaster.png'
imageHead = Image.open(myFile)
imageHead = imageHead.resize((560, 107), Image.ANTIALIAS)
img = ImageTk.PhotoImage(imageHead)

wel.create_image(280, 55, image=img)

# add drop down selection
keyCombo = ttk.Combobox(topArea, font=50, width=10)
keyCombo['values'] = ('name', 'city', 'state', 'type')
keyCombo.pack(side='left', fill='y')

# area to type search information
field = tk.Entry(topArea, font=50)
field.pack(side='left', fill='both', expand=True)

# search button, takes info to the left and starts search
searchButton = tk.Button(topArea, font=50, text='Search', width=10,
                         command=allEvents)
# searchButton = tk.Button(topArea, font=50, text='Search', width=10,
#                          command=search)
searchButton.pack(side='right', fill='y')

# shows frame version of those events
bottomCanvas = tk.Canvas(bottomArea, bg=COLOR2, yscrollcommand=scroller.set)
bottomCanvas.place(relx=0, relheight=1, relwidth=.95)
scroller.config(command=bottomCanvas.yview)
# ----------------------------------------
# previous version display Textual information here
# textArea = tk.Text(bottomArea, font='50')
# textArea.place(relheight=1, relwidth=1)
# -----------------------------------------


root.mainloop()

# myList = tk.Listbox(bottomArea, yscrollcommand=scroller.set)
# for line in range(100):
#     # myList.insert(tk.END, '***********' + str(line))
#     temp = tk.frame(bottomArea, bg=COLOR2, padx=20, height=80)
#     temp.pack(fill='x')
# myList.pack(side='left', fill='both')
# scroller.config(command=myList.yview)
