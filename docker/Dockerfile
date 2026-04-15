# =========================
# STAGE 1 - BUILDER
# =========================
FROM ghcr.io/astral-sh/uv:0.9.17-trixie-slim AS builder

ENV UV_PYTHON_INSTALL_DIR=/python

RUN uv python install 3.14.2

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project

COPY . /app
RUN uv sync --frozen


# =========================
# STAGE 2 - RUNTIME
# =========================
FROM debian:trixie-slim

ENV PYTHONUNBUFFERED=1

# deps playwright
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

# usuário
RUN useradd -m python

# 🔥 copia PYTHON + APP
COPY --from=builder /python /python
COPY --from=builder /app /app

WORKDIR /app

# 🔥 garante que usa o python do uv
ENV PATH="/app/.venv/bin:/python/cpython-3.14.2-linux-x86_64-gnu/bin:$PATH"

# 🔥 agora funciona
RUN python -m playwright install --with-deps

USER python

CMD ["python", "main.py"]