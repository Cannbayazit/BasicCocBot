import time
import tkinter
import pyautogui


def log_message(log_text, message):
    log_text.insert(tkinter.END, message + "\n")
    log_text.see(tkinter.END)  # Otomatik olarak kaydır


def enGenisten_Izle():
    pyautogui.hotkey('ctrl','alt')
    time.sleep(0.5)
    pyautogui.scroll(-10)
    pyautogui.hotkey('ctrl','alt','release')




def stringi_temizle_ve_integera_cevir(string):
    temiz_string = ""

    for char in string:
        if char.isdigit():
            temiz_string += char

    try:
        integer_deger = int(temiz_string)
        return integer_deger
    except ValueError:
        return 0
    
