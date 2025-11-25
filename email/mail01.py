import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email():
    try:
        sender_email = "srinadhtadikonda@gmail.com"
        app_password = "xmqe dvrd ncqq fqfo"   # Your Gmail App Password
        receiver_email = "pavanikrishnadola01@gmail.com"

        # Create message container
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = "mail from nipuna"

        # Email body
        msg.attach(MIMEText("This is a test message.", 'plain'))

        # Connect to Gmail SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, app_password)

        # Send email
        server.send_message(msg)
        server.quit()

        print("Email sent successfully.")

    except smtplib.SMTPException as e:
        print("SMTP Error:", e)
    except Exception as ex:
        print("General Error:", ex)


send_email()
