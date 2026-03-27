FROM ghcr.io/astral-sh/uv:0.9.17-trixie-slim AS builder

ENV UV_COMPILE_BYTECODE=1 \
  UV_LINK_MODE=copy \
  UV_PYTHON_PREFERENCE=only-managed \
  UV_NO_DEV=1 \
  UV_PYTHON_INSTALL_DIR=/python

RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Python gerenciado pelo uv
RUN uv python install 3.14.2

WORKDIR /app

# Cache inteligente das deps
RUN --mount=type=cache,target=/root/.cache/uv \
  --mount=type=bind,source=uv.lock,target=uv.lock \
  --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
  uv sync --frozen --no-install-project

# Copia projeto
COPY . /app

# Instala projeto + deps
RUN --mount=type=cache,target=/root/.cache/uv \
  uv sync --frozen

################################################################################

FROM debian:trixie-slim AS runtime

ENV PYTHONUNBUFFERED=1

# 🔥 DEPENDÊNCIAS DO PLAYWRIGHT (ESSENCIAL)
RUN apt-get update && apt-get install -y --no-install-recommends \
  libnss3 \
  libatk1.0-0 \
  libatk-bridge2.0-0 \
  libcups2 \
  libxkbcommon0 \
  libxcomposite1 \
  libxdamage1 \
  libxrandr2 \
  libgbm1 \
  libasound2 \
  libpangocairo-1.0-0 \
  libpango-1.0-0 \
  libcairo2 \
  libx11-xcb1 \
  libx11-6 \
  libxcb1 \
  libxext6 \
  libxi6 \
  libxtst6 \
  curl \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Usuário não-root
RUN groupadd --gid 1000 python \
  && useradd --uid 1000 --gid python --shell /bin/bash --create-home python

# Copia ambiente do builder
COPY --from=builder --chown=python:python /python /python
COPY --from=builder --chown=python:python /app /app

ENV PATH="/app/.venv/bin:${PATH}"

WORKDIR /app
USER python

# 🔥 Instala browsers do Playwright
RUN uv run playwright install --with-deps

# 🔥 Ajuste principal: rodar sua automação (não API)
CMD ["uv", "run", "python", "main.py"]