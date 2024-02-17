from pynput import mouse
import time
from datetime import datetime

def on_click(x, y, button, pressed):
    global start_time
    global end_time

    if pressed:
        start_time = time.time()
    else:
        end_time = time.time()
        click_duration = end_time - start_time
        print(f"Click occured at ", datetime.now())
        print(f"with a duration of {click_duration:.4f} seconds")

start_time = 0
end_time = 0

with mouse.Listener(on_click=on_click) as listener:
    listener.join()
