import smtplib
import ssl
from email.message import EmailMessage
from datetime import datetime


def send_email(email_senders_list, passwords_container, index_of_sender, email_receivers_list):
    email_sender = email_senders_list[index_of_sender]
    email_password = passwords_container[index_of_sender]

    # Generate a unique subject including the current timestamp
    subject = f"🛬 Imported 3D Printer! Arrived 🤑 Shop Now 🛒"

    # Read the HTML content from the file
    with open('index.html', 'r', encoding='utf-8') as file:
        body = file.read()

    # Connect to SMTP server and send the email
    context = ssl.create_default_context()

    for email_receiver in email_receivers_list:
        # Create a new EmailMessage for each receiver
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body, subtype='html')

        # Send the email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.send_message(em)
            print(f"Email sent successfully to {email_receiver}!")

    print("All emails sent successfully!")

