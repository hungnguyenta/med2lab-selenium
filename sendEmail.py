import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content, Personalization

def sendEmail():
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))


    from_email = Email("hung.nguyen@med2lab.com")  # Change to your verified sender
    # Replace these with your email addresses and names
    to_emails = [
        ('hung.nguyen@med2lab.com', 'Steven Universe'),
        ('Hungnm.nazzy@gmail.com', 'Garnet')
    ]

    subject = "Med2lab-SELENIUM Error script testing"
    content = Content("text/plain", "Hey, please take a look the scripts testing. We've got some error. Could you try at local to fix then upload the script to retry")
    mail = Mail(from_email,to_emails=to_emails,is_multiple=True, subject= subject,content = content)

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()

    # Send an HTTP POST request to /mail/send
    response = sg.client.mail.send.post(request_body=mail_json)
    print(response.status_code)
    print(response.headers)