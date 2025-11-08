# 👋 Hi

### 💼 About Me
你好，我是Jasonhonghh，正在学习和探索各种编程技术和工具，目标是成为一名全栈开发工程师。

### 💻 Code Activities
[![Contributions Badge](https://badges.strrl.dev/contributions/all/Jasonhonghh?style=flat-square)](https://github.com/Jasonhonghh)
[![Contributions Badge](https://badges.strrl.dev/contributions/weekly/Jasonhonghh?style=flat-square)](https://github.com/Jasonhonghh)
[![Commits Badge](https://badges.strrl.dev/commits/weekly/Jasonhonghh?style=flat-square)](https://github.com/Jasonhonghh)
[![Issues and PRs Badge](https://badges.strrl.dev/issues-and-prs/weekly/Jasonhonghh?style=flat-square)](https://github.com/Jasonhonghh)

### 📖 Posts
<!--blog start-->
*   [周记#1：衰退时代生存指南与初步实践](https://dev-insight.cloud/diary/diary1/)：<h2 id="写在前面">写在前面</h2>
<p>这是我的第一篇互联网周记，希望能够成为一个表达的窗口，和一个向内探索的契机。</p>
<h2 id="本周概览">本周概览</h2>
<ul>
<li>阅读《以日为鉴：衰退时代生存指南》</li>
<li>通过cloudflare缓存和国内字体cdn加速博客加载速度</li>
<li>第一次使用github action，自动更新github主页</li>
<li>基于nextjs和shadcn构建了一个go-chat-web聊天室前端</li>
<li>学习在telegram上搜集信息和资料</li>
<li>签署秋招卖身契，启动进军大厂计划</li>
</ul>
<h2 id="以日为鉴衰退时代生存指南">以日为鉴：衰退时代生存指南</h2>
<p>这本书的全称是<a href="https://book.douban.com/subject/37467536/">以日为鉴：衰退时代生存指南</a>，书名是《以日为鉴》，不过或许“衰退时代生存指南”才是作者想要传达的内容。</p>
<p>作者分析了最近几十年日本的经济寒冬与社会问题，也描述了日本政府的应对措施，在牺牲了几代人与科技创新的情况下，维持了社会的稳定和秩序。如今面临经济转型和产业升级的我们，或许可以从中汲取一些经验和教训。</p>
<p>读完整本书有几个感受：</p>
<ul>
<li>时代的一粒沙，到个人头上便是一座山：很多时候并非我们不够努力，而是经济周期和社会环境的变化，缩小了所谓的“努力”与“成功”之间的距离。</li>
<li>“苟着”也是一种生存智慧：在大环境不佳的情况下，保持稳定的生活和心态，静观事物的变化，一点一滴的成长，等待机会的到来。</li>
<li>“出海”或许是未来的方向：在全球化的今天，国内市场的局限性越来越明显，寻找海外市场和机会，或许能够带来新的增长点和突破口，更重要的是可以在避开内卷与经济寒冬的同时，为国内市场提供支持。</li>
</ul>
<h2 id="博客加速与优化">博客加速与优化</h2>
<p>这个博客基于<a href="https://developers.cloudflare.com/pages/framework-guides/deploy-a-hugo-site/">cloudflare-hugo</a>的方法搭建，国内IP也能访问。我重构了原本主题的字体和详情页的一些内容，博客字体采用了霞鹜文楷字体的cdn加速。但是存在两个问题：</p>
<ul>
<li>cloudflare pages解析加上加载网页的速度太慢了，大概需要5-10秒。</li>
<li>无论是使用这个<a href="https://github.com/lxgw/LxgwWenKai/issues/24">仓库issue</a>中提到的免费cdn，还是直接从cloudflare直接获取字体文件，加载字体的速度都很慢，当时采用的字体文件有10MB左右。</li>
</ul>
<p>为了解决这个问题，我做了以下优化：</p>
<ul>
<li>启用cloudflare的域缓存功能，将静态资源缓存到cloudflare的边缘节点，提升访问速度。</li>
<li>换用国内的字体cdn服务，同时更换为更小的字体文件，只包含常用字符集，减小字体文件大小。</li>
</ul>
<p>在hugo主题的theme文件夹下的<code>layouts/partials/extend_head.html</code>文件中，添加如下代码：</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-html" data-lang="html"><span class="line"><span class="cl"><span class="p">&lt;</span><span class="nt">link</span> <span class="na">rel</span><span class="o">=</span><span class="s">&#34;stylesheet&#34;</span> <span class="na">href</span><span class="o">=</span><span class="s">&#34;https://s4.zstatic.net/ajax/libs/lxgw-wenkai-screen-webfont/1.7.0/style.min.css&#34;</span> <span class="p">/&gt;</span>
</span></span><span class="line"><span class="cl"><span class="p">&lt;</span><span class="nt">link</span> <span class="na">rel</span><span class="o">=</span><span class="s">&#34;stylesheet&#34;</span> <span class="na">href</span><span class="o">=</span><span class="s">&#34;https://s4.zstatic.net/ajax/libs/lxgw-wenkai-webfont/1.7.0/style.min.css&#34;</span> <span class="p">/&gt;</span>
</span></span><span class="line"><span class="cl"><span class="p">&lt;</span><span class="nt">style</span><span class="p">&gt;</span>
</span></span><span class="line"><span class="cl">  <span class="c">/* 2. 使用 @font-face 定义字体 */</span>
</span></span><span class="line"><span class="cl">  <span class="p">@</span><span class="k">font-face</span> <span class="p">{</span>
</span></span><span class="line"><span class="cl">    <span class="nt">font-family</span><span class="o">:</span> <span class="s1">&#39;LXGW WenKai Screen&#39;</span><span class="o">;</span> <span class="c">/* 定义一个字体名称 */</span>
</span></span><span class="line"><span class="cl">    <span class="nt">src</span><span class="o">:</span> <span class="nt">url</span><span class="o">(</span><span class="s1">&#39;https://cdn.staticfile.net/lxgw-wenkai-screen-webfont/1.7.0/files/lxgwwenkaigbscreen-subset-97.woff2&#39;</span><span class="o">)</span> <span class="nt">format</span><span class="o">(</span><span class="s1">&#39;woff2&#39;</span><span class="o">);</span>
</span></span><span class="line"><span class="cl">    <span class="nt">font-weight</span><span class="o">:</span> <span class="nt">normal</span><span class="o">;</span>
</span></span><span class="line"><span class="cl">    <span class="nt">font-style</span><span class="o">:</span> <span class="nt">normal</span><span class="o">;</span>
</span></span><span class="line"><span class="cl">    <span class="nt">font-display</span><span class="o">:</span> <span class="nt">swap</span><span class="o">;</span> <span class="c">/* 确保文本始终可见 */</span>
</span></span><span class="line"><span class="cl">  <span class="p">}</span>
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl">  <span class="c">/* 3. 在 body 中应用这个字体，并设置一个通用备用字体 */</span>
</span></span><span class="line"><span class="cl">  <span class="nt">body</span> <span class="p">{</span>
</span></span><span class="line"><span class="cl">      <span class="c">/* 原版 */</span>
</span></span><span class="line"><span class="cl">      <span class="k">font-family</span><span class="p">:</span> <span class="s2">&#34;LXGW WenKai&#34;</span><span class="p">,</span> <span class="kc">sans-serif</span><span class="p">;</span>
</span></span><span class="line"><span class="cl">      <span class="c">/* 屏幕优化版 */</span>
</span></span><span class="line"><span class="cl">      <span class="k">font-family</span><span class="p">:</span> <span class="s2">&#34;LXGW WenKai Screen&#34;</span><span class="p">,</span> <span class="kc">sans-serif</span><span class="p">;</span>
</span></span><span class="line"><span class="cl">  <span class="p">}</span>
</span></span><span class="line"><span class="cl"><span class="p">&lt;/</span><span class="nt">style</span><span class="p">&gt;</span>
</span></span></code></pre></div><h2 id="github-action自动更新github主页">github action自动更新github主页</h2>
<p>Github主页是一个程序员的门面，之前我只是手动编写了一个静态的README.md文件，将我稍稍了解的技术栈和项目罗列在上面。最近意识到这个地方是表达自我的技术观点，和展示个人能力的好地方，于是决定定期更新这个页面，顺便也学习一下github action的使用，将最近的编程活动、博客和最近在读的书籍都放在了主页上，每6个小时自动触发一次更新。</p>
*   [好用的第三方库](https://dev-insight.cloud/tips/libs/)：收录一些好用的第三方库。
*   [开发的技巧](https://dev-insight.cloud/tips/blogs/)：收录一些开发技巧，包括环境搭建、工具使用、代码片段等。
<!--blog end-->

### 📚 Reading
<!--weread start-->
*   [以日为鉴：衰退时代生存指南](https://search.douban.com/book/subject_search?search_text=%E4%BB%A5%E6%97%A5%E4%B8%BA%E9%89%B4) - 分析师Boden
*   [refactoring2](https://search.douban.com/book/subject_search?search_text=refactoring2) - Unknown
*   [被讨厌的勇气：“自我启发之父”阿德勒的哲学课](https://search.douban.com/book/subject_search?search_text=%E8%A2%AB%E8%AE%A8%E5%8E%8C%E7%9A%84%E5%8B%87%E6%B0%94) - 岸见一郎 古贺史健
*   [哈利波特完整系列（全七册）](https://search.douban.com/book/subject_search?search_text=%E5%93%88%E5%88%A9%E6%B3%A2%E7%89%B9%E5%AE%8C%E6%95%B4%E7%B3%BB%E5%88%97) - [英]J.K.罗琳
*   [架构整洁之道](https://search.douban.com/book/subject_search?search_text=%E6%9E%B6%E6%9E%84%E6%95%B4%E6%B4%81%E4%B9%8B%E9%81%93) - 罗伯特 C. 马丁
<!--weread end-->