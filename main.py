import pyautogui

try:
    while True:
        # Fare konumunu al
        fare_x, fare_y = pyautogui.position()
        
        # Fare konumunu yazdır
        print(f"Fare X: {fare_x}, Fare Y: {fare_y}")
        
except KeyboardInterrupt:
    print("\nProgram durduruldu.")
