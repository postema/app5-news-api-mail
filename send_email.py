import smtplib
import ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "pj.postema@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "pj.postema@gmail.com"
    context = ssl.create_default_context()

    fmt = 'From: {}\r\nTo: {}\r\n{}'
    # fmt = 'From: {}\r\nTo: {}\r\nSubject: {}\r\n{}'


    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
        # server.sendmail(username, receiver, fmt.format(username, receiver, message).encode('utf-8'))
