import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
email = os.getenv("email")
password = os.getenv("password")

connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)
# connection.starttls()
connection.login(user=email, password=password)
connection.sendmail(from_addr=email, to_addrs=email, msg="Hello World!!")
connection.quit()
