# ベースイメージを指定
FROM python:3.9

ENV PYTHONUNBUFFERED 1
RUN mkdir /code

# ディレクトリを移動する
WORKDIR /code

# pipでrequirements.txtに記載のパッケージをインストール
COPY requirements.txt /code/
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /code/