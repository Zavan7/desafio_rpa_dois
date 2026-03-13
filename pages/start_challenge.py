from playwright.sync_api import Page


class StartChallenge:
    def __init__(
            self,
            page: Page,
            locator_challenge_two: str,
            user_selector: str,
            password_selector: str,
            button_selector: str,
            timeout: int=4000
        ):

        self.page = page
        self.locator_challenge_two = locator_challenge_two
        self.user_selector = user_selector
        self.password_selector = password_selector
        self.button_selector = button_selector
        self.timeout = timeout


    def login_page(self):
        try:
            self.page.wait_for_selector(
                self.locator_challenge_two,
                timeout = self.timeout
        )
            
            self.page.get_by_role('link', name='Test Login Page').click()
            print('Log de SUCESSO aqui (Test login page)')

        except Exception as e:
            print(f'Log de erro aqui {e}')


    def test_login_fail(self):
        ...