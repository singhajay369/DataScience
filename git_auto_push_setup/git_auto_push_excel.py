import os
import datetime

FOLDER_PATH = r"D:\Data Science\Excel"  # <-- Path to your Excel folder

os.chdir(FOLDER_PATH)
os.system("git add .")
os.system('git commit -m "Auto-update on ' + str(datetime.datetime.now()) + '"')
os.system("git push origin main")
