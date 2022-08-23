import os 
import pandas as pd
import smtplib
import imghdr
from email.message import EmailMessage

user_mail = os.environ.get("testmail")
user_pass = os.environ.get("apppassword")


df=pd.read_excel("D:\Emails.xlsx")
tomail=df["EMAIL_ID"].values

subject = input("Enter the subject :")
body = input("Enter the message :")

msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = user_mail
msg['To'] = tomail
msg.set_content(body)

zipped=zip(tomail)

for(a) in zipped:
    
    msg=EmailMessage()
    
    files = []
    n = int(input("Number of documents you want to send :"))
    for i in range(n):
        doc = input("Enter the file names :")
        files.append(doc)

    for file in files:
        with open(file, "rb") as f:
            file_data = f.read()
            file_type = imghdr.what(f.name)
            file_name = f.name

        msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
        
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(user_mail, user_pass)
    smtp.send_message(msg)