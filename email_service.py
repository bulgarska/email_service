import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USERNAME')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_ADDRESS_RECIPIENT = os.environ.get('EMAIL_ADDRESS_RECIPIENT')

email_template = 'html_email_template.html'

with open(email_template, 'r', encoding='utf-8') as f:
    html_string = f.read()

msg = EmailMessage()
msg['Subject'] = 'Check out this html template email!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS_RECIPIENT

msg.set_content('This is an html template email')

msg.add_alternative(html_string, subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)