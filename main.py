# Tkinter modules
from cgitb import text
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

# Selenium web drivers to target web site

driver = webdriver.Chrome(PATH, options=options)
driver.get("https://www.011info.com/kursna-lista")
driver.maximize_window()
# driver.implicitly_wait(10)
action = ActionChains(driver)

# scrapping curency values from web

xpath_list = ["/html/body/div[3]/div/div[1]/div/table/tbody/tr[1]/td[6]",
              "/html/body/div[3]/div/div[1]/div/table/tbody/tr[2]/td[6]",
              "/html/body/div[3]/div/div[1]/div/table/tbody/tr[3]/td[6]",
              "/html/body/div[3]/div/div[1]/div/table/tbody/tr[7]/td[6]"]

value_list = []
for i in range(len(xpath_list)):
    finded = driver.find_element(By.XPATH, xpath_list[i]).text
    replaced_dot = finded.replace(',', '.')
    str_to_float = float(replaced_dot)
    value_list.append(f'{str_to_float:.2f}')

# print(value_list)
# defining main frame top level window
top_win = Tk()
top_win.geometry("600x600")
top_win.title("Currency changer ")


# show current date used for daily curency urency course
present_time = datetime.datetime.now().strftime("%x")

# creating labels for curency changer App
variable = StringVar(top_win)
variable.set("Chose curency")
chosen = variable.get()
lab2_get_var = StringVar()


def chosen_currency(chosen):

    lab_1 = Label(top_win, text=f"{present_time}\n Today's {chosen} average course : ",
                  bg="lightblue", height=2, width=30).place(x=5, y=5)

    if chosen == "EUR":
        lab_2 = Label(top_win, textvariable=lab2_get_var,
                      height=2, width=20)
        lab_2.place(x=260, y=5)
        lab2_get_var.set(value_list[0])

    elif chosen == "AUD":
        lab_2 = Label(top_win, textvariable=lab2_get_var,
                      height=2, width=20)
        lab_2.place(x=260, y=5)
        lab2_get_var.set(value_list[1])

    elif chosen == "CAD":
        lab_2 = Label(top_win, textvariable=lab2_get_var,
                      height=2, width=20)
        lab_2.place(x=260, y=5)
        lab2_get_var.set(value_list[2])

    elif chosen == "DKK":
        lab_2 = Label(top_win, textvariable=lab2_get_var,
                      height=2, width=20)
        lab_2.place(x=260, y=5)
        lab2_get_var.set(value_list[3])


# Defining option meny for chosing curency
opt_menu = OptionMenu(top_win, variable, "EUR", "AUD",
                      "CAD", "DKK", command=chosen_currency)
opt_menu.place(x=300, y=70)


lab_3 = Label(top_win, text="Currency: ", width=30,
              height=2, bg="red").place(x=5, y=70)


lab_4 = Label(top_win, text="Amount to change: ",
              bg="yellow", width=30, height=2).place(x=5, y=135)

lab_5 = Label(top_win, text="Amount Rsd to assigned currency: ",
              bg="lightgreen", height=2, width=40).place(x=5, y=195)


# definning entry fields and get method for Button "Calculate"

amount_entry = Entry(top_win)
amount_entry.place(x=260, y=150)


def calculate_amount():
    values = lab2_get_var.get()
    total_rs_amount = float(values)*float(amount_entry.get())

    final_label = Label(
        top_win, text=f"{total_rs_amount:.2f} RSD", height=2, width=20)
    final_label.place(x=370, y=200)


# definning button for calculating amount in setted currency
but_1 = Button(top_win, text="Calculate", command=calculate_amount,
               height=2, width=20, relief=GROOVE,bg="yellow").place(x=200, y=300)


top_win.mainloop()
