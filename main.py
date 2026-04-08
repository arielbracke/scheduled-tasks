# region libraries
import smtplib
import datetime as dt
import random
import os
# endregion
# region CONSTANTS and variables
G_ADDRESS = os.environ.get("MY_EMAIL")
G_PASSWORD = os.environ.get("MY_PASSWORD")
O_ADDRESS = os.environ.get("O_EMAIL")
QUOTES = "quotes.txt"
quote = ""
now = dt.datetime.now()
day_of_the_week = now.weekday()
# endregion
# region Functions
def write_text():
    """Chooses quote from file, returns it as quote variable."""
    global quote
    quotes_list = None
    with open(file=QUOTES) as data:
        quotes_list = data.readlines()
        quote = random.choice(quotes_list)
        return quote
def send_message():
    """Connects to SMTP with login given in CONSTANTS, uses the global quote created in the write_text() function."""
    global quote
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = G_ADDRESS, password = G_PASSWORD)
        connection.sendmail(
            from_addr = G_ADDRESS,
            to_addrs = O_ADDRESS,
            msg = f"Subject: First Test\n\n{quote}"
        )
def check_day():
    """If the day is Monday, then it sends it to the receiver (value = 0 | Using datetime generated from today in CONSTANTS and variables)."""
    if day_of_the_week == 0:
        write_text()
        send_message()
# endregion
# region Main
check_day()
# endregion






