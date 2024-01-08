# Eliminar las siguientes líneas:
from time import sleep
import keyboard as keybd
import pyautogui as cursor

from automaticDeviceActions import openProgram, closeWindow


# Start recording:
def startRecording():
    cursor.moveTo(1760, 930);   sleep(3)
    cursor.click()


# Screen size:
print(cursor.size())

# Cursor position:
print(cursor.position())


link = 'https://centrodeelearning.zoom.us/j/96618310558?pwd=QW5uRE4veXZUMHVVRmFYYkd6OWhndz09'

# @todo: uncomment after testing stuff:
openProgram('Brave');       sleep(3)
keybd.press('CTRL + T');    sleep(1)
keybd.release('CTRL');      sleep(1)
keybd.write(link);          sleep(1)
keybd.press('\n');          sleep(1)
cursor.moveTo(1075, 220);   sleep(1)
cursor.click();             sleep(1)

openProgram('OBS');     sleep(3)
startRecording();       sleep(1)
closeWindow()
