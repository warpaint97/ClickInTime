import pyautogui
import sched
import time
from datetime import datetime
import os

def number_dialog(msg, maxNumber):
    os.system("cls")
    number = 0
    while (True):
        try:
            number = int(input(msg))
            assert number >= 0 and number <= maxNumber
            return number
        except:
            os.system("cls")
            print("Invalid input: Please enter a natural number within the specified bounds!")

def full_dialog():
    while (True):
        year = datetime.now().year
        month = datetime.now().month
        day = datetime.now().day

        #year = dialog("Enter a year (yyyy): ")
        #month = dialog("Enter a month (mm): ")
        #day = dialog("Enter a day (dd): ")
        hour = number_dialog("Enter an hour (0-23): ", 23)
        minute = number_dialog("Enter a minute (0-59): ", 59)
        second = number_dialog("Enter a second (0-59): ", 59)
        millisecond = number_dialog("Enter a millisecond (0-999): ", 999)
        microsecond = millisecond * 1000

        # Set the target time
        target_time = datetime(year, month, day, hour, minute, second, microsecond)  # Set your desired date and time

        os.system("cls")
        if (target_time - datetime.now()).total_seconds() < 0:
            print("Invalid input: Please enter a time in the future!")
            input("Press ENTER to restart!")
        else:
            return target_time

# Function to be executed
def trigger_event():
# Click at the current mouse position

    # pyautogui.click()

    # the mouse down duration takes approx. 100ms like this. A normal duration of a human would take 40-60ms 
    pyautogui.mouseDown()
    #time.sleep(0.02)
    pyautogui.mouseUp()

    current_time = datetime.now()
    print("Mouse click event triggered at ", current_time)
    print("with an error of ", (current_time - target_time).total_seconds(), " seconds.")
    input("Press ENTER to exit!")


if __name__ == "__main__":
    # Start dialog
    target_time = full_dialog()

    # Create a scheduler object
    scheduler = sched.scheduler(time.time, time.sleep)

    # Calculate the delay until the target time
    delay = (target_time - datetime.now()).total_seconds()

    # Schedule the event at the target time
    scheduler.enter(delay, 1, trigger_event, ())

    print("Mouse click scheduled at: ", target_time)
    scheduler.run()
