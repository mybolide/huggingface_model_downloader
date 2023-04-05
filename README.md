# Hugging Face 模型下载器

用于从 Hugging Face 批量下载预训练模型的 Python 脚本。

## 使用方法

1. 克隆此仓库：
   git clone https://github.com/yourusername/huggingface_model_downloader.git
2. 进入项目目录：
   cd huggingface_model_downloader
3. 安装依赖：
   pip install -r requirements.txt
4. 下载模型：
   python huggingface_model_downloader.py <model_name>

其中，`<model_name>` 是模型的名称，例如 `THUDM/chatglm-6b`。

下载的模型文件将被保存到 `models/` 目录下。

## 代理设置

要使用代理，请在 `huggingface_model_downloader.py` 文件中找到以下行：

```python
proxies = {"http": "http://127.0.0.1:7890", "https": "http://127.0.0.1:7890"}
```

## 要求

Python 3.6+  
requests  
beautifulsoup4  
tqdm
