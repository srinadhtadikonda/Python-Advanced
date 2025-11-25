#send mail with attachment
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

        # Create email container
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = "mail from nipuna"

        # Email body
        msg.attach(MIMEText("This is a test message with attachment.", 'plain'))

        # -------------------------
        # Add Attachment
        # -------------------------
        file_path = "C:/Users/YourFile.txt"   # CHANGE FILE PATH

        with open(file_path, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            f'attachment; filename={file_path.split("/")[-1]}'
        )

        msg.attach(part)
        # -------------------------

        # Gmail SMTP connection
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, app_password)

        # Send email
        server.send_message(msg)
        server.quit()

        print("Email sent successfully with attachment.")

    except smtplib.SMTPException as e:
        print("SMTP Error:", e)
    except Exception as ex:
        print("General Error:", ex)

send_email()
