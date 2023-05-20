import datetime as dt
import pandas as pd
import random
import smtplib

PASSWORD = "dizvxmizqnkqtoso"
MY_EMAIL = "bryangwin@gmail.com"

today = dt.datetime.now()
current_day = today.day
current_month = today.month

df = pd.read_csv("birthdays.csv")
bday_dict = df.to_dict(orient='index')

index_to_send = None

for key, value in bday_dict.items():
    if current_day == value["day"] and current_month == value["month"]:
        index_to_send = key

if index_to_send != None:
    path_to_letter = f"letter_{random.randint(1, 3)}.txt"
    with open(f"letter_templates/{path_to_letter}", "r") as letter:
        text_of_letter = letter.read()
        text_to_send = text_of_letter.replace(
            "[NAME]", bday_dict[index_to_send]["name"])
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=bday_dict[index_to_send]["email"],
        msg=f"Subject:Happy Birthday!!!\n\n{text_to_send}"
    )
    connection.close()
