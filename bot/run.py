"""
Before running:
- Run in PyCharm Community Edition 2021.2.3
- Require install selenium through pip via command: pip install selenium
- ChromeDriver is place in directory "C:\SeleniumDrivers"
"""

import tinhte.change_password_testcases as PWT
import tinhte.upload_article_testcases as UAT
import tinhte.upload_fact_testcases as UFT

from tinhte.tinhte import Tinhte

account = "thomas.maihoanganhvu@gmail.com"
current_password = 19082001
new_password = 19082001  # although it's weird, it will make testing process easier

# Only run one testcase each time
# Please notice: after running Change Password testcase 6 or 7, you must change current password
# to new one to avoid errors!
"""
Create new fact with only images
pass
"""
with Tinhte() as bot:
    bot.land_first_page()
    bot.login(account, current_password)
    bot.create_new_fact(fill_text=False,
                        upload_image=True,
                        upload_many_images=True)
