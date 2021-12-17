import requests
from smtplib import *
from bs4 import BeautifulSoup

product_url = 'https://www.amazon.in/gp/product/1853264040/ref=ewc_pr_img_3?smid=AT95IG9ONZD7S&psc=1'
my_email = YOUR_EMAIL
receiver = RECEIVER_EMAIL
password = PASSWORD

header = {
    'Accept-Language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/96.0.4664.110 '
                  ' Safari/537.36'
}

response = requests.get(url=product_url, headers=header)
data = response.content
soup = BeautifulSoup(data, 'html.parser')

price = soup.find(name='span', class_="a-size-medium a-color-price inlineBlock-display offer-price a-text-normal "
                                      "price3P").get_text()
without_currency = price.replace("₹", "").replace(",", "")
int_value = int(float(without_currency))

user_price = 250

if int_value <= user_price:
    with SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=receiver, msg=f"Subject:Low Price alert! 💰\n\n" \
                                                                       f"The amazon item is in your budget now!"
                                                                       f" Go get it now!! 💸".encode('utf-8'))
