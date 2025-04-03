# **Stock Ticker Info Scraper**

This project features a graphical user interface (GUI) built with Tkinter that allows users to input a stock ticker symbol. Upon submitting the ticker, the application uses Selenium WebDriver for Chrome to scrape the stock's full name and display it back in the GUI.

![Python Badge](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium Badge](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Tkinter Badge](https://img.shields.io/badge/Tkinter-008080?style=for-the-badge&logo=python&logoColor=white)

## Features

- **Ticker Input**: Users can enter a stock ticker symbol into a text field.
- **Web Scraping**: Selenium WebDriver is used to scrape the full name of the stock associated with the entered ticker symbol.
- **User Interface**: Built with Tkinter, the GUI displays the stock's full name once the submit button is pressed.

## Technology Stack

- **Frontend**: Tkinter (Python GUI)
- **Web Scraping**: Selenium WebDriver (for Chrome)
- **Web Driver**: ChromeDriver

## How it Works

1. **Tkinter GUI**: The user interacts with the GUI to input a stock ticker symbol and press a submit button.
2. **Selenium WebDriver**: Upon submission, the application initiates a web scraping process using Selenium WebDriver for Chrome. The driver opens a browser and queries a stock information website.
3. **Data Extraction**: The full name of the stock is extracted from the webpage.
4. **Displaying Results**: The stock's full name is displayed back in the Tkinter window for the user to see.
