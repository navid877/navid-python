import phonenumbers
from phonenumbers import timezone, geocoder, carrier
import tkinter as tk
from tkinter import messagebox

def get_phone_info():
    number = phone_entry.get()
    
    try:
        phone = phonenumbers.parse(number)
        time_zone = timezone.time_zones_for_number(phone)
        operator = carrier.name_for_number(phone, "en")
        region = geocoder.description_for_number(phone, "en")

        result_text = f"Details: {phone}\nTime zone: {time_zone}\nOperator: {operator}\nRegion: {region}"
        result_label.config(text=result_text)
    except phonenumbers.phonenumberutil.NumberParseException as e:
        messagebox.showerror("Error", f"Invalid phone number: {e}")

# Create main window
root = tk.Tk()
root.title("Phone Information")
root.configure(bg="#ddd")  # Set background color

# Create label and entry for phone number input
phone_label = tk.Label(root, text="Enter Your Phone with +:", bg="#f0f0f0")
phone_label.pack()

phone_entry = tk.Entry(root)
phone_entry.pack()

# Create button to retrieve phone info
get_info_button = tk.Button(root, text="Get Info", command=get_phone_info, relief="raised", bg="green")

get_info_button.pack()

# Create label to display result
result_label = tk.Label(root, text="", bg="#f0f0f0", justify="left")
result_label.pack()

# Start the GUI main loop
root.mainloop()
