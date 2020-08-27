#!/usr/bin/python

import json,csv,smtplib,sys,os,mimetypes
from email.message import EmailMessage

#comment this block if you don't have separete json file
with open('credentials.json') as js:
    '''
    you need to include the data in a jason file named 'files.json' in a format as below
    {"Email_address": "user@example.com",
    "Email_password": "password"}
    '''
    jsn = json.load(js)
    Email_address = jsn['Email_address']
    Email_password = jsn['Email_password']
# if you don't want to make json file enter username and password and recievers directly removing comment below
#Email_address = ""
#Email_password = ""
receivers=[]
# reading email list from the csv file that contains emails under header 'User Emails'
# you can modify the key below if you csv file contains email under different header
with open(sys.argv[2]) as f:
    fp = csv.DictReader(f)
    for item in fp:
        receivers.append(item['User Emails'])
    

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

#adding attachments
relative_path = os.path.abspath(sys.argv[1])+"/"
for file_name in filenames:
    with open(relative_path + file_name, 'rb') as ppt:
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
