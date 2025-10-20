from pathlib import Path
import xml.etree.ElementTree as et
import xmls as Exml
import json
import shutil
import time
import smtplib
from email.message import EmailMessage as mail
import datetime as dt

j=0
#while True:
new=[]
d=Path(r"C:\Users\WAIKHOM SADANANDA\Desktop\ClientA")
New=Path(r"C:\Users\WAIKHOM SADANANDA\Desktop\Trading patner")

for file in d.rglob("*.xml"):
  j=Exml.findx(file)

for i in j:
  if i["ProductID"]==[]:
     i["ProductID"]=["Not Available"]

print(j)
Sfile=json.dumps(j,indent=4).encode("utf-8")
Name=j[0]["PO"]+j[0]["OrderID"]

f=Path(r"C:/Users/WAIKHOM SADANANDA/Desktop/ClientA")
filename=f/f"{Name}.json"


#transfer file
with open(filename,'w') as N:
  json.dump(j,N,indent=4)
shutil.move(str(filename),str(New))

#delete file .xml
#for file in d.rglob("*.xml"):
# file.unlink()
#time.sleep(30)
#send email


time=dt.datetime.now().hour
if time < 12:
    wish="Good Morning"
elif 12<time<14:
    wish="Good Afternoon"
elif 14<time<24:
    wish="Good Evening"
else:
    wish="Hello"

#Require
meg=mail()
sender="sadanandaw13@gmail.com"
password="gixg vkij snsl alte"
receiver="sadanandaw13@gmail.com"

#Header
meg["From"]="sadanandaw13@gmail.com"
meg["To"]="romenslife@gmail.com"
meg["Subject"]="Sending a test PO"

meg.set_content(f"""
{wish},
  I hope this message finds you well.

Please find attached the Purchase Order {j[0]["PO"]} for your kind reference.

Should you have any questions or require further information, please do not hesitate to contact me.

Thank you for your attention.

Best regards,
Sadananda
 """)
#add attachment
meg.add_attachment(Sfile,
                   maintype="application",
                   subtype="json",
                   filename=Name)

#Connection
with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
    smtp.login(sender,password)
    smtp.send_message(meg)
print("send")