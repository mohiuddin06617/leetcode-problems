def validate_email(email):
    pass


def num_unique_emails(emails) -> int:
    for email in emails:
        if validation_pass := validate_email(email):
            pass
        return len(emails)
