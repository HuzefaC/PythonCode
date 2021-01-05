
# Demo for sending emails using smtplib
# import smtplib
#
# email = "demo@email.com"
# password = "demo_password"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=email, password=password)
#     connection.sendmail(from_addr=email, to_addrs=email, msg="Hello form python!!")
#

import datetime as dt
# import smtplib
import random

now = dt.datetime.now()
email = "demo@email.com"
password = "demo_password"

if now.weekday() == 1:
    with open(file="quotes.txt", mode="r", encoding="utf8") as file:
        data = file.readlines()
        quote_to_send = random.choice(data)
        print(quote_to_send)
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(user=email, password=password)
    #     connection.sendmail(
    #     from_addr=email,
    #     to_addrs=email,
    #     msg=f"Subject:Monday Motivation\n\n{quote_to_send}")
