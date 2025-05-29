from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

CHROMEDRIVERPATH = os.getenv("CHROMEDRIVERPATH", "chromedriver") 

root = Tk()
root.geometry("600x600")
root.title("Ticker Symbol to Stock Name")

def stocks(ticker):
    try:
        if not ticker.strip():
            messagebox.showwarning("Input Error", "Please enter a ticker symbol.")
            return
        output.configure(text="Searching...")
        driver = webdriver.Chrome(CHROMEDRIVERPATH)
        driver.get("https://www.nasdaq.com/market-activity/stocks")

        searchBox = driver.find_element(By.NAME, "q")
        searchBox.send_keys(ticker)
        searchBox.submit()

        name_element = driver.find_element(By.CLASS_NAME, "symbol-page-header__name")
        output.configure(text=name_element.text)

    except Exception as e:
        output.configure(text="Lookup failed.")
        messagebox.showerror("Error", f"Could not retrieve data for '{ticker}'.\n\nDetails:\n{e}")
    finally:
        try:
            driver.quit()
        except:
            pass

def takeInput():
    ticker = sourcetxt.get()
    stocks(ticker)

sourcetxt = Entry(root, width=40)
sourcetxt.pack(pady=10)

btn = Button(root, width=40, command=takeInput, text="Find full name")
btn.pack(pady=5)

output = Label(root, width=60, text="Enter a ticker symbol above and click the button.")
output.pack(pady=20)

clear_btn = Button(root, width=40, text="Clear", command=lambda: sourcetxt.delete(0, END))
clear_btn.pack(pady=5)

root.mainloop()
