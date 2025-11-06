import re
import requests
import xml.etree.ElementTree as ET

# --- 配置 ---
BLOG_FEED_URL = "https://dev-insight.cloud/index.xml"
POST_NUM = 5 # 你想显示的博客文章数量
README_PATH = "README.md"

def fetch_blog_posts():
    """从 XML feed 获取最新的博客文章"""
    try:
        # 添加 User-Agent 模拟浏览器访问
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }
        # 显式禁用代理，以防环境中有代理设置导致连接失败
        proxies = {
            "http": None,
            "https": None,
        }
        response = requests.get(BLOG_FEED_URL, headers=headers, timeout=15, proxies=proxies)
        response.raise_for_status()
        
        root = ET.fromstring(response.content)
        posts = []
        
        # RSS feed 的 item 元素通常在 channel 下
        for item in root.findall('./channel/item'):
            title = item.find('title').text
            link = item.find('link').text
            posts.append({'title': title, 'link': link})
            
        return posts[:POST_NUM]
        
    except requests.RequestException as e:
        print(f"请求博客 Feed 失败: {e}")
    except ET.ParseError as e:
        print(f"解析 XML 时发生错误: {e}")
    except Exception as e:
        print(f"处理博客文章时发生未知错误: {e}")
    return []

def format_posts_md(posts):
    """将文章列表格式化为 Markdown"""
    if not posts:
        return "暂无最新文章。"
        
    lines = []
    for post in posts:
        lines.append(f"*   [{post['title']}]({post['link']})")
            
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