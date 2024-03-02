import tkinter as tk
from tkinter import ttk
from tabs.saldir_tab import create_saldiri_tab
from tabs.toplama_tab import create_toplama_tab

def create_view():
    root = tk.Tk()
    root.title("View Example")
    root.geometry("500x600")

    # Yalnızca bir kere tab_control oluştur
    tab_control = ttk.Notebook(root)

    # Saldırı sekmesini oluşturmak için create_saldiri_tab fonksiyonunu çağır
    saldiri_tab = create_saldiri_tab(tab_control)
    tab_control.add(saldiri_tab, text='Saldırı')

    # Toplama sekmesini oluşturmak için create_toplama_tab fonksiyonunu çağır
    toplama_tab = create_toplama_tab(tab_control)
    tab_control.add(toplama_tab, text='Toplama')

    tab_control.pack(expand=1, fill='both')

    root.mainloop()

if __name__ == "__main__":
    create_view()
