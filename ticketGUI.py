# GUI for tickets
import functionsModule as tm
import tkinter as tk
# from tkinter import tkk
from PIL import ImageTk, Image
import eventGUI as eg

ticketsArray = []


def runTicketGUI(user, id):
    print('------------------------------------')
    print('TicketGUI' + '\nUser: ' + user + '   ' + '\nEvent: ' + id)

    # ---------------------------------------------------------------------------------------------

    def sort():
        # Will replace this with sort method soon
        print('-------Showing tickets for this event--------')
        results = tm.searchTickets(id)
        ticketArea.delete('1.0', tk.END)
        # print the header before printing tickets
        ticketArea.insert(tk.END, tm.ticketHeader())
        i = 0

        for each in results:
            formattedTickets = tm.ticketFormat(each)
            ticketArea.insert(tk.END, formattedTickets + '\t' + str(i) + '\n')
            i += 1

    # def buildMap(myFileChoice, mapPlace):
    #     imageHead = Image.open(myFileChoice)
    #     imageHead = imageHead.resize((500, 300), Image.ANTIALIAS)
    #     img = ImageTk.PhotoImage(imageHead)
    #     mapPic = tk.Canvas(mapPlace)
    #     mapPic.place(relwidth=1, relheight=1)
    #     mapPic.create_image(280, 55, image=img)

    def addToCart():
        # first get balance and add ticket price to balance
        tickets = tm.searchTickets(id)
        print('==============================')
        choice = purchaseEntry.get()
        print('choice: ' + str(choice))
        price = tickets[int(choice)].get('price')
        print(price)
        print(balanceLabel['text'])
        newBalance = (float(balanceLabel['text']) + float(price))
        balanceLabel.configure(text=(newBalance))
        print('==============================')
        # next make that ticket sold: true
        ticketID = tickets[int(choice)].get('_id')
        print(ticketID)
        tm.setTicketToSold(ticketID)
        ticketsArray.append(tm.addToTicketArray(ticketID))
        ticketArea.delete('1.0', tk.END)
        sort()
        purchaseEntry.delete(0, tk.END)

    def checkout():
        print('checking out')
        total = str(balanceLabel['text'])
        checkoutString = 'Total spent: $' + total + '\n' + 'Thank you for your purchase!'
        ticketArea.delete('1.0', tk.END)
        ticketArea.insert(tk.END, checkoutString)
        # add tickets to user collection
        tm.toUserHistory(ticketsArray, user)
        ticketsArray.clear()

    def remove():
        print('You pressed the remove button')

    def backButton():
        print('Starting event GUI')
        ticketRoot.quit()
        ticketRoot.destroy()
        eg.runEventGUI(user)
    # ---------------------------------------------------------------------------------------------
    # Build window
    XWIDTH = 600
    YHEIGHT = 700
    COLOR = '#4e83c9'
    COLOR2 = '#005aad'
    # main window and size
    ticketRoot = tk.Tk()
    ticketRoot.title('Tickets')
    canvas = tk.Frame(ticketRoot, height=YHEIGHT, width=XWIDTH)
    canvas.pack()
    # sections of window
    mapArea = tk.Frame(ticketRoot, bg=COLOR, padx=20, pady=5)
    mapArea.place(relheight=.3, relwidth=1)
    topArea = tk.Frame(ticketRoot, bg=COLOR, padx=20, pady=10)
    topArea.place(rely=.3, relheight=.1, relwidth=1)
    bottomArea = tk.Frame(ticketRoot, bg=COLOR, padx=20)
    bottomArea.place(rely=.4, relheight=.7, relwidth=1)
    scroller = tk.Scrollbar(bottomArea)
    scroller.place(relx=.97, relheight=1)

    # ---------------------------------------------------------------------------------------------
    purchaseEntry = tk.Entry(topArea)
    purchaseEntry.place(relx=0, relwidth=.8, relheight=1)

    addButton = tk.Button(topArea, font=50, text='Add to cart', command=addToCart)
    addButton.place(relx=.8, relwidth=.2, relheight=1)

    bottomCanvas = tk.Canvas(bottomArea, bg=COLOR2, yscrollcommand=scroller.set)
    bottomCanvas.place(relx=0, relheight=1, relwidth=1)
    scroller.config(command=bottomCanvas.yview)

    ticketArea = tk.Text(bottomCanvas)
    ticketArea.place(relx=0, relheight=1, relwidth=.7)

    # Bottom right area
    userLabel = tk.Label(bottomCanvas, font=30, text=user, height=2)
    userLabel.place(relx=.71, rely=.05, relwidth=.27)

    totalLabel = tk.Label(bottomCanvas, font=30, text='Total', height=2)
    totalLabel.place(relx=.71, rely=.15, relwidth=.27)

    balanceLabel = tk.Label(bottomCanvas, font=30, height=2, text='0')
    balanceLabel.place(relx=.71, rely=.25, relwidth=.27)

    checkoutButton = tk.Button(bottomCanvas, font=30, text='Checkout', height=2, command=checkout)
    checkoutButton.place(relx=.71, rely=.4, relwidth=.27)

    goBack = tk.Button(bottomCanvas, font=30, text='Back', height=2, command=backButton)
    goBack.place(relx=.71, rely=.5, relwidth=.27)

    # # sort Combobox
    # sectionSelection = tkk.Combobox(bottomCanvas)
    # sectionSelection['values'] = ('A', 'B', 'C', 'D')
    # sectionSelection.place(relx=.71, rely=.6, relwidth=.27)

    # ---------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------
    # images
    venueArray1 = ['Hard Rock Cafe', 'Minnesota State Fairgrounds', 'State Theatre',
                   'Mayo Civic Center Auditorium', 'Olmsted County Fairgrounds', 'Armory',
                   'Ames Center', 'Orpheum Theatre', 'Planet Hollywood', 'Caesar\'s Palace']

    venueArray2 = ['US Bank Stadium']
    venueArray3 = ['Target Field', 'CHS Field']

    venueArray4 = ['Navy Pier']

    venue = tm.getVenue(id)

    if venue in venueArray1:
        myFile1 = './Images/seating.jpg'
        imageHead = Image.open(myFile1)
        imageHead = imageHead.resize((500, 300), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(imageHead)
        mapPic = tk.Canvas(mapArea)
        mapPic.place(relwidth=1, relheight=1)
        mapPic.create_image(280, 65, image=img)
        # buildMap(myFile2, mapArea)
    elif venue in venueArray2:
        myFile2 = './Images/fbStadium.png'
        imageHead = Image.open(myFile2)
        imageHead = imageHead.resize((500, 200), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(imageHead)
        mapPic = tk.Canvas(mapArea)
        mapPic.place(relwidth=1, relheight=1)
        mapPic.create_image(280, 100, image=img)
    elif venue in venueArray3:
        myFile3 = './Images/bbStadium.png'
        imageHead = Image.open(myFile3)
        imageHead = imageHead.resize((500, 180), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(imageHead)
        mapPic = tk.Canvas(mapArea)
        mapPic.place(relwidth=1, relheight=1)
        mapPic.create_image(280, 95, image=img)
    elif venue in venueArray4:
        myFile4 = './Images/iceRink.png'
        imageHead = Image.open(myFile4)
        imageHead = imageHead.resize((500, 180), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(imageHead)
        mapPic = tk.Canvas(mapArea)
        mapPic.place(relwidth=1, relheight=1)
        mapPic.create_image(280, 95, image=img)
    else:
        print('\t\tIn else')
        myFile5 = './Images/background.jpg'
        imageHead = Image.open(myFile5)
        imageHead = imageHead.resize((500, 300), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(imageHead)
        mapPic = tk.Canvas(mapArea)
        mapPic.place(relwidth=1, relheight=1)
        mapPic.create_image(280, 55, image=img)
        # buildMap(myFile2, mapArea)

    # for each in venueArray1:
    #     if venueArray1[each] == venue:
    #         myFile2 = './Images/seating.jpg'
    #
    #         imageHead2 = Image.open(myFile2)
    #         imageHead2 = imageHead2.resize((500, 300), Image.ANTIALIAS)
    #         img2 = ImageTk.PhotoImage(imageHead2)
    #         mapPic2 = tk.Canvas(mapArea)
    #         mapPic2.place(relwidth=1, relheight=1)
    #         mapPic2.create_image(280, 55, image=img2)

    # ---------------------------------------------------------------------------------------------
    sort()
    ticketRoot.mainloop()


# this will open this window directly
runTicketGUI('box12', 'avengers')
