from time import sleep
import keyboard as keybd
import pyautogui as cursor


def openProgram(programName):
    cursor.moveTo(25, 1080);    sleep(1)
    cursor.click();             sleep(1)
    keybd.write(programName);   sleep(1)
    keybd.press('\n')


def closeWindow():
    cursor.moveTo(1810, 10);    sleep(1)
    cursor.click()