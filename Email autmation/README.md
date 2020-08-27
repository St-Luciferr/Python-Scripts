## About the scripts:
# script should be in the same folder as the attachments folder, csv file and the json file to be passed as arguments
- gmail_demo.py takes a single argument for the name of folder containing the attachments
        example: py gmail_demo.py attachments
                    here attachments is the folder containing the attachments to be send
                    
- email_with_csv.py takes two command-line arguments 1st one is the name or abs path of the folder having attachments 
        and 2nd is the csv file having list of user emails for sending email, email should be under headings User Emails in the csv file
        example : py email_with_csv.py attachments user.csv
                     here attachments is the folder containing the attachments to be send and user.csv contains user list to send email

- email_master.py  This files takes three command-line arguments first two are same as above and third one is the json
        file containing the login credentials check out the credentials.json for the sample.
        Example: py email_master.py attachments user.csv credentials.json
        
