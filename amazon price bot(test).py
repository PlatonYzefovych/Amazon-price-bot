import requests
from bs4 import *
import lxml
import smtplib

'''Enter your data: you need 2 mails, and password to access the mail you`ll get the message'''

FROM_MAIL = "text@gmail"
TO_MAIL = "example@gmail"
PASSWORD = "example mail password"

# Example product
URL = "https://www.amazon.com/Seagate-Portable-External-Hard-Drive/dp/B07CRG94G3/ref=lp_16225007011_1_2"

WANTED_PRICE = 60

'''Get your browser data from site below, and put in HEAD dict 
        http://myhttpheader.com/'''

head = {
    "User-Agent": "your User-Agent:",
    "Accept-Language": "your Accept-Language",
}

response = requests.get(url=URL, headers=head)
soup = BeautifulSoup(response.content, "lxml")

prices = soup.find("span", class_="a-price").getText()

price_without_currency = prices.split("$")[1]
price_as_float = float(price_without_currency)

if price_as_float <= WANTED_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=FROM_MAIL, password=PASSWORD)
        connection.sendmail(from_addr=FROM_MAIL,
                            to_addrs=TO_MAIL,
                            msg=f"Subject: HOT DEAL!!!\nIt`s seems like some of the products that you want "
                                f" now sells only for ${price_as_float} \n{URL}")
