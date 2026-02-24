from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os
from time import sleep

from pages.initial_page import InitialPage

load_dotenv()


def second_challenge():
    url = 'https://practicetestautomation.com/'
    selector_challenge_one = '#menu-item-20'

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()

        initial_page = InitialPage(url, selector_challenge_one)
        initial_page.practice_page(page)

        sleep(5)

        browser.close()


if __name__ == '__main__':
    second_challenge()