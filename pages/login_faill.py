from playwright.sync_api import Page
import logging

logger = logging.getLogger(__name__)


class LoginFaillChallenge:
    def __init__(
        self,
        page: Page,
        user_selector: str,
        password_selector: str,
        button_selector: str,
        timeout=4000
    ):
        self.page = page
        self.user_selector = user_selector
        self.password_selector = password_selector
        self.button_selector = button_selector
        self.timeout = timeout

    def login_fail_challenge(self, login_user: str, password: str) -> bool:
        try:
            logger.info(
                "Iniciando tentativa de login (esperando falha)",
                extra={"user": login_user}
            )

            self.page.wait_for_selector(
                self.user_selector,
                timeout=self.timeout
            )

            self.page.locator(self.user_selector).fill(login_user)
            self.page.locator(self.password_selector).fill(password)

            logger.debug("Campos de login preenchidos")

            self.page.locator(self.button_selector).click()

            logger.info(
                "Login executado (falha esperada)",
                extra={"user": login_user}
            )

            return True

        except Exception:
            logger.error(
                "Erro ao executar login de falha",
                exc_info=True,
                extra={
                    "user": login_user,
                    "selector_user": self.user_selector,
                    "selector_button": self.button_selector
                }
            )

            # opcional: screenshot para debug
            try:
                self.page.screenshot(path="logs/error_login_fail.png")
            except Exception:
                logger.warning("Falha ao capturar screenshot do erro")

            return False