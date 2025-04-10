import os
import time

file_path = "C:\\Users\\дл.DESKTOP-N32060M\\OneDrive\\Рабочий стол\\top academiya\\urok\\pyton\\test3.txt"

if os.path.exists(file_path):
    directory, name = os.path.split(file_path)
    atime = os.path.getatime(file_path)
    t = time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(atime))
    print(f"{name} ({directory}) - время последнего доступа к файлу {t}")
else:
    print(f"Файл {file_path} не существует")