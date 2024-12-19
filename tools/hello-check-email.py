
import requests
from hello_message import Hello

class EmailChecker:
    def __init__(self, hello_signature: str):
        """Initialize with a pre-signed Hello protocol signature"""
        self.signature = hello_signature

    def check_new_emails(self) -> dict:
        """
        Check for new emails using the Hello protocol authentication
        Returns a dictionary containing email data from the AIMX mail system
        """
        try:
            response = requests.post(
                "https://mail.aimx.com/inbox",
                headers={
                    "Authorization": self.signature,
                    "Content-Type": "application/json"
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"Failed to check emails: {str(e)}")

    def get_unread_count(self) -> int:
        """Get the count of unread emails"""
        try:
            emails = self.check_new_emails()
            return len([email for email in emails.get('messages', []) if not email.get('read', False)])
        except Exception as e:
            raise Exception(f"Failed to get unread count: {str(e)}")
