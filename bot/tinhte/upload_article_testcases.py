from tinhte.tinhte import Tinhte

account = "thomas.maihoanganhvu@gmail.com"
current_password = 19082001
new_password = 19082001  # although it's weird, it will make testing process easier


def testcase_1():
    """
    Create new article with caption and an image
    pass
    """
    with Tinhte() as bot:
        bot.land_first_page()
        bot.login(account, current_password)
        bot.create_new_article(fill_text=True,
                               insert_link=False,
                               upload_image=True,
                               upload_many_images=False)


def testcase_2():
    """
    Create new article with caption and many images
    pass
    """
    with Tinhte() as bot:
        bot.land_first_page()
        bot.login(account, current_password)
        bot.create_new_article(fill_text=True,
                               insert_link=False,
                               upload_image=True,
                               upload_many_images=True)


def testcase_3():
    """
    Create new article with only caption
    pass
    """
    with Tinhte() as bot:
        bot.land_first_page()
        bot.login(account, current_password)
        bot.create_new_article(fill_text=True,
                               insert_link=False,
                               upload_image=False,
                               upload_many_images=False)


def testcase_4():
    """
    Create new article without caption, link and images
    pass
    """
    with Tinhte() as bot:
        bot.land_first_page()
        bot.login(account, current_password)
        bot.create_new_article(fill_text=False,
                               insert_link=False,
                               upload_image=False,
                               upload_many_images=False)


def testcase_5():
    """
    Create new article with only images
    pass
    """
    with Tinhte() as bot:
        bot.land_first_page()
        bot.login(account, current_password)
        bot.create_new_article(fill_text=False,
                               insert_link=False,
                               upload_image=True,
                               upload_many_images=True)


def testcase_6():
    """
    Create new article with caption and link
    pass
    """
    with Tinhte() as bot:
        bot.land_first_page()
        bot.login(account, current_password)
        bot.create_new_article(fill_text=True,
                               insert_link=True,
                               upload_image=False,
                               upload_many_images=False)
