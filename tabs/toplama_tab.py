import tkinter as tk
from tkinter import ttk
from tesseract import collect_Gaynak

def create_toplama_tab(tab_control):
    toplama_tab = ttk.Frame(tab_control)
    tab_control.add(toplama_tab, text='Toplama')

    def button_click():
        collect_Gaynak()

    collect_button = tk.Button(toplama_tab, text="Ganimet Topla")
    collect_button.place(x=223, y=520)
    collect_button.config(command=button_click)

    return toplama_tab
