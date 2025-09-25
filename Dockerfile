#Dockerfile的作用
# 基础镜像
FROM python:3.12-slim

#设置工作空间
WORKDIR /app

#设置环境变量，防止pyc缓存、编码问题
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#拷贝代码内容
COPY . .

#启动命令（开发时使用runserver，后续使用gunicorn）
CMD ["python","manage.py","runserver","0.0.0.0:8000"]