import tkinter as tk # importing tkinter
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import messagebox

#main window
root=tk.Tk() 
root.title("cafe management") # it gives window a title 
window_width = 1500 
window_height = 750
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
centre_x=int(screen_width/2-window_width/2)
centre_y=int(screen_height/2-window_height/2)
root.geometry(f'{window_width}x{window_height}+{centre_x}+{centre_y}')
root.iconbitmap("C:/Users/Parija Sharma/.vscode/tkinter/coffee.ico") #this displays icon of your window
root.config(bg="#CFBCA3") 
#heading label
heading_label=tk.Label(root,text="CAFE MANAGEMENT SYSTEM",
                       font=("Georgia",26,"bold"),
                       anchor="center",
                       fg="#654321",
                       relief="raised",
                       bd=10) #this is main heading of window
heading2_label=tk.Label(root,text="-------------------Our cafe's best seller--------------------",
                        font=("Monotype Corsiva",16,"bold"),
                        anchor="center",
                        fg="#654321",
                        bg="#CFBCA3")
heading_label.grid(row=0,column=0,columnspan=8,pady=10)
heading2_label.grid(row=1,column=0,columnspan=8,pady=10)
#best seller panel
image_paths=[
    "C:/Users/Parija Sharma/OneDrive/Desktop/tkinter/Screenshot_20-10-2024_122333_www.bing.com.jpeg",
    "C:/Users/Parija Sharma/OneDrive/Desktop/tkinter/Frappe-Coffee.jpg",
    "C:/Users/Parija Sharma/OneDrive/Desktop/tkinter/brownie.jpeg",
    "C:/Users/Parija Sharma/OneDrive/Desktop/tkinter/burger.jpeg",
    "C:/Users/Parija Sharma/OneDrive/Desktop/tkinter/expresso.jpeg",
    "C:/Users/Parija Sharma/OneDrive/Desktop/tkinter/pizza.webp",
    "C:/Users/Parija Sharma/OneDrive/Desktop/tkinter/doughnuts.jpg",
    "C:/Users/Parija Sharma/OneDrive/Desktop/tkinter/Americano-coffee.jpg"
]
captions={
    "Cinnemon Roll":120,
            "Frappe Coffee":150,
            "Brownie":150,
            "Burger":80,
            "Espresso":150,
            "Pizza":260,
            "Doughnuts":85, 
            "Americano":120,}

selected_items=[]
total_price=0
# Inventory for each item
inventory = {item: 10 for item in captions.keys()}  # Default stock for all items
# Check if image paths and captions align
if len(image_paths) != len(captions):
    print("Error: The number of images does not match the number of items!")
    exit()
# Stock labels dictionary
stock_labels = {}

# Display images in a grid 
image_objects=[]
for index,(caption,price) in enumerate(captions.items()):
    try:
        img=Image.open(image_paths[index]).resize((100,100),Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        image_objects.append(img)
    except Exception as e:
        print(f"Error loading image at{caption}:{e}")
        continue
  
    stock_label = tk.Label(root, text=f"Stock: {inventory[caption]}", font=("Arial", 10), fg="green", bg="#CFBCA3")
    stock_label.grid(row=4, column=index % 10)
    stock_labels[caption] = stock_label
#buttons with their respective pictures:
    my_button=ttk.Button(root,image=img,command=lambda c=list(captions.keys())[index]:button_click(c))
    my_button.grid(row=2,column=index,padx=18, pady=10)
#Display the caption under each image
    caption_label=tk.Label(root,text=list(captions.keys())[index],font=("Monotype Corsiva",12,"bold"))
    caption_label.grid(row=3,column=index,padx=18,pady=10)


beveragemenu={
    'Espresso': 150,
    'Cappuccino': 100,
    'Latte': 120,
    'Americano': 120,
    'Frappe Coffee': 150,
    'Hot Chocolate': 50,
    'Iced Latte': 120,
    'Cold Brew': 100,
    'Tea': 100,
    'Fresh Lemonade': 80
    }
foodmenu={
    'Avocado Toast': 120,
    'Breakfast Sandwich (egg, cheese, bacon)': 120,
    'Veggie Wrap': 80,
    'Grilled Cheese': 100,
    'Caesar Salad': 200,
    'Burger': 80,
    'Pizza': 260,
    "Doughnuts":85,
    "Brownie":150,
    "Cinnemon Roll":120,
    }

selected_items=[]

def add_item():
    item=menu_combo.get().strip()
    if item:
        try:
            qty = int(quantity_entry1.get())
        except ValueError:
            messagebox.showwarning("Invalid Quantity", "Please enter a valid integer for quantity.")
            return
        if qty>0:  
            price=beveragemenu.get(item)
            if price is not None:
                selected_items.append((item,price*qty,qty))
                cart_listbox.insert(tk.END,f"{item}x{qty}- Rs{price*qty}")
                update_total()
            else:
                print("item not found")
        else:
            messagebox.showwarning("Invalid Quantity")
      
def add_item2():
    item=menu2_combo.get().strip()
    if item:
        try:
            qty=int(quantity_entry2.get())
        except ValueError:
            messagebox.showwarning("Invalid Quantity", "Please enter a valid integer for quantity.")
            return 
        if qty>0:
            price=foodmenu.get(item)
            if price is not None:
                selected_items.append((item,price*qty,qty))
                #print(f"you selected :{selected_items}\n")
                cart_listbox.insert(tk.END,f"{item}x{qty}- Rs{price*qty}")
                update_total()
            else:
                print("item not found")
        else:
            messagebox.showwarning("Invlid quantity", "Quantity must be greater than zero.")

#function to retrieve and validate quantity
def quantity():
    try:
        return int(quantity_entry.get())
    except ValueError:
        messagebox.showwarning("Invalid Quantity")
        return 1

# Function for adding an item to the cart
def button_click(caption):
    global total_price
    if inventory[caption]>0:
        qty = quantity()
        if inventory[caption] >= qty:  # Check if there is enough stock
            price=captions[caption]*qty
            selected_items.append((caption, price, qty))
            inventory[caption] -= qty  # Deduct correct quantity
            total_price += price
            cart_listbox.insert(tk.END, f"{caption} x{qty} - Rs.{price}")
            update_total()
            update_stock_labels()
        else:
            messagebox.showwarning("Out of Stock", f"Sorry, there are only {inventory[caption]} units of {caption} left.")


def update_total():
    global total_price
    total_price=sum(price for __, price,__ in selected_items)
    total_label.config(text=f"total : Rs{total_price}")

# Function to update stock labels
def update_stock_labels():
    for item, label in stock_labels.items():
        label.config(text=f"Stock: {inventory[item]}")
        if inventory[item] < 3:
            label.config(fg="red")
        else:
            label.config(fg="5C4033")

# Calculate tax
def tax(t=18):
    return (total_price * t) / 100

# Billing system to display detailed bill
def generate_bill():
    if selected_items:
        bill="\n".join([f"{item} : Rs {price}" for item , price ,qty in selected_items])
        total_price=sum(price for _,price, _ in selected_items)
        taxx=tax()
        total_with_tax=total_price+taxx
        bill += f"\n\nTotal Price: Rs {total_price:.2f}"
        bill+=f"\nTax: Rs{taxx:.2f}"
        bill+=f"\n\nTotal (inc.Tax): Rs {total_with_tax:.2f}"
        # Show the bill
        messagebox.showinfo("Bill", f"------ Your Bill ------\n\n{bill}")
    else:
        messagebox.showwarning("Empty Cart", "Your cart is empty. Please add items to the cart.")

def clear_cart():
    global selected_items, total_price
    for item, price, qty in selected_items:
        if item in inventory:
            inventory[item] += qty # Update inventory based on the quantity
        else:
            print(f"Warning: Item '{item}' not found in inventory.")
    selected_items.clear()
    cart_listbox.delete(0,tk.END)
    total_price=0
    update_total()
    update_stock_labels()
        

def Clear2_button():
    global selected_items, total_price
    selected_items.clear()
    menu_combo.delete(0,tk.END)
    selected_items = [item for item in selected_items if item[0] not in beveragemenu]
    #total_price=0
    #total_label.config(text="Total: Rs 0.00")

def Clear3_button():
    global selected_items, total_price
    selected_items.clear()
    menu2_combo.delete(0,tk.END)
    selected_items = [item for item in selected_items if item[0] not in foodmenu]
    #total_price=0
    #total_label.config(text="Total: Rs 0.00")

initial_items = {
     'Espresso': (150, 7),
    'Cappuccino': (100, 10),
    'Latte': (120, 8),
    'Americano': (120, 9),
    'Frappe Coffee': (150, 8),
    'Hot Chocolate': (50, 12),
    'Iced Latte': (120, 10),
    'Cold Brew': (100, 6),
    'Tea': (100, 15),
    'Fresh Lemonade': (80, 10),

    'Avocado Toast': (120, 5),
    'Breakfast Sandwich (egg, cheese, bacon)': (120, 7),
    'Veggie Wrap': (80, 10),
    'Grilled Cheese': (100, 10),
    'Caesar Salad': (200, 5),
    'Burger': (80, 10),
    'Pizza': (260, 4),
    'Doughnuts': (85, 12),
    'Brownie': (150, 5),
    'Cinnemon Roll': (120, 10)
}


def remove_item():
    selected_index = cart_listbox.curselection() 
    try:
        if selected_index:
            item_text = cart_listbox.get(selected_index)     
            cart_listbox.delete(selected_index)  
            item_name = item_text.split(" - Rs ")[0]
            item_price = int(item_text.split("Rs ")[1])
            selected_index.remove((item_name,item_price))
            update_total()
        else:
            messagebox.showwarning("Item not found",f"{item_name} was not found in the cart.") 
    except ValueError:
        messagebox.showwarning("error")


# Widgets for the GUI
# Quantity Entry Widget
quantity_label = tk.Label(root, text="^< Quantity for our Best Seller: >^", font=("Bookman Old Style", 10, "bold"), fg="#4A0909", bg="#E8B878", relief="raised", bd=3)
quantity_label.grid(row=9, column=3, columnspan=2, padx=10, pady=5)
quantity_entry = tk.Entry(root, width=10)
quantity_entry.grid(row=10, column=3, columnspan=2, padx=10, pady=5)
quantity_entry.insert(0, "1")  # Default quantity is 1

quantity_label = tk.Label(root, text="Quantity: >", font=("Bookman Old Style", 10, "bold"), fg="#4A0909", bg="#E8B878", relief="raised", bd=3)
quantity_label.grid(row=9, column=1, padx=10, pady=5)
quantity_entry1 = tk.Entry(root, width=5)
quantity_entry1.grid(row=10, column=1, padx=10, pady=5)
quantity_entry1.insert(0, "1")  # Default quantity is 1

quantity_label = tk.Label(root, text="< Quantity:", font=("Bookman Old Style", 10, "bold"), fg="#4A0909", bg="#E8B878", relief="raised", bd=3)
quantity_label.grid(row=9, column=6, padx=10, pady=5)
quantity_entry2 = tk.Entry(root, width=5)
quantity_entry2.grid(row=10, column=6, padx=10, pady=5)
quantity_entry2.insert(0, "1")  # Default quantity is 1

add_label=tk.Label(root,text="Select Beverage",font=("Bookman Old Style",12,"bold"),fg="#4A0909",bg="#E8B878",relief="raised",bd=5)
add_label.grid(row=9,column=2,padx=20,pady=5)

menu_combo=ttk.Combobox(root,values=list(beveragemenu.keys()),text="select beverage")
menu_combo.grid(row=10,column=2,padx=20,pady=5)

add_button=tk.Button(root,text="add to cart",command=add_item,font=("Bookman Old Style",10,"bold"),fg="#4A0909",bg="#E8B878",relief="raised",bd=4)
add_button.grid(row=11,column=2,padx=20,pady=5)

add2_label=tk.Label(root,text="Select Food Item",font=("Bookman Old Style",12,"bold"),fg="#4A0909",bg="#E8B878",relief="raised",bd=5)
add2_label.grid(row=9,column=5,padx=20,pady=5)

menu2_combo=ttk.Combobox(root,values=list(foodmenu.keys()),text="select a food item")
menu2_combo.grid(row=10,column=5,padx=20,pady=5)

add2_button=tk.Button(root,text="add to cart",command=add_item2,font=("Bookman Old Style",10,"bold"),fg="#4A0909",bg="#E8B878",relief="raised",bd=4)
add2_button.grid(row=11,column=5,padx=20,pady=5)

cart_listbox=tk.Listbox(root,width=50,height=9,selectmode="multiple") 
cart_listbox.grid(row=13,column=1,padx=20,pady=20,columnspan=2)
total_label=tk.Label(root,text="Total: Rs 0.00",width=15,font=("Bookman Old Style",12,"bold"),fg="#4A0909",bg="#E8B878",relief="raised",bd=5)
total_label.grid(row=12,column=4,padx=10,pady=20,columnspan=2,rowspan=2)


# Button to generate bill
bill_button = tk.Button(root, text="Generate Bill", command=generate_bill, font=("Bookman Old Style", 12, "bold"), fg="#4A0909", bg="#E8B878", relief="raised", bd=5)
bill_button.grid(row=12, column=6, columnspan=2,rowspan=2, pady=20)

clear2_button=tk.Button(root, text="Clear", command=Clear2_button, font=("Bookman Old Style", 8, "bold"), fg="#4A0909", bg="#E8B878", relief="raised", bd=5)
clear2_button.grid(row=12, column=2, pady=5,padx=5)

clear3_button=tk.Button(root, text="Clear", command=Clear3_button, font=("Bookman Old Style", 8, "bold"), fg="#4A0909", bg="#E8B878", relief="raised", bd=5)
clear3_button.grid(row=12, column=5, pady=5,padx=5)

clear_button=tk.Button(root, text=" Clear Cart ", command=clear_cart, font=("Bookman Old Style", 10, "bold"), fg="#4A0909", bg="#E8B878", relief="raised", bd=5)
clear_button.grid(row=12, column=3, pady=5, padx=15, rowspan=2)

remove_button = tk.Button(root, text="Remove Item", command=remove_item, font=("Bookman Old Style", 10, "bold"), fg="#4A0909", bg="#E8B878", relief="raised", bd=5)
remove_button.grid(row=14, column=1, pady=5, padx=15,columnspan=2)
root.mainloop()

