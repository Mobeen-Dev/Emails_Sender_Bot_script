import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope and credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("All google api Authentication key.json", scope)

# Authorize the client
client = gspread.authorize(creds)


def fetch_emails(sheet_name="3D Customer", worksheet_name="Potential_Customer", column_letter="D"):
    # Open the Google Sheet
    sheet = client.open(sheet_name).worksheet(worksheet_name)

    # Convert column letter to index
    column_index = ord(column_letter.upper()) - ord('A') + 1

    # Fetch all values in the specified column
    email_column = sheet.col_values(column_index)

    # Remove header row
    email_column = email_column[1:]
    email_column = list(set(email_column))

    return email_column[1:]


# #Example usage
# if __name__ == "__main__":
#     sheet_name = "3D Customer"
#     column = "D"  # Assuming column D contains email addresses
#     emails = fetch_emails(sheet_name, "Potential_Customer", column)
#     print("Emails:")
#     print(emails)
