import tkinter as tk
from tkinter import ttk
from tesseract import searchGanimet

def create_saldiri_tab(tab_control):
    saldiri_tab = ttk.Frame(tab_control)
    tab_control.add(saldiri_tab, text='Saldırı')

    def button_click():
        searchGanimet()

    label_altin = tk.Label(saldiri_tab, text="Altın Miktarı")
    label_altin.grid(row=0, column=0, padx=10, pady=10)
    label_altin_etry = tk.Entry(saldiri_tab)
    label_altin_etry.grid(row=0, column=1, padx=10, pady=10)

    label_iksir = tk.Label(saldiri_tab, text="İksir Miktarı")
    label_iksir.grid(row=1, column=0, padx=10, pady=5)  
    label_iksir_entry = tk.Entry(saldiri_tab)
    label_iksir_entry.grid(row=1, column=1, padx=10, pady=10)   
    
    ganimet_ara = tk.Button(saldiri_tab, text="Ganimet Ara")
    ganimet_ara.place(x=100, y=100)
    ganimet_ara.config(command=button_click)

    attack_button = tk.Button(saldiri_tab, text="Saldır")
    attack_button.place(x=223, y=520)
    attack_button.config(command=button_click)

    return saldiri_tab
