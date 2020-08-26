#!/usr/bin/python

import os
import sys
import smtplib
import json
import mimetypes
from email.message import EmailMessage

#comment this block if you don't have separete json file
with open('files.json') as js:
    '''
    you need to include the data in a jason file named 'files.json' in a format as below
    {"Email_address": "user@example.com",
    "Email_password": "password",
    "receivers":["user1@example.com","user2@examplecom","user3@example.com"]}
    '''
    jsn = json.load(js)
    Email_address = jsn['Email_address']
    Email_password = jsn['Email_password']
    receivers = jsn['receivers']
# if you don't want to make json file enter username and password and recievers directly removing comment below
#Email_address = ""
#Email_password = ""
receivers = ['suntoss.pandey@gmail.com']

# adding all recievers in single string separated with comma
receiver = ", ".join(receivers)
paths = sys.argv[1]
filenames = os.listdir(paths)

# giving contents to the email
msg = EmailMessage()
msg['Subject'] = "Hello"
msg['From'] = Email_address
msg['To'] = receiver
body = "Few attachment"
msg.set_content(body)
# put the name of files with extension that you want to send
# the files should be in same folder as the script
#filenames = ['photo1.JPG','chapter 1.pptx']
#adding attachments
for file_name in filenames:
    with open(file_name, 'rb') as ppt:
        file_data = ppt.read()

    #mimetypes.guess_type gives filetype and encoding as touple
    file_type,encode = mimetypes.guess_type(file_name)
    main_type,sub_type = file_type.split('/',1)
    msg.add_attachment(file_data,maintype=main_type,subtype=sub_type,filename=file_name)

# with smtplib.SMTP('smtp.gmail.com',587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.ehlo()
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    try:
        smtp.login(Email_address, Email_password)
        print("Logged in to Email")
    except:
        print("Login Failed")

    print("Sending Email")
    try:
        #This is for sending mail without EmailMessage class
        # smtp.sendmail(Email_address, receiver , msg)

        smtp.send_message(msg)
        print(f"Email Sent to {len(receivers)} users")
    except:
        print("Failed to send Email")
