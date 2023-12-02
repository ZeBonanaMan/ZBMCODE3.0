import tkinter as tk
from tkinter import font

def display_apple_price():
    apple_price_label.config(text=f"Price of an apple: ₱{apple_price}")

def display_orange_price():
    orange_price_label.config(text=f"Price of an orange: ₱{orange_price}")

def calculate_cost():
    orange_input = orange_entry.get()
    apple_input = apple_entry.get()

    if not orange_input and not apple_input:
        total_cost_label.config(text="Please insert valid values")
        return
    
    if not orange_input.isdigit() and not apple_input.isdigit():   
        total_cost_label.config(text="Hmm, I don't really know how to \ncompute these...")

    elif not orange_input.isdigit() and not apple_input.isalpha():   
        total_cost_label.config(text="Your oranges seem to be\nnon-existent or an expression...")

    elif not orange_input.isalpha() and not apple_input.isdigit():   
        total_cost_label.config(text="Your apples seem to be\nnon-existent or an expression...")

    elif int(orange_input) > 900000000 and int(apple_input) > 900000000:   
        total_cost_label.config(text="I think we should respect your wallet...")
    
    else:
        orange_quantity = int(orange_input)
        apple_quantity = int(apple_input)
            
        orange_subtotal = orange_price * orange_quantity
        apple_subtotal = apple_price * apple_quantity

        total_cost = orange_subtotal + apple_subtotal 
        total_cost_label.config(text=f"The total cost of the oranges: ₱{orange_subtotal}\nThe total cost of the apples: ₱{apple_subtotal}\n\nTotal Cost: ₱{total_cost}")
        
apple_price = 20
orange_price = 25
    
bg_color = "#2a2a2a"
fg_color = "#FFFFFF"
label_color = "#2d9dbd"
input_bg_color = "#545454"
button_bg_color = "#2a2a2a"
apple_display_color = "#ed2939"
orange_display_color = "#eb5406"

win = tk.Tk()
win.geometry("1100x330")
win.title("Fruit Cost Calculator")

win.configure(bg=bg_color)

custom_font = font.Font(family="fixedsys", size=18)

left_frame = tk.Frame(win, bg=bg_color)
left_frame.pack(side=tk.LEFT, padx=10)

right_frame = tk.Frame(win, bg=bg_color)
right_frame.pack(side=tk.RIGHT, padx=10)

orange_label = tk.Label(left_frame, text="Enter quantity of oranges:", bg=bg_color, fg=fg_color, font=custom_font)
orange_label.pack()

orange_entry = tk.Entry(left_frame, width=10, bg=input_bg_color, font=custom_font)
orange_entry.pack()

apple_label = tk.Label(left_frame, text="Enter quantity of apples:", bg=bg_color, fg=fg_color, font=custom_font)
apple_label.pack()

apple_entry = tk.Entry(left_frame, width=10, bg=input_bg_color, font=custom_font)
apple_entry.pack()

calculate_button = tk.Button(left_frame, text="Calculate!", command=calculate_cost, bg=bg_color, fg=label_color, font=custom_font)
calculate_button.pack()

total_cost_label = tk.Label(right_frame, text="Hi! I will compute your cost for you.", bg=bg_color, fg=label_color, font=custom_font)
total_cost_label.pack()

apple_price_label = tk.Label(right_frame, text="", bg=bg_color, fg=apple_display_color, font=custom_font)
apple_price_label.pack()
display_apple_price()

orange_price_label = tk.Label(right_frame, text="", bg=bg_color, fg=orange_display_color, font=custom_font)
orange_price_label.pack()
display_orange_price()

win.mainloop()
