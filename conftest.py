import pytest
from sendEmail import sendEmail

def pytest_terminal_summary(terminalreporter, exitstatus):
    if(exitstatus == pytest.ExitCode.OK):
        print("TEST OK")
    else:
        print("SEND EMAIL HERE")
        sendEmail()