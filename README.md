# RPA UV Dois

## 📌 Descrição

Este projeto implementa um sistema de automação robótica de processos (RPA) utilizando Playwright com Python. O foco principal é validar cenários de falha no login de aplicações web, garantindo que as mensagens de erro sejam exibidas corretamente após tentativas de autenticação inválidas.

> ⚠️ **Aviso Importante**
> Esta aplicação ainda está em desenvolvimento ativo e pode sofrer alterações significativas na estrutura, funcionalidades e implementação ao longo do tempo.

## 🎯 Objetivos

- Automatizar o fluxo de navegação e interação com interfaces web.
- Validar o comportamento da aplicação em cenários de erro de login.
- Registrar logs detalhados de cada etapa do processo.
- Persistir os resultados das execuções em um banco de dados MongoDB.

## 🚀 Funcionalidades

- **Navegação Automatizada**: Acesso a páginas web e interação com elementos DOM.
- **Teste de Login com Falha**: Simulação de tentativas de login inválidas.
- **Validação de Mensagens**: Verificação da presença e conteúdo de mensagens de erro.
- **Persistência de Dados**: Armazenamento de resultados em MongoDB.
- **Logging Estruturado**: Registros detalhados em formato JSON para auditoria.

## 📋 Pré-requisitos

- Python 3.14 ou superior
- MongoDB (local ou remoto)
- Navegador Firefox (instalado automaticamente pelo Playwright)

## 🛠️ Instalação

1. **Clone o repositório**:
   ```bash
   git clone <url-do-repositorio>
   cd rpa-uv-dois
   ```

2. **Crie um ambiente virtual**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # No Windows: .venv\Scripts\activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install -e .
   ```

4. **Instale os navegadores do Playwright**:
   ```bash
   playwright install firefox
   ```

5. **Configure as variáveis de ambiente**:
   - Copie o arquivo `env-exemple` para `.env`
   - Preencha as variáveis necessárias (USERNAME, PASSWORD, URL do MongoDB, etc.)

## ⚙️ Configuração

### Variáveis de Ambiente (.env)
```env
USERNAME=seu_usuario
PASSWORD=sua_senha
MONGODB_URL=mongodb://localhost:27017/
DATABASE_NAME=rpa_db
```

### MongoDB
Certifique-se de que o MongoDB esteja rodando e acessível. O projeto cria automaticamente a coleção `executions` para armazenar os resultados.

## 📖 Uso

Execute o script principal para iniciar a automação:

```bash
python main.py
```

O fluxo executará automaticamente:
1. Acesso à página inicial do desafio
2. Navegação para a página de login
3. Tentativa de login com credenciais inválidas
4. Validação da mensagem de erro
5. Persistência do resultado no banco de dados

## 📁 Estrutura do Projeto

```
rpa-uv-dois/
├── config/
│   └── log.py              # Configuração de logging
├── db/
│   └── mongo.py            # Integração com MongoDB
├── pages/
│   ├── initial_page.py     # Página inicial do desafio
│   ├── start_challenge.py  # Navegação para login
│   └── login_faill.py      # Teste de login com falha
├── utils/
│   └── validators/
│       └── validator.py    # Validações de elementos
├── downloads/              # Arquivos baixados (se aplicável)
├── logs/                   # Arquivos de log
├── main.py                 # Script principal
├── pyproject.toml          # Configuração do projeto
├── env-exemple             # Exemplo de variáveis de ambiente
└── README.md               # Este arquivo
```

## 🔄 Fluxo da Automação

1. **Inicialização**: Configuração do navegador e conexão com MongoDB
2. **Acesso Inicial**: Navegação para a URL da aplicação
3. **Iniciar Desafio**: Clique no elemento que inicia o teste
4. **Página de Login**: Navegação para a página de autenticação
5. **Tentativa de Login**: Preenchimento com credenciais inválidas
6. **Validação**: Verificação da mensagem de erro exibida
7. **Persistência**: Salvamento dos resultados no banco de dados
8. **Finalização**: Encerramento do navegador e logs finais

## 📊 Resultados

Cada execução é armazenada no MongoDB com os seguintes campos:
- `start_date`: Data/hora de início (UTC)
- `end_date`: Data/hora de fim (UTC)
- `duration`: Duração da execução
- `status`: Status da execução (Success/Error)
- `message`: Mensagem descritiva
- `error`: Detalhes do erro (se aplicável)

## 🧪 Testes

Para executar testes (se implementados):
```bash
pytest
```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📞 Suporte

Para dúvidas ou problemas, abra uma issue no repositório.  

---

## 📊 Logs e Observabilidade

O projeto utiliza logging estruturado para fornecer visibilidade completa da execução:

- `INFO`: etapas principais do fluxo  
- `DEBUG`: detalhes técnicos  
- `WARNING`: comportamentos inesperados  
- `ERROR`: falhas com stack trace  

---

## 🔐 Variáveis de Ambiente

As credenciais são carregadas via `.env`:

```env
USERNAME=CHANGE ME
PASSWORD=CHANGE ME

MONGO_URI=CHANGE ME
MONGO_DB=rCHANGE ME

USE_MONGO=CHANGE ME