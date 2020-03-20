import random


def test_registration(browser):
    # Проверка первичной регистрации посетителя страницы, наличия фразы "Спасибо за регистрацию!" на конечной
    # странице регистрации
        random_email = "ghfjj@j%s.ru" % random.randint(1, 10000)
    # self.random_email = "ghfjj@j123.ru"
        #self.password = "Alekseevaa
        link = "http://selenium1py.pythonanywhere.com/ru/"
        browser.get(link)
        registration = browser.find_element_by_id("login_link")
        registration.click()
        input1 = browser.find_element_by_name("registration-email")
        input1.send_keys(random_email)
        input2 = browser.find_element_by_name("registration-password1")
        input2.send_keys("48g3ui48g3ui48g3ui")
        input3 = browser.find_element_by_name("registration-password2")
        input3.send_keys("48g3ui48g3ui48g3ui")
        button = browser.find_element_by_name("registration_submit")
        button.click()
        assert browser.find_element_by_class_name("alertinner").is_displayed(), \
    'Регистрация прошла неуспешно!'
