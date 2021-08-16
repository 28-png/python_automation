import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = 'XML data image'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'trackin4rap@gmail.com'
msg.set_content('Image attached...')

files = ['C:/Users/Matthew Murphy/Pictures/xml_data.PNG', 'C:/Users/Matthew Murphy/Pictures/restore.PNG']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)