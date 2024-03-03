import tkinter as tk
from tkinter import ttk
from tesseract import searchGanimet
from utils import utility as ut



def create_saldiri_tab(tab_control):
    saldiri_tab = ttk.Frame(tab_control)
    tab_control.add(saldiri_tab, text='Saldırı')
  



    def button_click():
        searchGanimet()



    log_text = tk.Text(saldiri_tab, width=59, height=10)
    log_text.grid(row=0, column=0, columnspan=6, padx=10, pady=10)
    ut.log_message(log_text, "Ganimet arama işlemi başlatıldı.")

    label_altin = tk.Label(saldiri_tab, text="Altın Miktarı")
    label_altin.grid(row=1, column=0, padx=10, pady=10)
    altin_var = tk.BooleanVar()
    altin_checkbox = tk.Checkbutton(saldiri_tab, variable=altin_var)
    altin_checkbox.grid(row=1, column=1, sticky="w")
    label_altin_etry = tk.Entry(saldiri_tab)
    label_altin_etry.grid(row=1, column=1)


    label_iksir = tk.Label(saldiri_tab, text="İksir Miktarı")
    label_iksir.grid(row=2, column=0, padx=10, pady=5)  
    iksir_var = tk.BooleanVar()
    iksir_checkbox = tk.Checkbutton(saldiri_tab, variable=iksir_var)
    iksir_checkbox.grid(row=2, column=1, sticky="w")
    label_iksir_entry = tk.Entry(saldiri_tab)
    label_iksir_entry.grid(row=2, column=1, padx=10, pady=10)

    label_gara_iksir = tk.Label(saldiri_tab, text="Gara İksir Miktarı")
    label_gara_iksir.grid(row=3, column=0, padx=10, pady=5) 
    gara_iksir_var = tk.BooleanVar()
    gara_iksir_checkbox = tk.Checkbutton(saldiri_tab, variable=gara_iksir_var)
    gara_iksir_checkbox.grid(row=3, column=1, sticky="w") 
    label_gara_iksir_entry = tk.Entry(saldiri_tab)
    label_gara_iksir_entry.grid(row=3, column=1, padx=10, pady=10)      
    
    ganimet_ara = tk.Button(saldiri_tab, text="Ganimet Ara")
    ganimet_ara.grid(row=2, column=2)
    ganimet_ara.config(command=button_click)

 

    attack_button = tk.Button(saldiri_tab, text="Saldır")
    attack_button.place(x=223, y=520)
    attack_button.config(command=button_click)

  

    return saldiri_tab
