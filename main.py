import datetime as dt
import pandas as pd
import random
import smtplib
import os

G_ADDRESS = os.environ.get("MY_EMAIL")
G_PASSWORD = os.environ.get("MY_PASSWORD")
today = (dt.datetime.now().month,dt.datetime.now().day)
df = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month,data_row.day): data_row for (index,data_row) in df.iterrows()}
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as text:
        contents = text.read()
        contents = contents.replace("[NAME]",birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=G_ADDRESS,password=G_PASSWORD)
        connection.sendmail(
             from_addr=G_ADDRESS,
             to_addrs=birthday_person["email"],
             msg=f"Subject: HB!!!\n\n{contents}"
         )
print(birthdays_dict)



