import smtplib
import datetime as dt
import pandas
import random

df = pandas.read_csv("quotes.txt", header=None, names=["item"])
list_of_quotes = df["item"].tolist()


now = dt.datetime.now()
day = now.weekday()

password ="dizvxmizqnkqtoso"
my_email = "bryangwin@gmail.com"

if day == 0: 
        
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=my_email, 
                        msg=f"Subject: Quotes for Motivation\n\n{random.choice(list_of_quotes)}")
    connection.close()




