import csv


def fetch_emails(file_path="customers_export.csv", column_index=4, skip_header=True):
    """
    Fetches email addresses from a CSV file.

    Args:
        file_path (str): Path to the CSV file.
        column_index (int): Index of the column containing email addresses (1-based).
        skip_header (bool): Whether to skip the header row.

    Returns:
        list: A list of unique email addresses.
    """
    email_column = []

    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if skip_header:
                skip_header = False
                continue
            email = row[column_index - 1].strip()  # Adjust index to 0-based
            if email:
                email_column.append(email)
    return list(set(email_column))
