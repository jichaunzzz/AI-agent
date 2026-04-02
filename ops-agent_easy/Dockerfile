# 使用官方 Python 镜像作为基础镜像
FROM python:3.12-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录的内容到容器内
COPY . /app

# 安装构建工具 setuptools 和 wheel
RUN pip install --no-cache-dir setuptools wheel

RUN apt-get update && apt-get install -y procps
RUN apt-get update && apt-get install -y procps
RUN apt-get update && apt-get install -y iputils-ping

# 安装 requirements.txt 中的依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露端口 8501
EXPOSE 8501

# 启动 Streamlit 应用
CMD ["streamlit", "run", "ui.py"]