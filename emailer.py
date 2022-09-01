import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.utils import formataddr
from email import encoders

def sendEmail(fromaddr:str, name:str, password:str, to:str, subject:str, content:str, type="plain", attachment:str=None):
    msg = MIMEMultipart()
    msg['From'] = formataddr((name, fromaddr))
    msg['To'] = to
    msg['Subject'] = subject

    part = MIMEText(content, type)
    msg.attach(part)
    
    # Attach email attachment
    if attachment:
        with open(attachment, "rb") as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment", filename=attachment.split("/")[-1])
            msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, password)
    text = msg.as_string()
    server.sendmail(fromaddr, to, text)
    server.quit()