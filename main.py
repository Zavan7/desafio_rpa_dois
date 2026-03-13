from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os
from time import sleep

from pages.initial_page import InitialPage
from pages.start_challenge import StartChallenge
from pages.login_faill import LoginFaillChallenge

load_dotenv()


LOGIN_USER = os.getenv('USERNAME')
PASSWORD_USER = os.getenv('PASSWORD')

def second_challenge():
    url = 'https://practicetestautomation.com/'
    selector_challenge_one = '#menu-item-20'
    test_login_page = 'a[href*="practice-test-login"]'
    test_login_page = 'a[href*="practice-test-login"]'
    locator_login = '#username'
    locator_password = '#password'
    submit_button = '#submit'

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()

        initial_page = InitialPage(url, selector_challenge_one)
        initial_page.practice_page(page)

        page_challenge = StartChallenge(
            page,
            test_login_page,
            locator_login,
            locator_password,
            submit_button
        )

        page_challenge.login_page()

        login_fail_challenge = LoginFaillChallenge(
            page,
            locator_login,
            locator_password,
            submit_button
        )

        login_fail_challenge.login_fail_challenge(LOGIN_USER, PASSWORD_USER)

        sleep(5)

        browser.close()


if __name__ == '__main__':
    second_challenge()