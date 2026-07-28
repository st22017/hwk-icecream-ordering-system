import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

#constants
TITLE_FONT = "Comic Sans MS", 35
TEXT_FONT = "Comic Sans MS", 15

cones = ["Sugar", "Waffle", "Cake"]
flavours = ["Vanilla", "Chocolate", "Strawberry", "Hokey Pokey"]
toppings = ["Chocolate", "Chocolate Flake", "Cherry", "Sprinkles"]

class OrderGui:
    """gui setup"""
    def __init__(self, root):
        self.root = root
        self.root.title("Ordering Program")
        self.root.geometry ("1280x720")
        self.root.resizable(0, 0)

        self.root.columnconfigure([0, 1, 2, 3], weight=1)
        self.root.rowconfigure([0, 1, 2], weight=1)

        # gui layout
        self.title = tk.Label(root, text="Howick Icy Treats", bg="lightblue", font=TITLE_FONT)
        self.title.grid(row=0, column=0, sticky="nsew", columnspan=3)

        self.orderlb = tk.Label(root, text="Your Order:", bg="skyblue", font=TEXT_FONT)
        self.orderlb.grid(row=0, column=3, sticky="nsew")

        self.img1 = tk.PhotoImage(file="wafflecone.png")
        self.img1lb = tk.Label(root, image=self.img1, width=22)
        self.img1lb.grid(row=1, column=0, sticky="nsew", rowspan = 2)

        self.img2 = tk.Label(root, text="Image Placeholder", bg="lightgreen", width=22)
        self.img2.grid(row=1, column=1, sticky="nsew", rowspan = 2)

        self.img3 = tk.Label(root, text="Image Placeholder", bg="lightgreen", width=22, height=25)
        self.img3.grid(row=1, column=2, sticky="nsew", rowspan = 2)

        self.conelb = tk.Label(root, text="Cone", bg="skyblue", font=TEXT_FONT)
        self.conelb.grid(row=3, column=0, sticky="nsew")

        self.flavourlb = tk.Label(root, text="Flavour", bg="skyblue", font=TEXT_FONT)
        self.flavourlb.grid(row=3, column=1, sticky="nsew")

        self.toppinglb = tk.Label(root, text="Topping", bg="skyblue", font=TEXT_FONT, height=3)
        self.toppinglb.grid(row=3, column=2, sticky="nsew")

        self.conesl = ttk.Combobox(root, values=cones, state="readonly")
        self.conesl.grid(row=4, column=0, sticky="nsew")

        self.flavoursl = ttk.Combobox(root, values=flavours, state="readonly")
        self.flavoursl.grid(row=4, column=1, sticky="nsew")

        self.toppingsl = ttk.Combobox(root, values=toppings, state="readonly")
        self.toppingsl.grid(row=4, column=2, sticky="nsew", ipady = 5)

        self.display = tk.Label(root, text="(placeholder)", bg="lightblue")
        self.display.grid(row=1, column=3, sticky="nsew", rowspan=2)

        self.confirmbtn = tk.Button(root, text="Confirm Order", bg="skyblue", font=TEXT_FONT, command=self.ConfirmOrder)
        self.confirmbtn.grid(row=3, column=3, sticky="nsew", rowspan=2)
    
    def ConfirmOrder(self):
        cone = self.conesl.get()
        flavour = self.flavoursl.get()
        toppings = self.toppingsl.get()

        print(cone)
        print(flavour)
        print(toppings)
        pass

root = tk.Tk()
app = OrderGui(root)
root.mainloop()