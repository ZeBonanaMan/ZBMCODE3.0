import tkinter as tk
from tkinter import font

def calculate():   
    try:
        money = money_entry.get()
        price = price_entry.get()

        if not money or not price:
            result_label.config(text="Please enter valid money and price.")
            return
        
        money = float(money)
        price = float(price)

        if money <= 0:
            result_label.config(text="You're broke'...")
        
        elif money < price:
            result_label.config(text="Inflation is a beach...")

        else:
            max_apples = int(money / price)
            remaining_money = money - (max_apples * price)
        
            result_label.config(text=f"Maximum Apples: {max_apples}\nRemaining Money: ₱{remaining_money:.2f}")

    except ValueError:
         result_label.config(text="Hmm, I don't really know how to\ncompute these...")

root = tk.Tk()
root.geometry("1000x300")
root.title("Apple Buying Calculator")

custom_font = font.Font(family="fixedsys", size=20)

bg_color = "#2a2a2a"
fg_color = "#FFFFFF"
label_color = "#2d9dbd"
input_bg_color = "#545454"
button_bg_color = "#2a2a2a"
apple_color = "#ed2939"
money_color  ="#3cb043"

root.config(bg=bg_color)

left_frame = tk.Frame(bg=bg_color)
left_frame.pack(side=tk.LEFT, padx=10)

right_frame = tk.Frame(bg=bg_color)
right_frame.pack(side=tk.RIGHT, padx=10)

money_label = tk.Label(left_frame, text="Enter your Money:", bg=bg_color, fg=money_color, font=custom_font)
money_label.pack()
money_entry = tk.Entry(left_frame, bg=input_bg_color, fg=fg_color, font=custom_font)
money_entry.pack()

price_label = tk.Label(left_frame, text="Enter the Apple Price:", bg=bg_color, fg=apple_color, font=custom_font)
price_label.pack()
price_entry = tk.Entry(left_frame, bg=input_bg_color, fg=fg_color, font=custom_font)
price_entry.pack()

calculate_button = tk.Button(left_frame, text="Calculate!", command=calculate, bg=bg_color, fg=label_color, font=custom_font)
calculate_button.pack()

result_label = tk.Label(right_frame, text="Hi! I'll calculate your change\nfor you!", bg=bg_color, fg=label_color, font=custom_font)
result_label.pack()

root.mainloop()
