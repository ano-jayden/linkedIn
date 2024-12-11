# --- Email Class --- #
class Email:
    """Represents an email with basic details and a read/unread status."""
    
    # Class variable to track if the email has been read, with a default value of False
    has_been_read = False

    def __init__(self, email_address, subject_line, email_content):
        """Initialize the email with an address, subject, and content."""
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    def mark_as_read(self):
        """Mark the email as read."""
        self.has_been_read = True


# --- Lists --- #
# Initialize an empty list to store email objects
inbox = []


# --- Functions --- #
def populate_inbox():
    """Create 3 sample emails and add them to the inbox list."""
    inbox.append(
        Email("alice@example.com", "Meeting Reminder", "Don't forget our meeting tomorrow at 10 AM.")
    )
    inbox.append(
        Email("bob@example.com", "Greetings", "Hello! How have you been?")
    )
    inbox.append(
        Email("carol@example.com", "Project Update", "The project deadline has been extended by a week.")
    )


def list_emails():
    """Print the email’s subject line along with a corresponding number."""
    for index, email in enumerate(inbox):
        print(f"{index} {email.subject_line}")


def read_email(index):
    """Display a selected email and mark it as read."""
    if 0 <= index < len(inbox):
        email = inbox[index]
        print(f"\nEmail from: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"Content: {email.email_content}")
        email.mark_as_read()
        print(f"\nEmail from {email.email_address} marked as read.\n")
    else:
        print("Invalid index. Please try again.")


# --- Email Program --- #
# Populate the inbox with sample emails
populate_inbox()

# Fill in the logic for the various menu operations.
menu = True

while menu:
    user_choice = input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: ''')

    if user_choice.isnumeric():
        user_choice = int(user_choice)
        if user_choice == 1:
            list_emails()
            index = input("Enter the index of the email you want to read: ")
            if index.isnumeric():
                read_email(int(index))
            else:
                print("Please enter a valid number.")
        elif user_choice == 2:
            print("\nUnread Emails:")
            for index, email in enumerate(inbox):
                if not email.has_been_read:
                    print(f"{index} {email.subject_line}")
        elif user_choice == 3:
            print("Goodbye!")
            menu = False
        else:
            print("Oops - incorrect input.")
    else:
        print("Please enter a valid number.")


