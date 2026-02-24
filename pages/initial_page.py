from playwright.sync_api import Page

class InitialPage:
    def __init__(self, url: str, selector_page: str, timeout=4000):
        self.url = url
        self.selector_page = selector_page
        self.timeout = timeout

    def practice_page(self, page: Page) -> True:
        try:
            page.goto(self.url)
            page.wait_for_selector(
                self.selector_page,
                timeout=self.timeout
            )

            button = page.locator(self.selector_page)

            if not button.is_enabled():
                return False
            
            button.click()
            print('Log de sucesso ao acessar o inicio do desafio')

        except Exception as e:
            print ('Log de erro ao acessar a página iniciar do desafio')
            print (f'Erro: {e}')