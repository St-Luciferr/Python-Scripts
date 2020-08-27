#!/usr/bin/python

import os
import sys
import smtplib
import json
import mimetypes
from email.message import EmailMessage

with open('credentials.json') as js:
    '''
    look at the credentials.json file for the sample of json file
    '''
    jsn = json.load(js)
    Email_address = jsn['Email_address']
    Email_password = jsn['Email_password']

# if you don't want to make json file comment the block above
# And enter username and password directly removing comment below
#Email_address = ""
#Email_password = ""

# adding all recievers in single string separated with comma
receiver = str(sys.argv[2])
print(receiver)

paths = sys.argv[1]
filenames = os.listdir(paths)

# giving contents to the email
msg = EmailMessage()
#Change the subject to your choice if you wish
msg['Subject'] = "Hello"
msg['From'] = Email_address
msg['To'] = receiver
body = "Few attachment"
msg.set_content(body)

#adding attachments
relative_path = sys.argv[1]+"/"
for file_name in filenames:
    with open(relative_path + file_name, 'rb') as ppt:
        file_data = ppt.read()

    #mimetypes.guess_type gives filetype and encoding as touple
    file_type,encode = mimetypes.guess_type(file_name)
    main_type,sub_type = file_type.split('/',1)
    msg.add_attachment(file_data,maintype=main_type,subtype=sub_type,filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    try:
        smtp.login(Email_address, Email_password)
        print("Logged in to Email")
    except:
        print("Login Failed")

    print("Sending Email")
    try:
        smtp.send_message(msg)
        print(f"Email Sent to {receiver}")
    except:
        print("Failed to send Email")
