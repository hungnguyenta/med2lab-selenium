import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content, Personalization

def sendEmail():
    to_emails = [
        ('hungnm.nazzy@gmail.com', 'Steven Universe'),
        ('hung.nguyen@med2lab.com', 'Garnet')
    ]

    message = Mail(
        from_email=('hung.nguyen@med2lab.com', 'Sadie Miller'),
        subject='🍩 Donuts, at the big donut 🍩',
        html_content='<p>Fresh donuts are out of the oven. Get them while they’re <em>hot!</em></p>',
        # for improved deliverability, provide plain text content in addition to html content
        plain_text_content='Fresh donuts are out of the oven. Get them while they’re hot!',
        to_emails=to_emails,
        is_multiple=True)
    try:
        sendgrid_client = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

        response = sendgrid_client.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)