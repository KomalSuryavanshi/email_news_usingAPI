import os
import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "komalwork11@gmail.com"
    # password = "wgrftqupxdhojhom"    genereted from Gmail but this is unsafe method

    password = os.getenv("PASSWORD")

    receiver = "komalwork11@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
