import cv2
import pytesseract
import numpy as np
import pyautogui
import time
import re
import sys
from inference_sdk import InferenceHTTPClient
from PIL import ImageGrab
import base64
from python_imagesearch.imagesearch import imagesearcharea
from PIL import Image
from io import BytesIO

# Tesseract OCR'ı başlat
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
saldır = "saldır"
# gold değer okuma
sol_ust_x = 81
sol_ust_y = 119
sag_alt_x = 238
sag_alt_y = 166

istenilen_gold = 200000
istenilen_iksir = 200000

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

stratejiCoordinate_x = [680, 144, 794, 1139, 1717, 1196]
stratejiCoordinate_y = [875, 489, 63, 70, 486, 857]
duration = 0.1
interval = 10
eskerler = [(349, 989), (450, 990), (599, 975)]


gaynakGold_x=651
gaynakGold_y=502
gaynakIksir_x=757
gaynakIksir_y=657
gaynakGara_Iksir_x=1218
gaynakGara_Iksir_y=501


pos = imagesearcharea('./images/iksirr.png',0,0,1920,1080) 
if pos[0] != -1 and pos[1] != -1:
    print("Görüntü bulundu! Koordinatlar:", pos)
else:
    print("İmage bulunamadı")


# def collect_Gaynak():
#   try:
#         time.sleep(2)
#         pyautogui.moveTo(gaynakGold_x, gaynakGold_y)
#         pyautogui.click()
#         time.sleep(1)
#         pyautogui.moveTo(gaynakIksir_x, gaynakIksir_y)
#         pyautogui.click()
#         time.sleep(1)
#         pyautogui.moveTo(gaynakGara_Iksir_x, gaynakGara_Iksir_y)
#         pyautogui.click()
#   except BufferError:
#         print(BufferError)





# def enGenisten_Izle():
#     pyautogui.hotkey('ctrl','alt')
#     time.sleep(0.5)
#     pyautogui.scroll(-10)
#     pyautogui.hotkey('ctrl','alt','release')



# def stringi_temizle_ve_integera_cevir(string):
#     temiz_string = ""

#     for char in string:
#         if char.isdigit():
#             temiz_string += char

#     try:
#         integer_deger = int(temiz_string)
#         return integer_deger
#     except ValueError:
#         return 0
    
# def searchGanimet(istenilen_gold):
#     enGenisten_Izle()
#     try:
#         time.sleep(3)
#         if saldır == "saldır":
#             pyautogui.moveTo(saldir_x, saldir_y)
#             time.sleep(3)
#             pyautogui.click()
#             time.sleep(3)
#             pyautogui.moveTo(eslesme_bul_x, eslesme_bul_y)
#             time.sleep(3)
#             pyautogui.click()
#         else:
#             print("Bot başlatılamadı")
#     except BufferError:
#         print(BufferError)
#     while True:
#         try:
#             time.sleep(4)
#             ekran_goruntusuGold = pyautogui.screenshot(region=(sol_ust_x, sol_ust_y, sag_alt_x - sol_ust_x, sag_alt_y - sol_ust_y))
#             time.sleep(1)
#             ekran_goruntusuIksir = pyautogui.screenshot(region=(sol_ust_x2, sol_ust_y2, sag_alt_x2 - sol_ust_x2, sag_alt_y2 - sol_ust_y2))

#             ekran_npGold = np.array(ekran_goruntusuGold)
#             ekran_npIksir = np.array(ekran_goruntusuIksir)
#             ekran_npGold = cv2.cvtColor(ekran_npGold, cv2.COLOR_RGB2BGR)
#             ekran_npIksir = cv2.cvtColor(ekran_npIksir, cv2.COLOR_RGB2BGR)

#             metinGold = pytesseract.image_to_string(ekran_npGold)
#             strippedGold = metinGold.strip()
#             replacedGold = strippedGold.replace(" ","")
           
#             metinIksir = pytesseract.image_to_string(ekran_npIksir)
#             print("Gold Miktarı:", replacedGold)
#             print("İksir miktarı:", metinIksir)
            
#             try:
#                 extractedGold = stringi_temizle_ve_integera_cevir(replacedGold)
                
#                 if istenilen_gold <  extractedGold:
#                     print("buldum")
#                     return True
#                 else:
#                     print("Aramaya devamke")
#                     pyautogui.moveTo(ileri_coodinate_x, ileri_coodinate_y)
#                     time.sleep(3)
#                     pyautogui.click()
#             except (ValueError, TypeError):
#                 pyautogui.moveTo(ileri_coodinate_x, ileri_coodinate_y)
#                 time.sleep(3)
#                 pyautogui.click()
                
#         except KeyboardInterrupt:
#             print("\nProgram durduruldu.")

# def select_Esker(asker_koordinatlari):
#     for x, y in asker_koordinatlari:
#         pyautogui.click(x, y)
#         time.sleep(1)
#         IcindenGec(stratejiCoordinate_x,stratejiCoordinate_y,duration)

# def IcindenGec(x, y, duration):
#     try:
#         for x, y in zip(x, y):
#             pyautogui.moveTo(x, y)
#             time.sleep(duration)  # Belirtilen süre boyunca bekler
#             pyautogui.click()  # Click eventını gerçekleştirir
#             time.sleep(duration)  # Belirli bir aralıkla tekrarlamak için bekler
#     except KeyboardInterrupt:
#         print("\nProgram durduruldu.")

# collect_Gaynak()
# time.sleep(5)
# IsKoyDetectEdildi=searchGanimet(istenilen_gold)

# if IsKoyDetectEdildi:
#     select_Esker(eskerler)
#     print("İçinden Geçme İşlemi Tamamlandı")
#     sys.exit()
# else: 
#     print("Saldırı İptal edildi")



    



