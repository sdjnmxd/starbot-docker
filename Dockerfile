FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制README和LICENSE文件
COPY README.md LICENSE ./

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    build-essential \
    procps \
    redis-tools \
    bc \
    libfreetype6-dev \
    libfontconfig1-dev \
    fonts-dejavu-core \
    fontconfig \
    && rm -rf /var/lib/apt/lists/*

# 复制项目文件
COPY requirements.txt .
COPY healthcheck.sh /healthcheck.sh

# 设置健康检查脚本权限
RUN chmod +x /healthcheck.sh

# 安装Python依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目代码
COPY . .

# 设置环境变量
ENV PYTHONUNBUFFERED=1
ENV PYTHONFAULTHANDLER=1
ENV PYTHONHASHSEED=random

# 健康检查
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD /healthcheck.sh

# 启动命令
CMD ["python", "main.py"] 