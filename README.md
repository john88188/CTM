# MarkItDown 转换工具 (CTM)

这个项目提供了一个命令行工具，可以将多种文件格式（如 PDF、Word、Excel、图片等）转换为 Markdown 格式。

主要能力由微软开源工具 [MarkItDown](https://github.com/microsoft/markitdown) 提供，我是快手党，第一时间写了这个项目方便用户使用（包括我）。

我在 X 上活跃，**SamGor 三哥** 欢迎 Follow me [https://x.com/biggor888](https://x.com/biggor888)

## 项目简介

MarkItDown 转换工具支持多种文件格式，包括：
- **文档**：PDF、Word、Excel 等
- **图片**：JPG、PNG、GIF、BMP 等

对于图片文件，程序将使用 OpenAI 的 GPT-4 模型生成图像描述，并返回 Markdown 格式的内容。对于其他文档类型，程序将提取文本内容并转换为 Markdown。

## 安装依赖

首先，确保你安装了所有依赖项。你可以通过 `requirements.txt` 安装所有必需的 Python 库：

1. 克隆或下载项目：

   ```bash
   git clone https://github.com/john88188/ctm.git
   cd ctm
   ```

2. 创建虚拟环境（推荐）：

   ```bash
   python -m venv venv
   ```

3. 激活虚拟环境：
   * 对于 Linux/macOS：

     ```bash
     source venv/bin/activate
     ```
   * 对于 Windows：

     ```bash
     venv\Scripts\activate
     ```

4. 安装依赖：

   ```bash
   pip install -r requirements.txt
   ```

## 配置 OpenAI API 密钥

1. 在 OpenAI 网站上创建一个账户并获取你的 API 密钥。
2. 在项目根目录下创建 `.env` 文件，格式如下：

   ```env
   OPENAI_API_KEY=your-api-key-here
   ```

**注意：** 确保 `.env` 文件不会被上传到 GitHub，因此要添加到 `.gitignore` 文件中。

如果你需要一个 `.env` 文件的示例，可以参考 `.env.example` 文件，复制并重命名为 `.env`，然后填写你的 API 密钥。

## 使用方法

运行以下命令启动转换工具：

```bash
python ctm.py
```

当程序提示时，输入你要转换的文件路径。支持的文件格式包括：
* **文档**：PDF、Word、Excel 等
* **图片**：JPG、PNG、GIF、BMP 等

示例：

```bash
请输入文件路径（支持 PDF、Word、Excel、图片等格式）：test.pdf
```

对于图片文件，程序将使用 OpenAI 的 GPT-4 模型进行描述，并返回 Markdown 格式的内容。例如：

```bash
请输入文件路径（支持 PDF、Word、Excel、图片等格式）：example.jpg
```

程序将通过 GPT-4 生成图片的描述，并返回相应的 Markdown 内容。

## 项目结构

```plaintext
CTM/
│
├── .env           # 存储 API 密钥，GitHub 上不可公开
├── .env.example   # 示例文件，GitHub 上公开
├── .gitignore     # 忽略 .env 文件
├── ctm.py  # 主转换脚本
├── requirements.txt        # 项目依赖
└── README.md      # 使用说明
```

* `.env`：存储 OpenAI API 密钥，确保它不被上传到 GitHub 上。
* `.env.example`：示例文件，供用户参考，上传到 GitHub 上。
* `.gitignore`：确保 `.env` 文件被忽略，避免敏感信息泄露。

## 贡献

欢迎提交 Pull Request 和 Bug 修复。如果你有任何问题或建议，欢迎通过 GitHub Issues 提交。

## License

MIT License

### 说明：
1. **安装依赖**：提供了详细的步骤，确保用户能够顺利安装所有必需的库和工具，推荐使用虚拟环境。
2. **配置 OpenAI API 密钥**：详细说明了如何从 OpenAI 获取 API 密钥，并设置 .env 文件。提供了 .env.example 作为示例，帮助用户轻松配置。
3. **使用方法**：详细说明了如何运行工具，转换不同类型的文件（文档和图片）。同时，对于图片，程序将通过 GPT-4 模型生成描述，便于用户理解转换后的内容。
4. **项目结构**：列出了项目的主要文件及其功能，帮助用户快速理解项目的目录结构。