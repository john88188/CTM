import os
from dotenv import load_dotenv
from openai import OpenAI
from markitdown import MarkItDown

# 加载 .env 文件
load_dotenv()

# 获取 OpenAI API 密钥
openai_api_key = os.getenv("OPENAI_API_KEY")

# 检查是否成功获取密钥
if openai_api_key is None:
    raise ValueError("没有找到 OpenAI API 密钥，请确保在 .env 文件中设置了 OPENAI_API_KEY")

# 创建 OpenAI 客户端
client = OpenAI(api_key=openai_api_key)

# 创建 MarkItDown 实例，使用 OpenAI 客户端
md = MarkItDown(mlm_client=client, mlm_model="gpt-4o")

def convert_to_markdown(file_path):
    """将文件转换为 Markdown 格式"""
    try:
        result = md.convert(file_path)
        return result.text_content
    except Exception as e:
        return f"转换失败: {str(e)}"

def handle_image_with_llm(file_path):
    """使用 LLM 处理图片"""
    try:
        result = md.convert(file_path)
        return result.text_content
    except Exception as e:
        return f"图像描述失败: {str(e)}"

def save_markdown(content, output_dir, original_file):
    """将转换后的内容保存为 Markdown 文件"""
    os.makedirs(output_dir, exist_ok=True)  # 如果目录不存在，则创建
    file_name = os.path.splitext(original_file)[0] + ".md"  # 保留原文件名，改为 .md
    output_path = os.path.join(output_dir, file_name)
    
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f"转换后的文件已保存为: {output_path}")
    return output_path

def main():
    # 用户输入文件路径
    file_path = input("请输入文件路径（支持 PDF、Word、Excel、图片等格式）：").strip()
    
    output_dir = "converted_files"  # 子文件夹名称，可以修改为其他名称

    if file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
        # 如果是图片，使用 LLM 处理
        print("正在使用 LLM 处理图片...")
        result = handle_image_with_llm(file_path)
    else:
        # 否则，直接转换为 Markdown
        print("正在转换文件为 Markdown...")
        result = convert_to_markdown(file_path)

    # 将转换后的内容保存为 Markdown 文件
    save_markdown(result, output_dir, os.path.basename(file_path))

if __name__ == "__main__":
    main()
