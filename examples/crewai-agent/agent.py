from crewai import Agent
from hello_message import Hello
import requests

class EmailCheckerAgent:
    def __init__(self, private_key):
        self.hello = Hello(private_key)
        self.agent = Agent(
            role='Email Checker',
            goal='Check and process emails from the inbox',
            backstory='I am an agent responsible for checking emails',
            tools=[self.check_emails]
        )

    def check_emails(self) -> str:
        """Check emails from the inbox using hello_message authentication"""
        try:
            response = requests.post(
                "https://mail.aimx.com/inbox",
                headers={"Authorization": self.hello.get_signature}
            )
            return response.json()
        except Exception as e:
            return f"Error checking emails: {str(e)}"

    def run(self):
        return self.agent.execute()

if __name__ == "__main__":
    private_key = "0x4c0883a6910395b1e8dcd7db363c124593f3e8e62e4a8c32ef45b3ef82317b03"
    email_agent = EmailCheckerAgent(private_key)
    result = email_agent.run()
    print(result)