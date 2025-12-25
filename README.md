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
*   [周记#5：](https://dev-insight.cloud/diary/diary5/)：<h2 id="本周摘要">本周摘要</h2>
<ul>
<li>Go的竞态检测</li>
<li>Hello-Agents与“今天看什么”</li>
</ul>
<h2 id="go的竞态检测">Go的竞态检测</h2>
<p>之前只觉得Go的协程机制很丝滑，后面看课的时候发现竞态检测也很给力。竞态检测是指Go官方支持竟态检测器，能够在编译/运行时发现多个goroutine并发读写同一块内存且未能正确同步的问题。</p>
<p>数据竞争发生在以下条件同时满足时：</p>
<ul>
<li>至少两个 goroutine 并发访问同一块内存</li>
<li>至少有一个是写操作</li>
<li>这些访问之间没有同步机制（如 mutex、channel、atomic）</li>
</ul>
<p>例如</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-go" data-lang="go"><span class="line"><span class="cl"><span class="kd">var</span> <span class="nx">x</span> <span class="kt">int</span>
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl"><span class="kd">func</span> <span class="nf">main</span><span class="p">()</span> <span class="p">{</span>
</span></span><span class="line"><span class="cl">    <span class="k">go</span> <span class="kd">func</span><span class="p">()</span> <span class="p">{</span>
</span></span><span class="line"><span class="cl">        <span class="nx">x</span> <span class="p">=</span> <span class="mi">1</span>
</span></span><span class="line"><span class="cl">    <span class="p">}()</span>
</span></span><span class="line"><span class="cl">    <span class="k">go</span> <span class="kd">func</span><span class="p">()</span> <span class="p">{</span>
</span></span><span class="line"><span class="cl">        <span class="nx">_</span> <span class="p">=</span> <span class="nx">x</span>
</span></span><span class="line"><span class="cl">    <span class="p">}()</span>
</span></span><span class="line"><span class="cl"><span class="p">}</span>
</span></span></code></pre></div><p>Go官方提供了竟态检测器，编译/运行/测试时都可以通过-race选项打开，发现竟态会直接报错并且打印堆栈。</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-go" data-lang="go"><span class="line"><span class="cl"><span class="k">go</span> <span class="nx">run</span> <span class="o">-</span><span class="nx">race</span> <span class="nx">main</span><span class="p">.</span><span class="k">go</span>
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl"><span class="k">go</span> <span class="nx">build</span> <span class="o">-</span><span class="nx">race</span>
</span></span><span class="line"><span class="cl"><span class="p">.</span><span class="o">/</span><span class="nx">your_program</span>
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl"><span class="k">go</span> <span class="nx">test</span> <span class="o">-</span><span class="nx">race</span> <span class="p">.</span><span class="o">/...</span>
</span></span></code></pre></div><h2 id="智能体教程hello-agents">智能体教程Hello-Agents</h2>
<p>如果让你同时去爬取arxiv、github和各个论坛平台中关于ai的信息，你会怎么做，
在看这个教程之前我的答案还是“写个爬虫”。<a href="https://datawhalechina.github.io/hello-agents/#/./README">Hello-Agents</a>是 Datawhale 社区的系统性智能体学习教程，详细描述了智能体
的构建、原理，从构建智能体讲到构建自己的Agent框架，再讲到上下文工程等高级知识和一些综合案例。刚刚读完前面两章，基础知识有些晦涩，但是基于低代码平台的智能体搭建确实惊艳到我了。</p>
<p>根据教程指引，在coze上搭建了“每日ai简报”的工作流。</p>
<p><img alt="20251221163152" loading="lazy" src="https://3ec93ca.webp.li/20251221163152.png"></p>
<p>输出的结果</p>
<p><img alt="20251221163322" loading="lazy" src="https://3ec93ca.webp.li/20251221163322.png"></p>
<p>如果是爬虫的话，写爬虫，关注反爬，适配网站，适配输出格式可能需要大半天，搭建这样一条工作流只需要五分钟不到，适配新的平台只需要去插件市场找一下插件。</p>
<p><img alt="20251221163731" loading="lazy" src="https://3ec93ca.webp.li/20251221163731.png"></p>
<p>当然，这里有点跑偏了，低代码只是智能体应用的一个小方面，慢慢学吧。</p>
<p>在coze中搭建的智能体直接作为api发布，也就是说这些复杂的计算工作流，全部在他们的服务器上进行，我们只是需要调用api，也不用在我们自己的机器上跑爬虫或者智能体，就能完成这所有的工作。</p>
<p>参考官方托管在github的<a href="https://github.com/coze-dev/coze-studio/wiki/6.-API-%E5%8F%82%E8%80%83/39a0bcd29dbe98abd14f648db1cd063265bdd86f">api教程</a>，我将这个智能体发布为api，在博客菜单栏中新建了一个“今天看什么”栏目，同时在博客的github仓库中添加workflow来定时调用这个智能体的api。（唯一的缺点是密钥有效期没法设置永久）</p>
<p>后面发现可以新建一个Oauth授权应用，通过私钥获取jwt，实现永久认证。</p>
*   [周记#4：Let's go, 拥抱 AI](https://dev-insight.cloud/diary/diary4/)：MIT 6.824、Copilot与Trae。
*   [周记#3：生图仙人与群像故事](https://dev-insight.cloud/diary/diary3/)：体验AI生图与最近在看的好剧。
*   [周记#2：请务必平静的前进](https://dev-insight.cloud/diary/diaty2/)：Copilot Plan体验和最近的感受。
*   [周记#1：衰退时代生存指南与初步实践](https://dev-insight.cloud/diary/diary1/)：第一篇周记，记录近期的读书和实践经历。
<!--blog end-->

### 📚 Reading
<!--weread start-->
*   [哈利波特完整系列（全七册）](https://search.douban.com/book/subject_search?search_text=%E5%93%88%E5%88%A9%E6%B3%A2%E7%89%B9%E5%AE%8C%E6%95%B4%E7%B3%BB%E5%88%97) - [英]J.K.罗琳
*   [人偶游戏](https://search.douban.com/book/subject_search?search_text=%E4%BA%BA%E5%81%B6%E6%B8%B8%E6%88%8F) - [日]东野圭吾
*   [架构整洁之道](https://search.douban.com/book/subject_search?search_text=%E6%9E%B6%E6%9E%84%E6%95%B4%E6%B4%81%E4%B9%8B%E9%81%93) - 罗伯特 C. 马丁
*   [当我们不再理解世界（短经典精选）](https://search.douban.com/book/subject_search?search_text=%E5%BD%93%E6%88%91%E4%BB%AC%E4%B8%8D%E5%86%8D%E7%90%86%E8%A7%A3%E4%B8%96%E7%95%8C) - 本哈明·拉巴图特
*   [以日为鉴：衰退时代生存指南](https://search.douban.com/book/subject_search?search_text=%E4%BB%A5%E6%97%A5%E4%B8%BA%E9%89%B4) - 分析师Boden
<!--weread end-->