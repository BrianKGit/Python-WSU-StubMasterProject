# GUI for events
import functionsModule as tm
from tkinter import ttk as ttk
import tkinter as tk
from PIL import ImageTk, Image
import ticketGUI


def runEventGUI(user):
    print('Event GUI started for: ' + user)

    # -------------------------------------------------------------------------------------------------
    # def area
    def history():
        purchases = tm.showUserPurchases(user)
        textArea.insert(tk.END, purchases + '\n')

    def toTicket():
        eventid = eventField.get()
        # choice = eventField.get()
        # id = found[int(choice)].get('_id')
        print(eventid)
        eventRoot.quit()
        eventRoot.destroy()
        ticketGUI.runTicketGUI(user, eventid)

    def getSelection():
        selection = keyCombo.get()
        return selection

    def getEntry():
        entry = field.get()
        return entry

    def search():
        textArea.delete('1.0', tk.END)
        key = getSelection()
        entry = getEntry()
        # results = tm.showAllEvents()
        if key == 'all':
            results = tm.showAllEvents()
        elif key == 'type':
            results = tm.searchSpecificEventType(key, entry)
        elif key == 'city' or key == 'state':
            results = tm.searchSpecificEventLocation(key, entry)
        else:
            results = tm.searchSpecificEvent(key, entry)
        print('In GUI')
        textArea.insert(tk.END, tm.eventHeader() + '\n')
        for each in results:
            prettyText = tm.eventFormat(each)
            # prettyText = ''
            # print(each.get('_id'))
            # prettyText += str(each.get('_id')) + '|\t'
            # prettyText += each.get('name') + '|\t'
            # prettyText += each.get('location').get('venue')
            textArea.insert(tk.END, prettyText + '\n')

    # -------------------------------------------------------------------------------------------------
    # build window
    XWIDTH = 800
    YHEIGHT = 600
    COLOR = '#4e83c9'
    COLOR2 = '#005aad'
    # main window and size
    eventRoot = tk.Tk()
    eventRoot.title('Events')
    canvas = tk.Frame(eventRoot, height=YHEIGHT, width=XWIDTH)
    canvas.pack()
    # sections of window
    welcomeArea = tk.Frame(eventRoot, bg=COLOR, padx=20, pady=5)
    welcomeArea.place(relheight=.2, relwidth=1)
    topArea = tk.Frame(eventRoot, bg=COLOR, padx=20, pady=10)
    topArea.place(rely=.2, relheight=.1, relwidth=1)
    bottomArea = tk.Frame(eventRoot, bg=COLOR, padx=20)
    bottomArea.place(rely=.3, relheight=1, relwidth=1)
    scroller = tk.Scrollbar(bottomArea)
    scroller.place(relx=.95, relheight=1)
    # -------------------------------------------------------------------------------------------------
    # middle tools
    # add drop down selection
    keyCombo = ttk.Combobox(topArea, font=50, width=10)
    keyCombo['values'] = ('all', 'name', 'city', 'state', 'type')
    keyCombo.pack(side='left', fill='y')

    # area to type search information
    field = tk.Entry(topArea, font=50)
    field.pack(side='left', fill='both', expand=True)

    # search button, takes info to the left and starts search
    searchButton = tk.Button(topArea, font=50, text='Search', width=10, command=search)
    searchButton.pack(side='right', fill='y')
    # -------------------------------------------------------------------------------------------------

    # area for bottom stuff
    bottomCanvas = tk.Canvas(bottomArea, bg=COLOR, yscrollcommand=scroller.set)
    bottomCanvas.place(relx=0, relheight=.7, relwidth=1)
    scroller.config(command=bottomCanvas.yview)
    # text display
    textArea = tk.Text(bottomCanvas, font='40')
    textArea.place(relx=0, relheight=1, relwidth=.75)

    # -------------------------------------------------------------------------------------------------
    # fill in bottom area with widgets
    bottomChoiceCanvas = tk.Canvas(bottomCanvas, bg=COLOR2)
    bottomChoiceCanvas.place(relx=.75, relheight=1, relwidth=.25)

    choiceLabel = tk.Label(bottomChoiceCanvas, text='Enter ID')
    choiceLabel.place(relx=.05, rely=.05, relwidth=.9, height=40)

    eventField = tk.Entry(bottomChoiceCanvas)
    eventField.place(relx=.05, rely=.15, relwidth=.9, height=40)

    goButton = tk.Button(bottomChoiceCanvas, font=50, text='Go',
                         command=toTicket)
    goButton.place(relx=.05, rely=.25, relwidth=.9, height=40)

    showHistoryButton = tk.Button(bottomChoiceCanvas, font=50, text='Show History',
                                  command=history)
    showHistoryButton.place(relx=.05, rely=.35, relwidth=.9, height=40)

    # -------------------------------------------------------------------------------------------------
    # Shows logo
    logo = tk.Canvas(welcomeArea)
    logo.place(relwidth=1, relheight=1)
    myFile = './Images/StubMaster.png'
    imageHead = Image.open(myFile)
    imageHead = imageHead.resize((750, 110), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(imageHead)

    logo.create_image(380, 55, image=img)
    # -------------------------------------------------------------------------------------------------

    eventRoot.mainloop()


# runEventGUI('box12')
