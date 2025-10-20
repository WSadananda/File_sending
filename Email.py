import smtplib
from email.message import EmailMessage as mail
import datetime as dt

time=dt.datetime.now().hour
if time < 12:
    wish="Good Morning"
elif 12<time<14:
    wish="Good Afternoon"
elif 14<time<24:
    wish="Good Evening"
else:
    wish="Hello"
#initialize
file=""
PO=""
fname=""
#Require
meg=mail()
sender="sadanandaw13@gmail.com"
password="gixg vkij snsl alte"
receiver="sadanandaw13@gmail.com"

#Header
meg["From"]="sadanandaw13@gmail.com"
meg["To"]="sadanandaw13@gmail.com"
meg["Subject"]="Sending a test PO"

meg.set_content(f"""
{wish},
  I hope this message finds you well.

Please find attached the Purchase Order {PO} for your kind reference.

Should you have any questions or require further information, please do not hesitate to contact me.

Thank you for your attention.

Best regards,
Sadananda
 """)
#add attachment
meg.add_attachment(file,
                   maintype="application",
                   subtype="json",
                   filename=fname)

#Connection
with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
    smtp.login(sender,password)
    smtp.send_message(meg)
print("send")