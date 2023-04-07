import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "phaneendrasaisds@gmail.com"
password = "qsbeirywwhxctqhm"

receiver = "alluruphaneendrasai@gmail.com"
context = ssl.create_default_context()
message = """ Subject : Hi THis is from Python
How are you Buddy??"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)