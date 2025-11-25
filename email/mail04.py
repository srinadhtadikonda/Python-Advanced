//multiple attachments
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email():
    try:
        sender_email = "xyzdemo@gmail.com"
        app_password = "xmqe dvrd ncqq fqfo"   # Gmail App Password
        receiver_email = "abcdemo@gmail.com"

        # Create message container
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = "mail from nipuna"

        # Email body
        msg.attach(MIMEText("This is a test message with multiple attachments.", 'plain'))

        # -------------------------
        # List of attachment file paths
        # -------------------------
        files = [
            "C:/Users/a.pdf",
            "C:/Users/b.jpg",
            "C:/Users/c.xlsx"
        ]

        # Attach each file
        for file_path in files:
            try:
                with open(file_path, "rb") as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())

                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename={file_path.split('/')[-1]}'
                )

                msg.attach(part)
            except Exception as fex:
                print(f"Could not attach file: {file_path}. Error: {fex}")
        # -------------------------

        # Connect to Gmail SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, app_password)

        # Send email
        server.send_message(msg)
        server.quit()

        print("Email sent successfully with multiple attachments.")

    except smtplib.SMTPException as e:
        print("SMTP Error:", e)
    except Exception as ex:
        print("General Error:", ex)

send_email()
