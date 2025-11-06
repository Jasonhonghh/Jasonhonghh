import re
import cloudscraper # 导入 cloudscraper
import xml.etree.ElementTree as ET

# --- 配置 ---
BLOG_FEED_URL = "https://dev-insight.cloud/index.xml"
POST_NUM = 5 # 你想显示的博客文章数量
README_PATH = "README.md"

def fetch_blog_posts():
    """从 XML feed 获取最新的博客文章"""
    try:
        # 创建一个 cloudscraper 实例
        scraper = cloudscraper.create_scraper()
        
        # 使用 scraper 发送请求，它会自动处理 Cloudflare 质询
        response = scraper.get(BLOG_FEED_URL, timeout=15)
        response.raise_for_status()
        
        root = ET.fromstring(response.content)
        posts = []
        
        # RSS feed 的 item 元素通常在 channel 下
        for item in root.findall('./channel/item'):
            title = item.find('title').text
            
            # 2. 去除 title 为 "About" 的博客
            if title and title.strip().lower() == 'about':
                continue

            link = item.find('link').text
            # 1. 获取 description
            description_element = item.find('description')
            description = description_element.text if description_element is not None else ""
            
            posts.append({'title': title, 'link': link, 'description': description.strip()})
            
        return posts[:POST_NUM]
        
    except Exception as e:
        # cloudscraper 可能会抛出自己的异常，但用通用的 Exception 也能捕获
        print(f"请求或处理博客 Feed 时发生错误: {e}")
    return []

def format_posts_md(posts):
    """将文章列表格式化为 Markdown"""
    if not posts:
        return "暂无最新文章。"
        
    lines = []
    for post in posts:
        title = post.get('title')
        link = post.get('link')
        description = post.get('description')

        # 1. 将 description 以括号的形式添加进来
        if description:
            lines.append(f"*   [{title}]({link})：{description}")
        else:
            lines.append(f"*   [{title}]({link})")
            
    return "\n".join(lines)

def update_readme(content):
    """更新 README.md 文件中的博客部分"""
    try:
        with open(README_PATH, "r", encoding="utf-8") as f:
            readme_content = f.read()
        
        # 使用正则表达式替换 <!--blog start--> 和 <!--blog end--> 之间的内容
        new_readme = re.sub(
            r"<!--blog start-->[\s\S]*?<!--blog end-->",
            f"<!--blog start-->\n{content}\n<!--blog end-->",
            readme_content
        )
        
        if new_readme != readme_content:
            with open(README_PATH, "w", encoding="utf-8") as f:
                f.write(new_readme)
            print("博客列表更新成功！")
        else:
            print("博客列表内容无变化，无需更新。")
            
    except FileNotFoundError:
        print(f"错误: {README_PATH} 未找到。")
    except Exception as e:
        print(f"更新 README 时发生错误: {e}")

if __name__ == "__main__":
    latest_posts = fetch_blog_posts()
    markdown_content = format_posts_md(latest_posts)
    print("--- 生成的博客 Markdown 内容 ---")
    print(markdown_content)
    print("-----------------------------")
    update_readme(markdown_content)