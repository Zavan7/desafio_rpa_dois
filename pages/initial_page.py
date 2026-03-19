from playwright.sync_api import Page
import logging

logger = logging.getLogger(__name__)


class InitialPage:
    def __init__(self, url: str, selector_page: str, timeout=4000):
        self.url = url
        self.selector_page = selector_page
        self.timeout = timeout

    def practice_page(self, page: Page) -> bool:
        try:
            logger.info(
                "Acessando página",
                extra={"url": self.url}
            )

            page.goto(self.url)

            page.wait_for_selector(
                self.selector_page,
                timeout=self.timeout
            )

            button = page.locator(self.selector_page)

            if not button.is_enabled():
                logger.warning(
                    "Botão encontrado, mas desabilitado",
                    extra={"selector": self.selector_page}
                )
                return False

            button.click()

            logger.info(
                "Click realizado com sucesso",
                extra={"selector": self.selector_page}
            )

            return True

        except Exception:
            logger.error(
                "Erro ao acessar a página do desafio",
                exc_info=True,
                extra={
                    "url": self.url,
                    "selector": self.selector_page
                }
            )
            return False