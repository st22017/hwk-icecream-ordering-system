import tkinter as tk
from tkinter import ttk

#constants
TITLE_FONT = "Comic Sans MS", 35

cones = ["Sugar", "Waffle", "Cake"]
flavours = ["Vanilla", "Chocolate", "Strawberry", "Hokey Pokey"]
toppings = ["Chocolate", "Chocolate Flake", "Cherry", "Sprinkles"]

def ConfirmOrder():
    cone = conesl.get()
    flavour = flavoursl.get()
    toppings = toppingsl.get()

    print(cone)
    print(flavour)
    print(toppings)
    pass


root = tk.Tk()
root.title("Ordering Program")
root.geometry ("1280x720")
root.resizable(0, 0)

root.columnconfigure([0, 1, 2, 3], weight=1)
root.rowconfigure([0, 1, 2], weight=1)

# gui layout
title = tk.Label(root, text="Howick Icy Treats", bg="lightblue", font=TITLE_FONT)
title.grid(row=0, column=0, sticky="nsew", columnspan=3)

orderlb = tk.Label(root, text="Your Order:", bg="skyblue")
orderlb.grid(row=0, column=3, sticky="nsew")

img1 = tk.Label(root, text="Image Placeholder", bg="lightgreen")
img1.grid(row=1, column=0, sticky="nsew", rowspan = 2)

img2 = tk.Label(root, text="Image Placeholder", bg="lightgreen")
img2.grid(row=1, column=1, sticky="nsew", rowspan = 2)

img3 = tk.Label(root, text="Image Placeholder", bg="lightgreen", height=25)
img3.grid(row=1, column=2, sticky="nsew", rowspan = 2)

conelb = tk.Label(root, text="Cone", bg="skyblue")
conelb.grid(row=3, column=0, sticky="nsew")

flavourlb = tk.Label(root, text="Flavour", bg="skyblue")
flavourlb.grid(row=3, column=1, sticky="nsew")

toppinglb = tk.Label(root, text="Topping", bg="skyblue", height=5)
toppinglb.grid(row=3, column=2, sticky="nsew")

conesl = ttk.Combobox(root, values=cones, state="readonly")
conesl.grid(row=4, column=0, sticky="nsew")

flavoursl = ttk.Combobox(root, values=flavours, state="readonly")
flavoursl.grid(row=4, column=1, sticky="nsew")

toppingsl = ttk.Combobox(root, values=toppings, state="readonly")
toppingsl.grid(row=4, column=2, sticky="nsew", ipady = 5)

display = tk.Label(root, text="(placeholder)", bg="lightblue")
display.grid(row=1, column=3, sticky="nsew", rowspan=2)

confirmbtn = tk.Button(root, text="Confirm Order", bg="skyblue", command=lambda:ConfirmOrder())
confirmbtn.grid(row=3, column=3, sticky="nsew", rowspan=2)

print("test")

root.mainloop()

