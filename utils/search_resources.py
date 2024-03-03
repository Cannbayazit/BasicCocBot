import time
import tkinter
import cv2
import numpy as np
import pyautogui
from utils import utility as ut
import pytesseract
from tabs import saldir_tab as st
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
sol_ust_x = 81
sol_ust_y = 119
sag_alt_x = 238
sag_alt_y = 166

#iksir değer okuma
sol_ust_x2 = 76
sol_ust_y2 = 165
sag_alt_x2 = 210
sag_alt_y2 = 207

ileri_coodinate_x = 1783
ileri_coodinate_y = 821
saldir_x = 40
saldir_y = 919
eslesme_bul_x=1352
eslesme_bul_y=609

def searchGanimet(istenilen_gold):
    try:
            time.sleep(3)
            pyautogui.moveTo(saldir_x, saldir_y)
            time.sleep(3)
            pyautogui.click()
            time.sleep(3)
            pyautogui.moveTo(eslesme_bul_x, eslesme_bul_y)
            time.sleep(3)
            pyautogui.click()
    except BufferError:
        print(BufferError)
    while True:
        try:
            time.sleep(4)
            ekran_goruntusuGold = pyautogui.screenshot(region=(sol_ust_x, sol_ust_y, sag_alt_x - sol_ust_x, sag_alt_y - sol_ust_y))
            time.sleep(1)
            ekran_goruntusuIksir = pyautogui.screenshot(region=(sol_ust_x2, sol_ust_y2, sag_alt_x2 - sol_ust_x2, sag_alt_y2 - sol_ust_y2))

            ekran_npGold = np.array(ekran_goruntusuGold)
            ekran_npIksir = np.array(ekran_goruntusuIksir)
            ekran_npGold = cv2.cvtColor(ekran_npGold, cv2.COLOR_RGB2BGR)
            ekran_npIksir = cv2.cvtColor(ekran_npIksir, cv2.COLOR_RGB2BGR)

            metinGold = pytesseract.image_to_string(ekran_npGold)
            strippedGold = metinGold.strip()
            replacedGold = strippedGold.replace(",","")
            replacedGold = replacedGold.replace(";","")
            replacedGold = replacedGold.replace(":","")
            replacedGold = replacedGold.replace("/","")
            replacedGold = replacedGold.replace("-","")
            replacedGold = replacedGold.replace("?","")
            replacedGold = replacedGold.replace(".","")
           
            metinIksir = pytesseract.image_to_string(ekran_npIksir)
            print("Gold Miktarı:", replacedGold)
            print("İksir miktarı:", metinIksir)
            
            try:
                extractedGold = ut.stringi_temizle_ve_integera_cevir(replacedGold)
                
                if istenilen_gold <  extractedGold:
                    print("buldum")
                    return True
                else:
                    print("Aramaya devamke")
                    pyautogui.moveTo(ileri_coodinate_x, ileri_coodinate_y)
                    time.sleep(3)
                    pyautogui.click()
            except (ValueError, TypeError):
                pyautogui.moveTo(ileri_coodinate_x, ileri_coodinate_y)
                time.sleep(3)
                pyautogui.click()
                
        except KeyboardInterrupt:
            print("\nProgram durduruldu.")