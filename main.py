from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os
import logging
from time import sleep

from config.log import setup_logging
from pages.initial_page import InitialPage
from pages.start_challenge import StartChallenge
from pages.login_faill import LoginFaillChallenge

from validators.validator import Validation


# 🔥 inicializa logging (TEM QUE SER NO TOPO)
setup_logging()
logger = logging.getLogger(__name__)

load_dotenv()

LOGIN_USER = os.getenv('USERNAME')
PASSWORD_USER = os.getenv('PASSWORD')


def second_challenge():

    '''
    Orquestra o fluxo completo do desafio de automação utilizando Playwright,
    validando o comportamento de login com falha e a exibição da mensagem de erro.

    Configurações:
    - Define URL da aplicação
    - Define seletores necessários para navegação e interação
    - Carrega credenciais via variáveis de ambiente

    Fluxo:
    - Inicializa o navegador e cria uma nova página
    - Acessa a página inicial do desafio
    - Navega até a página de login (Test Login Page)
    - Executa tentativa de login com falha (credenciais inválidas)
    - Realiza a validação da mensagem de erro exibida na tela
    - Registra logs em cada etapa do processo
    - Finaliza a execução encerrando o navegador

    Tratamento de erros:
    - Caso qualquer etapa falhe, registra erro crítico no log
    - Cada componente já possui seu próprio tratamento interno

    Retorno:
    - None: função orquestradora, não retorna valor
    - O sucesso ou falha deve ser analisado via logs da execução
    '''


    url = 'https://practicetestautomation.com/'
    selector_challenge_one = '#menu-item-20'
    test_login_page = 'a[href*="practice-test-login"]'
    locator_login = '#username'
    locator_password = '#password'
    submit_button = '#submit'
    msg_validator = '#error'

    logger.info('Iniciando execução do desafio')

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()

        try:
            initial_page = InitialPage(url, selector_challenge_one)
            result_initial = initial_page.practice_page(page)

            if not result_initial:
                logger.warning('Falha ao acessar página inicial')
                return

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

            result_login = login_fail_challenge.login_fail_challenge(
                LOGIN_USER,
                PASSWORD_USER
            )

            if not result_login:
                logger.warning('Login falhou conforme esperado')

            final_validation = Validation(msg_validator)
            final_validation.final_validation(page)

            sleep(5)

        except Exception:
            logger.error('Erro crítico na execução do fluxo', exc_info=True)

        finally:
            browser.close()
            logger.info('Execução finalizada')


if __name__ == '__main__':
    second_challenge()