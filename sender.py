import sys
import os.path
from Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

CLIENT_SECRET_FILE = "client_secret.json"
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

emailMsg = sys.argv[1]
mimeMessage = MIMEMultipart()

  
if os.path.isfile(sys.argv[2]):
    with open(sys.argv[2]) as file:
        lines = file.readlines()
        receivers = ", ".join(str(address.strip("\n")) for address in lines)
elif type(sys.argv[2]) == str:
    receivers = sys.argv[2]

mimeMessage['to'] = receivers
mimeMessage['subject'] = sys.argv[3]
mimeMessage.attach(MIMEText(emailMsg, 'plain'))
raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
# print(message)
