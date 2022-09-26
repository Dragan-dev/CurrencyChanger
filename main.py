# Tkinter modules
from time import strftime
from tkinter import *
import datetime
import tkinter.messagebox as mb

# web scrap modules
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By



# Run headless Chrome window-scrapping in background

options = webdriver.ChromeOptions()
options.add_argument('headless')
PATH = "/home/laki/Documents/chromedriver"

driver = webdriver.Chrome(PATH, options=options)
driver.get("https://www.011info.com/kursna-lista")
driver.maximize_window()
driver.implicitly_wait(10)

action = ActionChains(driver)
average_euro_course = driver.find_element(
    By.XPATH, '/html/body/div[3]/div/div[1]/div/table/tbody/tr[1]/td[6]').text

print(type(average_euro_course))



# defining main frame top level window
top_win = Tk()
top_win.geometry("600x600")
top_win.title("Currency changer ")
# show current date used for daily Euro course in Serbia
present_time = datetime.datetime.now().strftime("%x")

# creating labels for curency changer App
lab_1 = Label(top_win, text=f"{present_time} \n Today's euro course : ",
              bg="lightblue", height=2, width=30).place(x=5, y=5)

lab_2 =Label(top_win,text=f"{average_euro_course}", height= 2 , width=20).place(x = 260, y=5) 

lab_3 = Label(top_win, text="Currency: ", width=30,
              height=2, bg="red").place(x=5, y=70)

lab_3 = Label(top_win, text="Amount to change: ",
              bg="yellow", width=30, height=2).place(x=5, y=135)

lab_4 = Label(top_win, text="Equal money Euro to assigned currency: ",
              bg="lightgreen", height=2, width=40).place(x=5, y=195)


# definning entry fields and get method for Button "Calculate"


# XXX


def calculate_amount():
    entered_value = amount_entry.get()
    int(entered_value)

    if type(entered_value) == int:
        mb.showerror("Invalid input", "Please input Number")
    else:
        print(entered_value)


amount_entry = Entry(top_win)
amount_entry.place(x=260, y=152)

# definning button for calculating amount in setted currency
but_1 = Button(top_win, text="Calculate", command=calculate_amount,
               height=2, width=20).place(x=200, y=300)


top_win.mainloop()
