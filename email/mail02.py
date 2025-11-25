import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email():
    try:
        sender_email = "xyzdemo@gmail.com"
        app_password = "xmqe dvrd ncqq fqfo"   # Gmail App Password

        # List of all receivers
        receiver_emails = [
            "abcdemo@gmail.com",
            "test123@gmail.com",
            "user456@yahoo.com"
        ]

        # Create message container
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = ", ".join(receiver_emails)     # multiple emails
        msg['Subject'] = "mail from nipuna"

        # Email body
        msg.attach(MIMEText("This is a test message.", 'plain'))

        # Connect to Gmail SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, app_password)

        # Send mail to all emails in the list
        server.sendmail(sender_email, receiver_emails, msg.as_string())

        server.quit()

        print("Email sent successfully to multiple recipients.")

    except smtplib.SMTPException as e:
        print("SMTP Error:", e)
    except Exception as ex:
        print("General Error:", ex)

send_email()
