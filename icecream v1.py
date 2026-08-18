import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import scrolledtext
from tkinter import messagebox

#constants
TITLE_FONT = "Comic Sans MS", 35
TEXT_FONT = "Comic Sans MS", 15
SUBTEXT_FONT = "Comic Sans MS", 8

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
        self.conecb = ttk.Combobox(root, values=list(cones.keys()), state="readonly")
        self.conecb.grid(row=4, column=0, sticky="nsew")

        # flavour combobox
        self.flavourcb = ttk.Combobox(root, values=list(flavours.keys()), state="readonly")
        self.flavourcb.grid(row=4, column=1, sticky="nsew")

        # topping combobox
        self.toppingcb = ttk.Combobox(root, values=list(toppings.keys()), state="readonly")
        self.toppingcb.grid(row=4, column=2, sticky="nsew", ipady = 5)

        #order part
        self.display1 = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg="lightblue", font=TEXT_FONT, width=30) #scrollable box !!
        self.display1.grid(row=1, column=3, sticky="nsew", rowspan=2, columnspan=2)
        self.display1.insert(tk.INSERT, "Order is empty.")
        self.display1.config(state=tk.DISABLED)

        #confirm order button
        self.confirmbtn = tk.Button(root, text="Confirm Order", bg="skyblue", font=TEXT_FONT, command=self.confirm_order)
        self.confirmbtn.grid(row=4, column=4, sticky="nsew")

        #add item to order button
        self.addbtn = tk.Button(root, text="Add item", bg="skyblue", font=TEXT_FONT, width=13, command=self.add_item)
        self.addbtn.grid(row=3, column=3, sticky="nsew")

        #remove item button
        self.removebtn = tk.Button(root, text="Remove items", bg="skyblue", font=TEXT_FONT, command=self.remove_item)
        self.removebtn.grid(row=4, column=3, sticky="nsew")

        self.neworderbtn = tk.Button(root, text="Start new order", bg="skyblue", font=TEXT_FONT, command=lambda: self.start_new_order())
        self.neworderbtn.grid(row=3, column=4, sticky="nsew")
    
    def confirm_order(self):
        """finalises order"""
        self.receipt, self.total = self.order_converter.finalise_order(order)
        print(self.receipt)
        print(self.total)
        # WORK IN PROGRESS AAAHHHHHH

        if order: # if order has items

            self.confirm_window = tk.Toplevel(root, bg="lightblue")
            self.confirm_window.title("Order Confirmation window")
            self.confirm_window.geometry("400x600")
            self.confirm_window.resizable(0, 0)
            self.confirm_window.transient(root)
            self.confirm_window.grab_set()

            self.lb1 = tk.Label(self.confirm_window, text="Order Confirmation window", font=TEXT_FONT)
            self.lb1.pack(pady=10)

            # create scrollbox for the order 
            self.display2 = scrolledtext.ScrolledText(self.confirm_window, wrap=tk.WORD, bg="white", font=TEXT_FONT, width=30, height=10)
            self.display2.pack(pady=10)
            self.display2.config(state=tk.NORMAL)
            self.display2.insert(tk.INSERT, self.receipt) 
            self.display2.config(state=tk.DISABLED)

            self.lb2 = tk.Label(self.confirm_window, text=(f"Your total is ${self.total}."), font=TEXT_FONT)
            self.lb2.pack(pady=10)

            self.btn1 = tk.Button(self.confirm_window, text="Go back to edit", font=TEXT_FONT, command = lambda:[self.confirm_window.destroy(), self.confirm_window.grab_release()])
            self.btn1.pack(pady=10)

            self.btn2 = tk.Button(self.confirm_window, text="Confirm order", font=TEXT_FONT)
            self.btn2.pack(pady=10)
        
        else: #if order is empty
            self.empty_order_warning()

    def add_item(self):
        """takes in user input from comboboxes and updates the sidebar with the according order"""
        # V4 FULLY FUNCTIONAL
        self.comboboxes = [self.conecb, self.flavourcb, self.toppingcb]

        if any(not cb.get().strip() for cb in self.comboboxes): #validation !!!
            self.show_combobox_warning()
        else:
            cone = self.conecb.get() 
            flavour = self.flavourcb.get()
            toppings = self.toppingcb.get()
            order.append([cone, flavour, toppings]) # add item to order list
            ordertext = self.order_converter.convert_to_text(order)

            self.display1.config(state=tk.NORMAL)
            self.display1.delete("1.0", tk.END) # clear display
            self.display1.insert(tk.INSERT, ordertext) # update scrollable textbox w/ neworder string
            self.display1.config(state=tk.DISABLED)
            pass

    def remove_item(self):
        """opens a seperate window that allows the user to select and remove items from their order"""
        # V5 SCROLLABLE BOX ADDED
        # could possibly look to decompose this as its quite big
        if order: #if there are items in order
            # initialise toplevel pop-out window
            self.selected_option = tk.StringVar(value=order[0])
            self.removal_window = tk.Toplevel(bg="lightblue")
            self.removal_window.title("Removal window")
            self.removal_window.geometry("400x550")
            self.removal_window.transient(root)
            self.removal_window.grab_set()

            self.lb1 = tk.Label(self.removal_window, text="Item removal window", font=TEXT_FONT)
            self.lb1.pack(pady=10)

            self.lb2 = tk.Label(self.removal_window, text="(The box below is scrollable.)", font=SUBTEXT_FONT)
            self.lb2.pack(pady=10)

            #initialise canvas frame for the scrollbox
            self.main_frame = ttk.Frame(self.removal_window)
            self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

            self.canvas = tk.Canvas(self.main_frame, highlightthickness=0)
            self.scrollbar = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.canvas.yview)

            self.scrollable_frame = ttk.Frame(self.canvas)

            self.scrollable_frame.bind(
                "<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
            )

            self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
            self.canvas.configure(yscrollcommand=self.scrollbar.set)

            # variable list for tracking what checkboxes are selected 
            self.var_list = []

            for index, value in enumerate(order): 
                # idk if u need the value variable there but it breaks if i get rid of it soooooo its here to stay
                self.statusvar = tk.BooleanVar()
                self.var_list.append(self.statusvar) # add new statusvar to list for tracking
                
                # convert each order into an appropriate textstring
                res = self.order_converter.convert_item_to_text(order, index)

                # create checkbox using the converted order textstring 
                self.cb = tk.Checkbutton(self.scrollable_frame, text=f"Item {index+1}: {res}", variable=self.statusvar)
                self.cb.pack(anchor="w")
            
            self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            def _on_mousewheel(event):
                self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
                    
            self.canvas.bind_all("<MouseWheel>", _on_mousewheel)

            self.btn1 = tk.Button(self.removal_window, text="Go back to edit", font=TEXT_FONT, 
            command = lambda:[self.removal_window.destroy(), self.removal_window.grab_release(), 
                              self.removal_window.unbind_all("<MouseWheel>")])
            self.btn1.pack(pady=10)

            self.btn2 = tk.Button(self.removal_window, text="Remove selected items from order", font=TEXT_FONT, 
            command= lambda: [self.remove_selected(), self.removal_window.destroy(), self.show_removal_info(), 
                              self.removal_window.grab_release(), self.removal_window.unbind_all("<MouseWheel>")])  
            # ok its a lot of commands but stuff breaks if i dont do this
            self.btn2.pack(pady=10)

        else:
            self.empty_order_warning()
        
    def remove_selected(self):
        """loops through the checkbox variable list and removes ticked items"""
        self.count = 0
        for i in range(len(self.var_list) -1, -1, -1): # Loops backward through the list to avoid indexing issues
            if self.var_list[i].get(): # if selected
                del order[i]
                del self.var_list[i]
                self.count += 1 
        print(order)
        ordertext = self.order_converter.convert_to_text(order)
        
        self.display1.config(state=tk.NORMAL)
        self.display1.delete("1.0", tk.END) # clear display
        self.display1.insert(tk.INSERT, ordertext) # update scrollable textbox w/ neworder string
        self.display1.config(state=tk.DISABLED)

    def show_removal_info(self):
        """creates a small popup box confirming item removal"""
        self.infobox1 = messagebox.showinfo("Success", f"Removed {self.count} items succesfully!")
    
    def show_combobox_warning(self):
        """small popup box"""
        self.infobox2 = messagebox.showerror("Error", "Please select an option for cone, flavour and topping!")

    def confirm_action(self):
        self.response = messagebox.askyesno("Confirmation", "Are you sure you want to proceed?")
        
        if self.response:
            return True
        else: 
            return False

    def empty_order_warning(self):
        """small popup box"""
        self.infobox2 = messagebox.showerror("Error", "You have no items in your order!")

    def start_new_order(self):
        """Resets the window back to it's starting state and resets the order."""
        order.clear() #clear list

        self.conecb.set('') #reset comboboxes
        self.flavourcb.set('')
        self.toppingcb.set('')

        self.display1.config(state=tk.NORMAL)
        self.display1.delete("1.0", tk.END) # clear display
        self.display1.config(state=tk.DISABLED)
        pass


class OrderConversions:
    """Collection of functions that convert the order 2D list into formatted text strings ready for GUI displays"""
    # im so proud of these and how they're implemented within their respective loops
    # 12-08-26 MASSIVELY simplified
    def convert_to_text(self, list_input):
        """converts the order 2d list to a formatted string."""
        res = "" # initialise variables
        for index, value in enumerate(list_input):
            individual_price = cones.get(list_input[index][0]) + flavours.get(list_input[index][1]) + toppings.get(list_input[index][2])
            res += (f"{list_input[index][0]} Cone, {list_input[index][1]} Flavour, {list_input[index][2]} Topping - ${individual_price} \n\n")

        return res.strip()

    def convert_item_to_text(self, list_input, position):
        """Converts a specified position of a 2D list into a formatted text string."""
        # literally just reused the same code as above slightly modified
        price = cones.get(list_input[position][0]) + flavours.get(list_input[position][1]) + toppings.get(list_input[position][2])
        res = (f"{list_input[position][0]} Cone, {list_input[position][1]} Flavour, {list_input[position][2]} Topping - ${price}") 
        return res.strip()
    
    def finalise_order(self, list_input):
        """converts the order into a biiiig textstring INCLUDING prices"""
        res = ""
        price = 0
        for index, value in enumerate(list_input):
            individual_price = cones.get(list_input[index][0]) + flavours.get(list_input[index][1]) + toppings.get(list_input[index][2])
            res += (f"{list_input[index][0]} Cone, {list_input[index][1]} Flavour, {list_input[index][2]} Topping - ${individual_price} \n\n")
            price += cones.get(list_input[index][0]) + flavours.get(list_input[index][1]) + toppings.get(list_input[index][2])
        return res.strip(), price

# main loop woohoo
root = tk.Tk()
app = OrderGui(root)
root.mainloop()