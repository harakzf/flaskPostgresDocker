# Baseイメージ
FROM python:3

WORKDIR /usr/local/src/work

# Flaskのインストール
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org flask

# psycopg2(PostgreSQLクライアント)のインストール
RUN pip install psycopg2