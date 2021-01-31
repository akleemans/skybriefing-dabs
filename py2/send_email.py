import smtplib
import os

### CONFIG START ###

SEND_TO = ['myemail1@gmail.com', 'myemail2@gmail.com']
PDFS = 1 # set this to 2 if you used a login for a second PDF
PDF_PATH = 'my path' # Mac OS X: '~/temp/', or on Raspi: '/home/pi/temp/'
SENDER_EMAIL = 'sender-email@gmail.com'
SENDER_PW = 'gmail-password'
EMAIL_SUBJECT = 'skybriefing.com report'
EMAIL_BODY = 'Sent from Raspberry Pi :)'

### CONFIG END ###

# get PDF files
files = [PDF_PATH + f for f in os.listdir(PDF_PATH) if f.endswith('.pdf')]

def send_email_att(user, pwd, recipient, subject, message):
    """ Send an email with attachment. """
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEText import MIMEText
    from email.MIMEBase import MIMEBase
    from email import encoders
    
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # attachment 1
    filename = files[0].split("/")[-1]
    attachment = open(path1, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)

    # attachment 2
    if PDFS == 2:
        filename = files[1].split("/")[-1]
        attachment = open(path2, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(part)

    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.ehlo()
    session.starttls()
    session.login(user, pwd)

    session.sendmail(user, recipient, msg.as_string())
    session.quit()
    print 'Email with attachment succesfully sent.'

# send emails
for email in SEND_TO:
    send_email_att(SENDER_EMAIL, SENDER_PW, email, EMAIL_SUBJECT, EMAIL_BODY)

# delete files after sending
for f in files:
    os.remove(f)
