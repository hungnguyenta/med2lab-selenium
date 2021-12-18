# import sendgrid
# import os
# from sendgrid.helpers.mail import Mail, Email, To, Content, Personalization

# def sendEmail():
#     sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
#     print(os.environ.get("SENDGRID_API_KEY"))

#     from_email = Email("hung.nguyen@med2lab.com")  # Change to your verified sender
#     # Replace these with your email addresses and names
#     person1 = Personalization()
#     person1.add_to(Email ("hung.nguyen@med2lab.com"))
#     person2 = Personalization()
#     person2.add_to(Email ("hungnm.nazzy@gmail.com"))

#     subject = "Med2lab-SELENIUM Error script testing"
#     content = Content("text/plain", "Hey, please take a look the scripts testing. We've got some error. Could you try at local to fix then upload the script to retry")
#     mail = Mail(from_email, subject,None, content, is_multiple=True)
#     mail.add_personalization(person1)
#     mail.add_personalization(person2)

#     # Get a JSON-ready representation of the Mail object
#     mail_json = mail.get()

#     # Send an HTTP POST request to /mail/send
#     response = sg.client.mail.send.post(request_body=mail_json)
#     print(response.status_code)
#     print(response.headers)

# sendEmail()

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Replace these with your email addresses and names
to_emails = [
    ('hungnm.nazzy@gmail.com', 'Steven Universe'),
    ('hung.nguyen@huuk.social', 'Garnet')
]

message = Mail(
    from_email=('hung.nguyen@med2lab.com', 'Hung Nguyen'),
    subject='🍩 Donuts, at the big donut 🍩',
    html_content='<p>Fresh donuts are out of the oven. Get them while they’re <em>hot!</em></p>',
    # for improved deliverability, provide plain text content in addition to html content
    plain_text_content='Fresh donuts are out of the oven. Get them while they’re hot!',
    to_emails=to_emails,
    is_multiple=True)
try:
    sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    print(os.environ.get('SENDGRID_API_KEY'))
    response = sendgrid_client.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)


