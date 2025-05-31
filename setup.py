# BISMILLAH E ARRAHMAN ARRAHEEM
import subprocess
import sys
from time import sleep as wait

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'selenium==4.17.2'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'jafri-chromedriver-installer'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'schedule'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'Pillow'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyautogui'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'opencv-python'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'numpy'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'psutil'])


print()
print(f"Setup completed.")
wait(5)