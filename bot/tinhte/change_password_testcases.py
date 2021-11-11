from tinhte.tinhte import Tinhte

account = "thomas.maihoanganhvu@gmail.com"
current_password = 19082001
new_password = 19082001 # although it's weird, it will make testing process easier


def testcase_1():
    """
    Change password with all fields filled correctly
    Will pass
    """
    with Tinhte() as bot:
        bot.land_first_page()
        bot.login(account, current_password)
        bot.change_password(current_password, new_password,
                            fill_current_password=True,
                            fill_new_password=True,
                            fill_confirm_password=True,
                            expected_to_have_error=False,
                            fill_wrong_confirm_password=False)


def testcase_2():
    """
    Change password without current password
    Will pass
    """
    with Tinhte() as bot:
        bot.land_first_page()
        bot.login(account, current_password)
        bot.change_password(current_password, new_password,
                            fill_current_password=False,
                            fill_new_password=True,
                            fill_confirm_password=True,
                            expected_to_have_error=True,
                            fill_wrong_confirm_password=False)


def testcase_3():
    """
    Change password without new password
    Will pass
    """
    with Tinhte() as bot:
        bot.land_first_page()
        bot.login(account, current_password)
        bot.change_password(current_password, new_password,
                            fill_current_password=True,
                            fill_new_password=False,
                            fill_confirm_password=True,
                            expected_to_have_error=True,
                            fill_wrong_confirm_password=False)


def testcase_4():
    """
    Change password without re-password
    Will pass
    """
    with Tinhte() as bot:
        bot.land_first_page()
        bot.login(account, current_password)
        bot.change_password(current_password, new_password,
                            fill_current_password=True,
                            fill_new_password=True,
                            fill_confirm_password=False,
                            expected_to_have_error=True,
                            fill_wrong_confirm_password=False)


def testcase_5():
    """
    Change password with wrong re-password
    Will pass
    """
    with Tinhte() as bot:
        bot.land_first_page()
        bot.login(account, current_password)
        bot.change_password(current_password, new_password,
                            fill_current_password=True,
                            fill_new_password=True,
                            fill_confirm_password=True,
                            expected_to_have_error=True,
                            fill_wrong_confirm_password=True)


def testcase_6():
    """
    Change password with weak password (e.g: 123456)
    Will failed
    """
    with Tinhte() as bot:
        bot.land_first_page()
        bot.login(account, current_password)

        temp_new_password = 123456
        bot.change_password(current_password, temp_new_password,
                            fill_current_password=True,
                            fill_new_password=True,
                            fill_confirm_password=True,
                            expected_to_have_error=True,
                            fill_wrong_confirm_password=False)

        # Because password will be change into new password
        # So you have to change current password to 123456 to make sure there will be no error for next other testcases


def testcase_7():
    """
    Change password with only specific letters password
    Will failed
    """
    with Tinhte() as bot:
        bot.land_first_page()
        bot.login(account, current_password)

        temp_new_password = "@"

        bot.change_password(current_password, temp_new_password,
                            fill_current_password=True,
                            fill_new_password=True,
                            fill_confirm_password=True,
                            expected_to_have_error=True,
                            fill_wrong_confirm_password=False)

        # Because password will be change into new password
        # So you have to change current password to "@" to make sure there will be no error for next other testcases
