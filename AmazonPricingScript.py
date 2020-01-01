import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.in/Lap-Gadgets-Battery-ProBook-battery/dp/B01E8Y59RM/ref=sr_1_1_sspa?crid=32MDO84Q137GG&keywords=laptop+battery+hp+elitebook+8460p&qid=1573573874&sprefix=laptop+battery+hp+eli%2Caps%2C282&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzSUpCUU5IWUhaM1VUJmVuY3J5cHRlZElkPUEwNTMyODIzMTYzVjZTUDhBS0pKVyZlbmNyeXB0ZWRBZElkPUEwOTc5NDg5Wk5ETks5V0pFSklRJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='


headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'}

def send_mail():
     server = smtplib.SMTP('smtp.gmail.com', 587)
     server.ehlo()
     server.starttls()
     server.ehlo()

     server.login('abdulahadas@gmail.com', '###################' )

     subject = 'Price fell down!!!'
     body = 'check the amazon link https://www.amazon.in/Lap-Gadgets-Battery-ProBook-battery/dp/B01E8Y59RM/ref=sr_1_1_sspa?crid=32MDO84Q137GG&keywords=laptop+battery+hp+elitebook+8460p&qid=1573573874&sprefix=laptop+battery+hp+eli%2Caps%2C282&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzSUpCUU5IWUhaM1VUJmVuY3J5cHRlZElkPUEwNTMyODIzMTYzVjZTUDhBS0pKVyZlbmNyeXB0ZWRBZElkPUEwOTc5NDg5Wk5ETks5V0pFSklRJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
     
     msg = f"{subject}\n\n{body}"

     server.sendmail(
         'abdulahadas@gmail.com',
         'aiwithab.ml@gmail.com',

         msg
     )

     print('Hey email has been sent!')

     server.quit()



def check_price():

    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()

    converted_price =float(price[2:7].replace(',', '.'))

    if (converted_price < 1.500):
        send_mail()

    print(converted_price)
    print(title.strip())

while(True):

    check_price()
