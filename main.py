from snd_mail import send_email
from Credential import email_senders, passwords # this is list of credentials i import from my Local computer u should use your own credentials
from email_from_csv import fetch_emails


if __name__ == "__main__":
    # Index of the desired sender
    selected_sender_index = 0  # Change this index as needed

    # Email receiver
    email_receiver = fetch_emails()

    for i in range(1):
        send_email(email_senders, passwords, selected_sender_index, email_receiver)
        
