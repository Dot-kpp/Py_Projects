from multiprocessing import context
import smtplib
import ssl
from email.message import EmailMessage

#Fill in information
subject = " Simple Email Tool "
body = " BODY HERE "
sender_email = " EMAIL HERE "
receiver_email = " EMAIL HERE "
password = input("Enter a password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""

message.add_alternative(html, subtype="html")

context = ssl.create_default_context()

print("Sending Email!")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Success")