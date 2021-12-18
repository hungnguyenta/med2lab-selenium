# import pytest
# args_str = "-k test_myfavorite"
# args = args_str.split(" ")
# pytest.main(args)
import yagmail

receiver = "your@gmail.com"
body = "Hello there from Yagmail"
filename = "document.pdf"

yag = yagmail.SMTP("hungnm.nazzy@gmail.com")
yag.send(
    to=receiver,
    subject="Yagmail test with attachment",
    contents=body, 
)