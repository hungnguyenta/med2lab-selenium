import pytest
def pytest_terminal_summary(terminalreporter, exitstatus):
    if(exitstatus == pytest.ExitCode.OK):
        print("TEST OK")
        # sendEmail()
    else:
        print("SEND EMAIL HERE")