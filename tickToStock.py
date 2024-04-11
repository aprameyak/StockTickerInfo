from tkinter import *
from tkinter.ttk import *
from selenium import webdriver
#imports tkinter for gui andselenium for web scraping

root = Tk()
root.geometry("600x600")
root.title("Ticker Symbol to Stock Name")
#setup of gui

def stocks(ticker):
    driver = webdriver.Chrome(CHROMEDRIVERPATH)
    driver.get("https://www.nasdaq.com/market-activity/stocks")
    searchBox = driver.find_element_by_name("q")
    searchBox.send_keys(ticker)
    searchBox.submit()
    output.configure(text=driver.find_element_by_class_name("symbol-page-header__name").text)
    driver.quit()
#function to lookup ticker and fetch its full name

sourcetxt = Entry(root, width=40 ,text="Enter ticker symbol")
sourcetxt.pack()
btn = (Button(root, width=40, command=lambda: takeInput(), text="Find full name"))
btn.pack()
output = Button(root, width=40, text=" ")
output.pack()
#more setup of gui

def takeInput():
    input = sourcetxt.get()
    stocks(input)
#function for lambda button

root.mainloop()
