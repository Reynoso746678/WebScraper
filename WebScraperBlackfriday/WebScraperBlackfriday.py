import requests 
from bs4 import BeautifulSoup
import smtplib
import time

#URL of Amazon item
URL = 'https://www.amazon.com/dp/B00W2D806Y/?coliid=I25HCE64XGIDZ9&colid=3R7CIZSP5HK6T&psc=1&ref_=lv_ov_lig_dp_it'

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'}

#Check if price has fallen
def check_price():
    
    #Combine request(s)
    page = requests.get(URL, headers=headers)
    
    #Amazon page request(s)
    soup = BeautifulSoup(page.content, 'lxml')
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:])
    
    if(converted_price < 39):
        send_mail()

#Send Email 
def send_mail():

    #Email touch
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    #Depending on your 2 step verification process through a google account
    server.login('gmail', 'pass')
    
    #Components of Message
    subject = 'Yo! Its finally fallen'
    body = 'Check the amazon link https://www.amazon.com/dp/B00W2D806Y/?coliid=I25HCE64XGIDZ9&colid=3R7CIZSP5HK6T&psc=1&ref_=lv_ov_lig_dp_it'
    msg = f"Subject: {subject}\n\n{body}"
    
    #From (email address) & to (Email Address)
    server.sendmail(
        'from',
        'to',
        msg
    )
    server.quit()

#Time to recheck price
while(True):
    check_price()

    # 24 hour 
    time.sleep(82400)
