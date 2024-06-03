import smtplib
from email.message import EmailMessage
from email.utils import make_msgid
from email.mime.image import MIMEImage


def send_email_with_attachment(smtp_server, port, sender_email, receiver_email, subject, body, image_path, login, app_password):
    # Create the email message
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content(body)

    # Read the image file
    with open(image_path, 'rb') as img:
        img_data = img.read()
        # Create a unique Content-ID for the image
        img_cid = make_msgid(domain='xyz.com')
        msg.add_attachment(img_data, maintype='image',
                           subtype='jpeg', filename=image_path, cid=img_cid)

    # Connect to the SMTP server and send the email
    with smtplib.SMTP_SSL(smtp_server, port) as server:
        server.login(login, app_password)
        server.send_message(msg)


smtp_server = 'smtp.gmail.com'
port = 465
sender_email = 'arpandas0002941@gmail.com'
receiver_email = 'trashquery@gmail.com'
subject = 'Subject of the Email'
body = 'This is the body of the email.'
image_path = 'graph.png'
login = 'arpandas0002941@gmail.com'
app_password = 'hptf suhf zzvm thya'


send_email_with_attachment(smtp_server, port, sender_email,
                           receiver_email, subject, body, image_path, login, app_password)
