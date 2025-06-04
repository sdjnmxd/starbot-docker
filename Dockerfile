FROM python:3.9-slim

# 镜像元数据
LABEL maintainer="sdjnmxd <sdjnmxd@users.noreply.github.com>"
LABEL org.opencontainers.image.title="StarBot Docker"
LABEL org.opencontainers.image.description="StarBot 的 Docker 容器化部署版本 - B站动态推送机器人"
LABEL org.opencontainers.image.version="latest"
LABEL org.opencontainers.image.authors="sdjnmxd"
LABEL org.opencontainers.image.url="https://github.com/sdjnmxd/starbot-docker"
LABEL org.opencontainers.image.source="https://github.com/sdjnmxd/starbot-docker"
LABEL org.opencontainers.image.documentation="https://github.com/sdjnmxd/starbot-docker#readme"
LABEL org.opencontainers.image.licenses="MIT"
LABEL org.opencontainers.image.vendor="sdjnmxd"
LABEL org.opencontainers.image.base.name="python:3.9-slim"

WORKDIR /app

COPY README.md LICENSE ./

RUN apt-get update && apt-get install -y \
    build-essential \
    libfreetype6-dev \
    libfontconfig1-dev \
    fonts-dejavu-core \
    fontconfig \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1
ENV PYTHONFAULTHANDLER=1
ENV PYTHONHASHSEED=random

CMD ["python", "main.py"]