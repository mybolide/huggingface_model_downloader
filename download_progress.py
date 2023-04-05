import os
import sys
import requests
import json
from bs4 import BeautifulSoup
from tqdm import tqdm


def download_file(url, output_path, proxies=None):
    headers = {}
    if os.path.exists(output_path):
        file_size = os.path.getsize(output_path)
        if file_size > 0:
            headers["Range"] = f"bytes={file_size}-"

    response = requests.get(url, stream=True, headers=headers, proxies=proxies)
    total_size = int(response.headers.get('content-length', 0))

    with open(output_path, "ab") as f:
        for chunk in tqdm(response.iter_content(chunk_size=1024), total=total_size // 1024, unit='KB', unit_scale=True):
            if chunk:
                f.write(chunk)

import re
from bs4 import BeautifulSoup

def download_model(model_name, proxies=None):
    base_url = f"https://huggingface.co/{model_name}/resolve/main/"
    repo_url = f"https://huggingface.co/{model_name}/tree/main"

    response = requests.get(repo_url, proxies=proxies)
    soup = BeautifulSoup(response.text, "lxml")

    files_to_download = []

    file_rows = soup.find_all("a", href=True)
    for file_row in file_rows:
        match = re.search(rf"/{model_name}/blob/main/(.*)", file_row["href"])
        if match:
            file_name = match.group(1)
            files_to_download.append(file_name)

    print("文件列表:", files_to_download)  # 打印文件列表

    os.makedirs("models", exist_ok=True)

    for file in files_to_download:
        url = f"{base_url}{file}"
        output_path = os.path.join("models", file)

        print(f"开始下载 {file}")
        download_file(url, output_path)
        print(f"{file} 已成功下载！")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法：python download_progress.py <model_name>")
        sys.exit(1)

    model_name = sys.argv[1]
    proxies = {"http": "http://127.0.0.1:7890", "https": "http://127.0.0.1:7890"}
    download_model(model_name,proxies=proxies)
