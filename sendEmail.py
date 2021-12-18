import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content, Personalization

def sendEmail():
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))


    from_email = Email("hung.nguyen@med2lab.com")  # Change to your verified sender
    # Replace these with your email addresses and names
    person1 = Personalization()
    person1.add_to(Email ("hung.nguyen@med2lab.com"))
    person2 = Personalization()
    person2.add_to(Email ("hungnm.nazzy@gmail.com"))

    subject = "Med2lab-SELENIUM Error script testing"
    content = Content("text/plain", "Hey, please take a look the scripts testing. We've got some error. Could you try at local to fix then upload the script to retry")
    mail = Mail(from_email, None, subject, content, is_multiple=True)
    mail.add_personalization(person1)
    mail.add_personalization(person2)

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()

    # Send an HTTP POST request to /mail/send
    response = sg.client.mail.send.post(request_body=mail_json)
    print(response.status_code)
    print(response.headers)

sendEmail()