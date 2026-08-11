import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import scrolledtext

#constants
TITLE_FONT = "Comic Sans MS", 35
TEXT_FONT = "Comic Sans MS", 15

cones = {"Sugar": 1, "Waffle": 2, "Cake": 2}
flavours = {"Vanilla": 3, "Chocolate": 3, "Strawberry": 4, "Hokey Pokey": 3.5, "Soft Serve": 2.5}
toppings = {"Chocolate": 2, "Chocolate Flake": 2.5, "Cherry": 2, "Sprinkles": 1, "Strawberry Syrup": 1.5}

order = [] #initialise list

class OrderGui:
    
    def __init__(self, root):
        """gui setup"""
        #initialisation
        self.root = root
        self.root.title("Ordering Program")
        self.root.geometry ("1280x720")
        self.root.resizable(0, 0)
        
        self.order_converter = OrderConversions()

        self.root.columnconfigure([0, 1, 2], weight=1)
        self.root.rowconfigure([0, 1, 2, 3], weight=1)

        # gui layout

        # title
        self.title = tk.Label(root, text="Howick Icy Treats", bg="lightblue", font=TITLE_FONT, height=2)
        self.title.grid(row=0, column=0, sticky="nsew", columnspan=3)

        # order label
        self.orderlb = tk.Label(root, text="Your Order:", bg="skyblue", font=TEXT_FONT)
        self.orderlb.grid(row=0, column=3, sticky="nsew", columnspan=2)

        # cone image
        self.img1 = tk.PhotoImage(file="wafflecone.png")
        self.img1lb = tk.Label(root, image=self.img1, width=22)
        self.img1lb.grid(row=1, column=0, sticky="nsew", rowspan = 2)

        # resize image
        self.img2 = Image.open("neapolitan-ice-cream.png")
        self.img2resize = self.img2.resize((300, 350), Image.LANCZOS)
        self.tk_img2 = ImageTk.PhotoImage(self.img2resize)
        # place into grid + label
        self.img2lb = tk.Label(root, image=self.tk_img2, width=22)
        self.img2lb.grid(row=1, column=1, sticky="nsew", rowspan = 2)

        # topping image
        self.img3 = Image.open("99_ice_cream.png")
        self.img3resize = self.img3.resize((300, 450), Image.LANCZOS)
        self.tk_img3 = ImageTk.PhotoImage(self.img3resize)
        self.img3lb = tk.Label(root, image=self.tk_img3, width=22, height=25)
        self.img3lb.grid(row=1, column=2, sticky="nsew", rowspan = 2)

        # cone label
        self.conelb = tk.Label(root, text="Cone", bg="skyblue", font=TEXT_FONT)
        self.conelb.grid(row=3, column=0, sticky="nsew")

        # flavour label
        self.flavourlb = tk.Label(root, text="Flavour", bg="skyblue", font=TEXT_FONT)
        self.flavourlb.grid(row=3, column=1, sticky="nsew")

        # topping label
        self.toppinglb = tk.Label(root, text="Topping", bg="skyblue", font=TEXT_FONT, height=3)
        self.toppinglb.grid(row=3, column=2, sticky="nsew")

        # cone combobox
        self.conesl = ttk.Combobox(root, values=list(cones.keys()), state="readonly")
        self.conesl.grid(row=4, column=0, sticky="nsew")

        # flavour combobox
        self.flavoursl = ttk.Combobox(root, values=list(flavours.keys()), state="readonly")
        self.flavoursl.grid(row=4, column=1, sticky="nsew")

        # topping combobox
        self.toppingsl = ttk.Combobox(root, values=list(toppings.keys()), state="readonly")
        self.toppingsl.grid(row=4, column=2, sticky="nsew", ipady = 5)

        #order part
        self.display = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg="lightblue", font=TEXT_FONT, width=30) #scrollable box !!
        self.display.grid(row=1, column=3, sticky="nsew", rowspan=2, columnspan=2)
        self.display.insert(tk.INSERT, "Order is empty.")
        self.display.config(state=tk.DISABLED)

        #confirm order button
        self.confirmbtn = tk.Button(root, text="Confirm Order", bg="skyblue", font=TEXT_FONT, command=self.ConfirmOrder)
        self.confirmbtn.grid(row=3, column=4, sticky="nsew", rowspan=2)

        #add item to order button
        self.addbtn = tk.Button(root, text="Add item", bg="skyblue", font=TEXT_FONT, width=13, command=self.AddItem)
        self.addbtn.grid(row=3, column=3, sticky="nsew")

        #remove item button
        self.removebtn = tk.Button(root, text="Remove item", bg="skyblue", font=TEXT_FONT, command=self.RemoveItem)
        self.removebtn.grid(row=4, column=3, sticky="nsew")
    
    def ConfirmOrder(self):
        cone = self.conesl.get()
        flavour = self.flavoursl.get()
        toppings = self.toppingsl.get() #later ur gonna have to query the dictionary using the keys from the order to get the total so thats gonna be fun

        print(cone)
        print(flavour)
        print(toppings) #placeholder for now
        pass

    def AddItem(self):
        """takes in user input from comboboxes and updates the sidebar with the according order"""
        cone = self.conesl.get() # V3 REFORMATTED WITH A SCROLLABLE SIDEBAR - STILL LACKS VALIDATION
        flavour = self.flavoursl.get()
        toppings = self.toppingsl.get()
        order.append([cone, flavour, toppings]) # add item to order list
        ordertext = self.order_converter.convert_to_text(order)

        self.display.config(state=tk.NORMAL)
        self.display.delete("1.0", tk.END) # clear display
        self.display.insert(tk.INSERT, ordertext) # update scrollable textbox w/ neworder string
        self.display.config(state=tk.DISABLED)
        pass

    def RemoveItem(self):
        """opens a seperate window that allows the user to select and remove items from their order"""
        # V2 WE ARE SO BACK ALL THE INTERNAL WORKINGS FOR TEXT FORMATTING ARE TIDY AND GOOD TO GO  
        # Still wip is the stylisation and allat and also the actual item removal part lol
        self.selected_option = tk.StringVar(value=order[0])

        # initialise toplevel pop-out window
        self.removal_window = tk.Toplevel(root, bg="lightblue")
        self.removal_window.title("Removal window")
        self.removal_window.geometry("400x500")
        self.root.resizable(0, 0)

        # variable list for tracking what checkboxes are selected 
        self.var_list = []

        self.lb1 = tk.Label(self.removal_window, text="Item removal window", font=TEXT_FONT)
        self.lb1.pack(pady=20)

        for index, value in enumerate(order): 
            # idk if u need the value variable there but it breaks if i get rid of it soooooo its here to stay
            self.statusvar = tk.BooleanVar()
            self.var_list.append(self.statusvar) # add new statusvar to list for tracking

            # convert each order into an appropriate textstring
            res = self.order_converter.convert_item_to_text(order, index)

            # create checkbox using the converted order textstring 
            self.cb = tk.Checkbutton(self.removal_window, text=f"Item {index+1}: {res}", variable=self.statusvar)
            self.cb.pack(anchor="w")

        self.btn1 = tk.Button(self.removal_window, text="Remove selected items from order", font=TEXT_FONT, command= lambda: [self.remove_selected(), self.removal_window.destroy()]) 
        self.btn1.pack(pady=20) #needs an extra popup window to notify user that item Has Been Removed
        
    def remove_selected(self):
        for index, var in enumerate(self.var_list): #yo theres a Bug 
            if var.get():
                del order[index]
                del self.var_list[index]
        print(order)



class OrderConversions:
    """Collection of functions that convert the order 2D list into formatted text strings ready for GUI displays"""
    # im so proud of these and how they're implemented within their respective loops
    # 12-08-26 MASSIVELY simplified
    def convert_to_text(self, list_input):
        """converts the order 2d list to a formatted string."""
        res = "" # initialise variables
        for index, value in enumerate(list_input):
            res += (f"{list_input[index][0]} Cone, {list_input[index][1]} Flavour, {list_input[index][2]} Topping \n\n")

        return res.strip()

    def convert_item_to_text(self, list_input, position):
        """Converts a specified position of a 2D list into a formatted text string."""
        # literally just reused the same code as above slightly modified
        res = (f"{list_input[position][0]} Cone, {list_input[position][1]} Flavour, {list_input[position][2]} Topping") 
        return res.strip()



root = tk.Tk()
app = OrderGui(root)
root.mainloop()