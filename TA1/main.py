import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# Import tkinter library

# Pass Tk as parameter


class EmailSenderApp():
    def __init__(self):
        super().__init__()
        # Set the title Email Sender

        # Create and arrange GUI elements

        # Create a Label with the name Sender's Email.

        # Create a Label with the name Sender's Password.

        # Create a Label with the name Message.

    def send_single_email(self):
        sender_email = input("Enter Sender Email\n")
        sender_password = input("Enter Sender Password\n")
        recipient_email = input("Enter Recipient Email\n")
        subject = input("Enter Email Subject\n")
        message_body = input("Enter Message\n")

        try:
            smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
            smtp_server.starttls()
            smtp_server.login(sender_email, sender_password)

            # Create and send the email
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = recipient_email
            message["Subject"] = subject
            message.attach(MIMEText(message_body, "plain"))

            smtp_server.sendmail(
                sender_email, recipient_email, message.as_string())
            smtp_server.quit()
            print("Email Sent", "Email sent successfully!")

        except Exception as e:
            print("Error", f"An error occurred: {str(e)}")


def main():
    app = EmailSenderApp()
    # Instead of send_single_email call mainloop() function
    app.send_single_email()


if __name__ == "__main__":
    main()
