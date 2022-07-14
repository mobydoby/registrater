import pynput
import sys
import pause
from datetime import datetime
from selenium import webdriver
import chromedriver_binary

def getdata(file):
    with open(file) as f:
        lines = f.readlines()
    time = lines[0].strip()
    courses = lines[1].strip()
    return time, courses

def enter_courses(class_string):
    keyboard = pynput.keyboard.Controller()

    #navigate to the first input
    keyboard.press(pynput.keyboard.Key.tab)
    keyboard.release(pynput.keyboard.Key.tab)

    for char in class_string:
        if char == ' ':
            keyboard.press(pynput.keyboard.Key.tab)
            keyboard.release(pynput.keyboard.Key.tab)
            continue
        elif char == '!': 
            keyboard.press(pynput.keyboard.Key.enter)
            keyboard.release(pynput.keyboard.Key.enter)
            continue
        keyboard.press(char)
        keyboard.release(char)
    print("Courses entered")        

if __name__ == '__main__':
    if len(sys.argv)!=2:
        print(f"Wrong number of input files {len(sys.argv)}")
    filename = sys.argv[1];
    

    #read data
    timestr, coursestr = getdata(filename)
    time = [int(x) for x in timestr.split(' ')]
    time = datetime(time[0], time[1], time[2], time[3], time[4])

    #refresh the browser
    driver = webdriver.Chrome()
    # executable_path=r"C:\Users\Andy\Downloads\miniconda\Lib\site-packages\chromedriver_binary.exe"
    driver.get("https://sis.rpi.edu/rss/bwskfreg.P_AltPin")
    # driver.get("https://google.com")

    #pause until registration opens
    pause.until(time)
    print("done pausing")

    driver.refresh();
    #wait 2 seconds don't know a better way to do this lol
    driver.implicitly_wait(2)
    enter_courses(coursestr)


    

    
    

