import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email():
    try:
        sender_email = "xyzdemo@gmail.com"
        app_password = "xmqe dvrd ncqq fqfo"   # Gmail App Password

        # -------------------------
        # Multiple Recipients
        # -------------------------
        recipients = [
            "abcdemo@gmail.com",
            "testuser1@gmail.com",
            "testuser2@yahoo.com"
        ]

        # Create mail container
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = ", ".join(recipients)
        msg['Subject'] = "Mail with Multiple Recipients and Attachments"

        # Email body
        msg.attach(MIMEText("This is a test email with multiple recipients and attachments.", 'plain'))

        # -------------------------
        # Multiple Attachments
        # -------------------------
        attachment_files = [
            "C:/Users/file1.pdf",
            "C:/Users/file2.jpg",
            "C:/Users/file3.xlsx"
        ]

        for file_path in attachment_files:
            try:
                with open(file_path, "rb") as file:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(file.read())

                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename={file_path.split('/')[-1]}'
                )

                msg.attach(part)

            except Exception as e:
                print(f"Error attaching {file_path}: {e}")

        # -------------------------
        # SMTP Send Mail
        # -------------------------
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, recipients, msg.as_string())
        server.quit()

        print("Email sent successfully with multiple recipients and attachments.")

    except smtplib.SMTPException as smtp_error:
        print("SMTP Error:", smtp_error)
    except Exception as ex:
        print("General Error:", ex)

send_email()
