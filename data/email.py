import smtplib
from email.mime.text import MIMEText
from socket import gaierror

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    try :
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
        
    except gaierror :
        print("Gmail server can't be reached, check your internet connexion :(")
    
    else :
        smtp_server.quit()