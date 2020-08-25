from bs4 import BeautifulSoup
import requests
import smtplib

URL = ""
MY_PRICE = 80

actual_price = check_price()
if actual_price <= MY_PRICE:
    send_email(actual_price)
