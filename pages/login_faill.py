from playwright.sync_api import Page


class LoginFaillChallenge:
    def __init__ (
            self,
            page: Page,
            user_selector: str,
            password_selector: str,
            button_selector: str,
            timeout = 4000
        ):
        self.page = page
        self.user_selector = user_selector
        self.password_selector = password_selector
        self.button_selector = button_selector
        self.timeout = timeout

    def login_fail_challenge(self, login_user: str, password: str):
        try:
            self.page.wait_for_selector(
                self.user_selector,
                timeout=self.timeout
            )

            self.page.locator(self.user_selector).fill(login_user)
            self.page.locator(self.password_selector).fill(password)

            self.page.locator(self.button_selector).click()

            print('Sucesso na falha de login, isso mesmo, sucesso na falha')

        except Exception as e:
            print (f'Log de erro ao fazer o fail login as {e}')