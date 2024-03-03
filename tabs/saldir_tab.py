import tkinter as tk
from tkinter import ttk
from utils import utility as ut
from PIL import Image, ImageTk
from utils import search_resources 

resized_currency_gold = None
resized_currency_elixir = None
resized_currency_dark_elixir = None
log_text = None
def create_saldiri_tab(tab_control):
    saldiri_tab = ttk.Frame(tab_control)
    tab_control.add(saldiri_tab, text='Saldırı')
    global resized_currency_gold
    global resized_currency_elixir
    global resized_currency_dark_elixir
    global log_text

    def toggle_entry_state(checkbox, entry):
        if checkbox.get():
            entry.config(state="normal")
        else:
            entry.config(state="disabled")

    
    def button_click():
        search_resources.searchGanimet(label_altin_etry.get())

   
    log_text = tk.Text(saldiri_tab, width=59, height=10)
    log_text.grid(row=0, column=0, columnspan=6, padx=10, pady=10)
    ut.log_message(log_text, "Ganimet arama işlemi başlatıldı.")

    #Altın Alanı
    currency_gold_image= Image.open("images/currency_gold.png")
    resized_currency_gold_image= currency_gold_image.resize((20, 20), Image.BICUBIC)
    resized_currency_gold = ImageTk.PhotoImage(resized_currency_gold_image)
    currency_gold = tk.Label(saldiri_tab, image=resized_currency_gold)
    currency_gold.grid(row=1, column=0,sticky="w",padx=10, pady=10)
    label_altin = tk.Label(saldiri_tab, text="Altın:")
    label_altin.grid(row=1, column=0, padx=10, pady=10)
    altin_var = tk.BooleanVar(value=True)
    altin_checkbox = tk.Checkbutton(saldiri_tab, variable=altin_var,command=lambda: toggle_entry_state(altin_var, label_altin_etry))
    altin_checkbox.grid(row=1, column=1, sticky="w")
    label_altin_etry = tk.Entry(saldiri_tab)
    label_altin_etry.grid(row=1, column=1)
    #Altın Alanı

    #İksir Alanı
    currency_elixir_image= Image.open("images/currency_elixir.jpg")
    resized_currency_elixir_image= currency_elixir_image.resize((20, 20), Image.BICUBIC)
    resized_currency_elixir = ImageTk.PhotoImage(resized_currency_elixir_image)
    currency_elixir = tk.Label(saldiri_tab, image=resized_currency_elixir)
    currency_elixir.grid(row=2, column=0,sticky="w",padx=10, pady=10)
    label_iksir = tk.Label(saldiri_tab, text="İksir:")
    label_iksir.grid(row=2, column=0, padx=10, pady=5)  
    iksir_var = tk.BooleanVar(value=True)
    iksir_checkbox = tk.Checkbutton(saldiri_tab, variable=iksir_var,command=lambda: toggle_entry_state(iksir_var, label_iksir_entry))
    iksir_checkbox.grid(row=2, column=1, sticky="w")
    label_iksir_entry = tk.Entry(saldiri_tab)
    label_iksir_entry.grid(row=2, column=1, padx=10, pady=10)
    #İksir Alanı

    #Gara İksir Alanı
    currency_dark_elixir_image= Image.open("images/currency_dark_elixir.jpg")
    resized_currency_dark_elixir_image= currency_dark_elixir_image.resize((20, 20), Image.BICUBIC)
    resized_currency_dark_elixir = ImageTk.PhotoImage(resized_currency_dark_elixir_image)
    currency_dark_elixir = tk.Label(saldiri_tab, image=resized_currency_dark_elixir)
    currency_dark_elixir.grid(row=3, column=0,sticky="w",padx=10, pady=10)
    label_gara_iksir = tk.Label(saldiri_tab, text="Gara İksir:")
    label_gara_iksir.grid(row=3, column=0, padx=10, pady=5) 
    gara_iksir_var = tk.BooleanVar(value=True)
    gara_iksir_checkbox = tk.Checkbutton(saldiri_tab, variable=gara_iksir_var,command=lambda: toggle_entry_state(gara_iksir_var, label_gara_iksir_entry))
    gara_iksir_checkbox.grid(row=3, column=1, sticky="w") 
    label_gara_iksir_entry = tk.Entry(saldiri_tab)
    label_gara_iksir_entry.grid(row=3, column=1, padx=10, pady=10)      
    #Gara İksir Alanı

    ganimet_ara = tk.Button(saldiri_tab, text="Ganimet Ara")
    ganimet_ara.grid(row=2, column=2)
    ganimet_ara.config(command=button_click)

 

    attack_button = tk.Button(saldiri_tab, text="Saldır")
    attack_button.place(x=223, y=520)
    attack_button.config(command=button_click)


    return saldiri_tab
