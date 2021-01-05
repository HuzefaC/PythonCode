import pandas
import datetime as dt
import random
import smtplib

email = "demoemail@email.com"
password = "password"
now = dt.datetime.today()
month = now.month
day = now.day
letter_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

data = pandas.read_csv("birthdays.csv")
birthdays = data.to_dict(orient="records")

# 1. Check if today matches a birthday in the birthdays.csv
for birthday in birthdays:
    if birthday['month'] == month and birthday['day'] == day:
        # 3. If step 2 is true, pick a random letter from letter templates and
        # replace the [NAME] with the person's actual name from birthdays.csv
        letter = random.choice(letter_list)
        name = birthday["name"]
        to_email = birthday["email"]
        with open(file=f"letter_templates/{letter}", mode="r", encoding="utf8") as file:
            letter_content = file.read()
            letter_content = letter_content.replace("[NAME]", name)
        with smtplib.SMTP("smtp.google.com") as connection:
            # 4. Send the letter generated in step 3 to that person's email address.
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs=to_email,
                msg=f"Subject:Happy Birthday\n\n{letter_content}")
