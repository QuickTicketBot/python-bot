from PIL import ImageGrab
import traceback
from datetime import datetime
import pyautogui
import cv2
import numpy as np
import time
from time import sleep as wait


def print_log(message):
    time_stemp = str(datetime.now())
    time_stemp = time_stemp.split('.')[0]
    msg = f"{time_stemp} - {message}"
    print(msg)
    log_file = open('data_files/logs.txt', 'a')
    log_file.write(f"{msg}\n")


def record_screen():
    time_stemp = str(datetime.now())
    time_stemp = f"{time_stemp.split('.')[0]}:{time_stemp.split('.')[1][0:2]}"
    for s in ['-', ':', ' ']:
        if s in time_stemp:
            time_stemp = time_stemp.replace(s, '-')

    output_file = f"recordings/recording_{time_stemp}.avi"
    print_log(f"Screen is being recording and will save as '{output_file}'")

    duration = 300  # 300 seconds (5 minutes)
    screen_width, screen_height = pyautogui.size()
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_file, fourcc, 10, (screen_width, screen_height))
    start_time = time.time()
    while (time.time() - start_time) < duration:
        screenshot = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        out.write(frame)

    out.release()
    cv2.destroyAllWindows()

    print_log(f"Screen recording has been save as '{output_file}'")


if __name__ == '__main__':
    try:
        for i in range(2):
            record_screen()
    except:
        print_log(traceback.format_exc())
        wait(10)
