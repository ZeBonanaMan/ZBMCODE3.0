import tkinter as tk
from tkinter import font
from tkinter import colorchooser

def change_font():
    chosen_font = font.Font(family=font_family.get(), size=20)
    display_text.config(font=chosen_font)

def change_color():
    chosen_color = colorchooser.askcolor(title="Text Color")
    if chosen_color[1]:
        display_text.config(fg=chosen_color[1])

def submit_info():
    name = name_entry.get()
    age = age_entry.get()
    address = address_entry.get("1.0", "end-1c")
 
    if not name or not age or not address:
       
        display_text.config(state=tk.NORMAL)
        display_text.delete("1.0", tk.END)
        display_text.insert(tk.END, "You need to answer all my questions...")
        display_text.config(state=tk.DISABLED)

    elif not all(characters.isalpha() or characters.isspace() for characters in name):

        display_text.config(state=tk.NORMAL)
        display_text.delete("1.0", tk.END)
        display_text.insert(tk.END, "Please enter a valid name containing only letters.")
        display_text.config(state=tk.DISABLED)

    elif not age.isdigit() or int(age) > 120:

        display_text.config(state=tk.NORMAL)
        display_text.delete("1.0", tk.END)
        display_text.insert(tk.END, "Please enter a valid age between 1 and 120 using numbers only.")
        display_text.config(state=tk.DISABLED)
        
    else:
        display_text.config(state=tk.NORMAL)
        display_text.delete("1.0", tk.END)
        display_text.insert(tk.END, f"You are {name}\nAged {age} years old\nLiving in {address}")
        display_text.insert(tk.END, f"\n\nNice Meeting you!")
        display_text.config(state=tk.DISABLED)


def set_font_family(selected_font):
    font_family.set(selected_font)
    change_font()

root = tk.Tk()
root.title("User Info")

bg_color = "#2a2a2a"
fg_color = "#FFFFFF"
label_color = "#F28500"
input_bg_color = "#545454"
button_bg_color = "#2a2a2a"

root.configure(bg=bg_color)

left_frame = tk.Frame(root, bg=bg_color)
left_frame.pack(side=tk.LEFT, padx=10)

name_label = tk.Label(left_frame, text="Enter your name:", bg=bg_color, fg=label_color)
name_label.pack()
name_entry = tk.Entry(left_frame, bg=input_bg_color)
name_entry.pack()

age_label = tk.Label(left_frame, text="Enter your age:", bg=bg_color, fg=label_color)
age_label.pack()
age_entry = tk.Entry(left_frame, bg=input_bg_color)
age_entry.pack()

address_label = tk.Label(left_frame, text="Enter your address:", bg=bg_color, fg=label_color)
address_label.pack()
address_entry = tk.Text(left_frame, height=1, width=30, bg=input_bg_color)
address_entry.pack()

font_family = tk.StringVar(value="fixedsys")

font_label = tk.Label(left_frame, text="Font Family:", bg=bg_color, fg=label_color)
font_label.pack()
font_menu = tk.OptionMenu(left_frame, font_family, *font.families())
font_menu.config(bg=button_bg_color, fg=label_color)  
font_menu.pack()
font_button = tk.Button(left_frame, text="Change Font", command=change_font, bg=bg_color, fg=label_color)
font_button.pack()

color_button = tk.Button(left_frame, text="Text Color", command=change_color, bg=bg_color, fg=label_color)
color_button.pack()

right_frame = tk.Frame(root, bg=bg_color)
right_frame.pack(side=tk.RIGHT, padx=10)

display_text = tk.Text(right_frame, height=10, width=50, state=tk.DISABLED, bg=bg_color, fg=fg_color)
display_text.pack()

submit_button = tk.Button(right_frame, text="Submit", command=submit_info, bg=bg_color, fg=label_color)
submit_button.pack()

root.mainloop()