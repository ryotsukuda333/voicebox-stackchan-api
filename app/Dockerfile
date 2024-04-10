# 基本イメージとしてPythonの公式イメージを使用
FROM python:3.8

# ffmpegをインストール
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係をインストール
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースをコピー
COPY . .

# Uvicornを使ってFastAPIアプリケーションを実行
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--reload"]
