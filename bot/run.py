'''
Before running:
- Run in PyCharm Community Edition 2021.2.3
- Require install selenium through pip via command: pip install selenium
- ChromeDriver is place in directory "C:\SeleniumDrivers"
'''

from tinhte.tinhte import Tinhte

with Tinhte() as bot:
    account = "thomas.maihoanganhvu@gmail.com"
    current_password = 2
    new_password = 2

    bot.land_first_page()
    bot.login("thomas.maihoanganhvu@gmail.com", current_password)
    # bot.change_password(current_password, new_password)
    # bot.create_new_article()
    # bot.create_new_fact()
