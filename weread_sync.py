import os
import re
import json
import requests

# --- 从环境变量中获取必要信息 ---
WEREAD_COOKIE = os.environ.get("WEREAD_COOKIE")
BOOK_NUM = 3 # 你想显示的书籍数量

# --- API 和请求头 ---
# 参考 curl 命令，直接请求网页版书架
API_URL = "https://weread.qq.com/web/shelf"
HEADERS = {
    "Host": "weread.qq.com",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": WEREAD_COOKIE,
}

def get_reading_books():
    """获取正在阅读的书籍列表"""
    if not WEREAD_COOKIE:
        print("错误：WEREAD_COOKIE 未设置")
        return []

    try:
        # 使用 GET 请求获取书架 HTML 页面
        response = requests.get(API_URL, headers=HEADERS, timeout=10)
        response.raise_for_status()
        html_content = response.text

        # 使用正则表达式从 HTML 中提取 window.__INITIAL_STATE__
        match = re.search(r'window\.__INITIAL_STATE__\s*=\s*({.*?});', html_content)
        if not match:
            print("错误：无法在 HTML 中找到 __INITIAL_STATE__")
            return []

        # 将提取的字符串解析为 JSON
        data = json.loads(match.group(1))
        
        # 从 JSON 数据中获取书籍列表
        books = data.get("shelf", {}).get("books", [])
        
        # 筛选正在读的书（进度 < 100%）并按进度降序排序
        reading_books = [b for b in books if b.get("readingProgress", 1.0) < 1.0]
        reading_books.sort(key=lambda x: x.get("readingProgress", 0), reverse=True)
        
        return reading_books[:BOOK_NUM]
    except requests.RequestException as e:
        print(f"请求 API 失败: {e}")
    except Exception as e:
        print(f"处理数据时发生错误: {e}")
    return []

def format_books_md(books):
    """将书籍列表格式化为 Markdown"""
    if not books:
        return "暂无在读书籍。"
        
    lines = []
    for book in books:
        title = book.get("title")
        author = book.get("author")
        book_id = book.get("bookId")
        # 将 0-1 的浮点数进度转换为百分比
        progress = int(book.get("readingProgress", 0) * 100)
        
        if title and book_id:
            book_url = f"https://weread.qq.com/web/reader/{book_id}"
            lines.append(f"*   [{title}]({book_url}) - {author} (进度：{progress}%)")
            
    return "\n".join(lines)

def update_readme(content):
    """更新 README.md 文件"""
    readme_path = "README.md"
    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            readme_content = f.read()
        
        # 使用正则表达式替换注释之间的内容
        new_readme = re.sub(
            r"<!--weread start-->[\s\S]*?<!--weread end-->",
            f"<!--weread start-->\n{content}\n<!--weread end-->",
            readme_content
        )
        
        if new_readme != readme_content:
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(new_readme)
            print("README.md 更新成功！")
        else:
            print("内容无变化，无需更新。")
            
    except FileNotFoundError:
        print(f"错误: {readme_path} 未找到。")
    except Exception as e:
        print(f"更新 README 时发生错误: {e}")

if __name__ == "__main__":
    reading_books = get_reading_books()
    markdown_content = format_books_md(reading_books)
    print("--- 生成的 Markdown 内容 ---")
    print(markdown_content)
    print("--------------------------")
    update_readme(markdown_content)