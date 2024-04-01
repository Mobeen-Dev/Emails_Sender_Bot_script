from snd_mail import send_email
from Credential import email_senders, passwords
from email_from_csv import fetch_emails


if __name__ == "__main__":
    # Index of the desired sender
    selected_sender_index = 0  # Change this index as needed

    # Email receiver
    email_receiver = ["bscs23050@itu.edu.pk", "mubeenqamar29@gmail.com", "daroghawal@gmail.com",
                      "welding.info@yahoo.com"]
    #email_receiver = fetch_emails()
    for i in range(1):
        send_email(email_senders, passwords, selected_sender_index, email_receiver)
        print(i % len(email_senders))


fetch_emails()
