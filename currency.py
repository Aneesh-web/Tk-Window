import tkinter as tk
from tkinter import messagebox

# Function to perform the currency conversion
def convert_currency():
    try:
        # Get the amount entered by the user
        usd_amount = float(entry_usd.get())
        
        # Conversion rates (as of today, you can update these with real-time rates)
        conversion_rates = {
            'EUR': 0.94,   # USD to Euro
            'GBP': 0.82,   # USD to British Pound
            'INR': 83.21,  # USD to Indian Rupee
            'JPY': 149.67  # USD to Japanese Yen
        }
        
        # Perform the conversion
        eur_amount = usd_amount * conversion_rates['EUR']
        gbp_amount = usd_amount * conversion_rates['GBP']
        inr_amount = usd_amount * conversion_rates['INR']
        jpy_amount = usd_amount * conversion_rates['JPY']
        
        # Update the labels with the converted amounts
        label_result_eur.config(text=f"EUR: {eur_amount:.2f}")
        label_result_gbp.config(text=f"GBP: {gbp_amount:.2f}")
        label_result_inr.config(text=f"INR: {inr_amount:.2f}")
        label_result_jpy.config(text=f"JPY: {jpy_amount:.2f}")
    
    except ValueError:
        messagebox.showerror("Input error", "Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("300x250")

# USD input
label_usd = tk.Label(root, text="Enter amount in USD:")
label_usd.pack(pady=10)
entry_usd = tk.Entry(root)
entry_usd.pack(pady=5)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.pack(pady=10)

# Conversion result labels
label_result_eur = tk.Label(root, text="EUR: ")
label_result_eur.pack()
label_result_gbp = tk.Label(root, text="GBP: ")
label_result_gbp.pack()
label_result_inr = tk.Label(root, text="INR: ")
label_result_inr.pack()
label_result_jpy = tk.Label(root, text="JPY: ")
label_result_jpy.pack()

# Run the application
root.mainloop()
