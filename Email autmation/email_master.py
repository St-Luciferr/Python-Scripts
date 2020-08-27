#!/usr/bin/python

import json,csv,smtplib,sys,os,mimetypes
from email.message import EmailMessage

# this block reads your credentials from the file given as third command line argument while execution
with open(sys.argv[3]) as js:
    jsn = json.load(js)
    Email_address = jsn['Email_address']
    Email_password = jsn['Email_password']
#variable to store the list of user to send the email
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

# you can change the subject of your email here
msg['Subject'] = "Hello"
msg['From'] = Email_address
msg['To'] = receiver
# Edit what content you want to give to your email body
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

#initiating SMTP to login to gmail and to send the emails
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    try:
        smtp.login(Email_address, Email_password)
        print("Logged in to Email")
    except:
        print("Login Failed")

    print("Sending Email")
    try:
        smtp.send_message(msg)
        print(f"Email Sent to {len(receivers)} users")
    except:
        print("Failed to send Email")
