import smtplib
import os
from tkinter import *
from tkinter import filedialog, messagebox
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

attachments = []  # global list for all attachments

# -------------------------------------------------------------
# Add individual files
# -------------------------------------------------------------
def add_attachments():
    files = filedialog.askopenfilenames(title="Select Attachments")
    for f in files:
        attachments.append(f)
    attach_label.config(text=f"{len(attachments)} file(s) attached")

# -------------------------------------------------------------
# Add all files inside a selected folder
# -------------------------------------------------------------
def add_folder_attachments():
    folder = filedialog.askdirectory(title="Select Folder")
    if folder:
        for filename in os.listdir(folder):
            full_path = os.path.join(folder, filename)
            if os.path.isfile(full_path):
                attachments.append(full_path)
        attach_label.config(text=f"{len(attachments)} file(s) attached")

# -------------------------------------------------------------
# Send Email
# -------------------------------------------------------------
def send_email():
    try:
        sender = sender_entry.get()
        password = pass_entry.get()

        to_list = [email.strip() for email in to_entry.get().split(",") if email.strip()]
        cc_list = [email.strip() for email in cc_entry.get().split(",") if email.strip()]
        bcc_list = [email.strip() for email in bcc_entry.get().split(",") if email.strip()]

        all_receivers = to_list + cc_list + bcc_list

        subject = subject_entry.get()
        body = body_text.get("1.0", END)

        # Email container
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = ", ".join(to_list)
        msg['Cc'] = ", ".join(cc_list)
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        # Attach all files
        for file in attachments:
            try:
                with open(file, "rb") as f:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(f.read())

                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename="{os.path.basename(file)}"'
                )
                msg.attach(part)

            except Exception as e:
                messagebox.showerror("Attachment Error", f"Cannot attach {file}\n{e}")

        # SMTP
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, all_receivers, msg.as_string())
        server.quit()

        messagebox.showinfo("Success", "Email sent successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email\n{e}")

# -------------------------------------------------------------
# Tkinter GUI
# -------------------------------------------------------------
root = Tk()
root.title("Email Sender - To / CC / BCC / Folder Attachments")
root.geometry("600x700")

Label(root, text="Sender Email:").pack()
sender_entry = Entry(root, width=60)
sender_entry.pack()

Label(root, text="App Password:").pack()
pass_entry = Entry(root, width=60, show="*")
pass_entry.pack()

Label(root, text="To (comma separated):").pack()
to_entry = Entry(root, width=60)
to_entry.pack()

Label(root, text="CC (comma separated):").pack()
cc_entry = Entry(root, width=60)
cc_entry.pack()

Label(root, text="BCC (comma separated):").pack()
bcc_entry = Entry(root, width=60)
bcc_entry.pack()

Label(root, text="Subject:").pack()
subject_entry = Entry(root, width=60)
subject_entry.pack()

Label(root, text="Body:").pack()
body_text = Text(root, height=10, width=60)
body_text.pack()

Button(root, text="Add Files", command=add_attachments).pack(pady=5)
Button(root, text="Add Entire Folder", command=add_folder_attachments).pack(pady=5)

attach_label = Label(root, text="No attachments selected")
attach_label.pack()

send_btn = Button(root, text="Send Email", command=send_email,
                  bg="green", fg="white", width=20)
send_btn.pack(pady=10)

root.mainloop()
