import yagmail
import pytest
def pytest_terminal_summary(terminalreporter, exitstatus):
    if(exitstatus == pytest.ExitCode.OK):
        print("TEST OK")
        # sendEmail()
    else:
        print("SEND EMAIL HERE")

def sendEmail():
    receiver = "hungnm.nazzy@gmail.com"
    body = "Hello there from Yagmail"

    yag = yagmail.SMTP("hungnm.nazzy@gmail.com")
    yag.send(
        to=receiver,
        subject="Yagmail test with attachment",
        contents=body, 
    )