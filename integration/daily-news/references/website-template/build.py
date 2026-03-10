#!/usr/bin/env python3
"""
Daily News Website Builder
将 Markdown 日报转换为终端风格的 HTML 网页
"""

import os
import re
import json
import shutil
from pathlib import Path
from datetime import datetime

def parse_markdown(md_content):
    """解析 Markdown 内容"""
    sections = {
        'title': '',
        'summary': [],
        'five_star': [],
        'four_star': [],
        'worth_viewing': []
    }

    lines = md_content.split('\n')
    current_section = None
    current_item = None

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # 提取日期
        if line.startswith('# Daily News'):
            match = re.search(r'(\d{4}-\d{2}-\d{2})', line)
            if match:
                sections['date'] = match.group(1)
            continue

        # 导读
        if line == '## 导读':
            current_section = 'summary'
            continue

        # 五星推荐
        if line == '## 五星推荐':
            current_section = 'five_star'
            if current_item:
                sections[current_section].append(current_item)
            current_item = None
            continue

        # 四星推荐
        if line == '## 四星推荐':
            current_section = 'four_star'
            if current_item and current_section != 'summary':
                sections[current_section].append(current_item)
            current_item = None
            continue

        # 值得一看
        if line == '## 值得一看':
            current_section = 'worth_viewing'
            if current_item and current_section != 'summary':
                sections[current_section].append(current_item)
            current_item = None
            continue

        # 解析内容
        if current_section == 'summary' and line.startswith('- **'):
            # 导读条目
            match = re.match(r'- \*\*(.+?)\*\*：(.+)', line)
            if match:
                sections['summary'].append({
                    'topic': match.group(1),
                    'content': match.group(2)
                })

        elif current_section in ['five_star', 'four_star', 'worth_viewing']:
            # 文章条目
            if line.startswith('**['):
                # 新条目开始
                if current_item:
                    sections[current_section].append(current_item)
                current_item = {'title': '', 'url': '', 'summary': '', 'meta': ''}

                # 提取标题和URL
                match = re.match(r'\*\*\[(.+?)\]\((.+?)\)\*\*', line)
                if match:
                    current_item['title'] = match.group(1)
                    current_item['url'] = match.group(2)

            elif line.startswith('`') and '·' in line:
                # 元数据行
                current_item['meta'] = line.strip('`')

            elif line and not line.startswith('---') and not line.startswith('*Generated'):
                # 摘要内容
                if current_item['summary']:
                    current_item['summary'] += ' ' + line
                else:
                    current_item['summary'] = line

    # 添加最后一个条目
    if current_item and current_section in ['five_star', 'four_star', 'worth_viewing']:
        sections[current_section].append(current_item)

    return sections

def generate_html(data, all_dates):
    """生成 HTML 页面"""

    # 星级图标
    star_icons = {
        5: '★★★★★',
        4: '★★★★☆',
        3: '★★★☆☆'
    }

    # 生成日期导航
    date_nav = ''
    for d in sorted(all_dates, reverse=True):
        active = 'active' if d == data.get('date') else ''
        date_nav += f'<a href="{d}.html" class="date-link {active}">{d}</a>'

    # 生成导读
    summary_html = ''
    for item in data.get('summary', []):
        summary_html += f'''
        <div class="summary-item">
            <span class="summary-topic">{item['topic']}</span>
            <span class="summary-content">{item['content']}</span>
        </div>
        '''

    # 生成文章列表
    def generate_articles(articles, stars):
        html = ''
        for article in articles:
            if not article.get('title'):
                continue
            html += f'''
            <article class="news-item">
                <div class="news-header">
                    <a href="{article.get('url', '#')}" class="news-title" target="_blank" rel="noopener">{article.get('title', 'Untitled')}</a>
                    <span class="news-meta">{article.get('meta', '')}</span>
                </div>
                <p class="news-summary">{article.get('summary', '')}</p>
            </article>
            '''
        return html

    five_star_html = generate_articles(data.get('five_star', []), 5)
    four_star_html = generate_articles(data.get('four_star', []), 4)
    worth_html = generate_articles(data.get('worth_viewing', []), 3)

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Daily News - {data.get('date', '')}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-primary: #fafafa;
            --bg-secondary: #f5f5f5;
            --bg-terminal: #1a1a1a;
            --text-primary: #1a1a1a;
            --text-secondary: #666666;
            --text-muted: #999999;
            --accent: #2563eb;
            --accent-light: #3b82f6;
            --border: #e5e5e5;
            --border-light: #f0f0f0;
            --star: #f59e0b;
            --code-bg: #f4f4f4;
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            line-height: 1.6;
        }}

        /* Terminal Header */
        .terminal-header {{
            background: var(--bg-terminal);
            color: #fff;
            padding: 1rem 2rem;
            font-family: 'JetBrains Mono', monospace;
        }}

        .terminal-line {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin-bottom: 0.25rem;
        }}

        .terminal-prompt {{
            color: #10b981;
        }}

        .terminal-cursor {{
            display: inline-block;
            width: 8px;
            height: 1.2em;
            background: #10b981;
            animation: blink 1s infinite;
            vertical-align: text-bottom;
        }}

        @keyframes blink {{
            0%, 50% {{ opacity: 1; }}
            51%, 100% {{ opacity: 0; }}
        }}

        /* Navigation */
        .nav-container {{
            background: var(--bg-secondary);
            border-bottom: 1px solid var(--border);
            padding: 1rem 2rem;
            overflow-x: auto;
        }}

        .date-nav {{
            display: flex;
            gap: 0.5rem;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.875rem;
        }}

        .date-link {{
            padding: 0.5rem 1rem;
            color: var(--text-secondary);
            text-decoration: none;
            border-radius: 4px;
            transition: all 0.2s;
            white-space: nowrap;
        }}

        .date-link:hover {{
            background: var(--bg-primary);
            color: var(--accent);
        }}

        .date-link.active {{
            background: var(--accent);
            color: white;
        }}

        /* Main Content */
        .container {{
            max-width: 900px;
            margin: 0 auto;
            padding: 3rem 2rem;
        }}

        .page-title {{
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            font-family: 'JetBrains Mono', monospace;
        }}

        .page-subtitle {{
            color: var(--text-muted);
            font-family: 'JetBrains Mono', monospace;
            margin-bottom: 3rem;
        }}

        /* Summary Section */
        .summary-section {{
            background: var(--bg-secondary);
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 3rem;
        }}

        .section-title {{
            font-size: 0.875rem;
            font-weight: 600;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 1rem;
            font-family: 'JetBrains Mono', monospace;
        }}

        .summary-item {{
            padding: 0.75rem 0;
            border-bottom: 1px solid var(--border);
        }}

        .summary-item:last-child {{
            border-bottom: none;
        }}

        .summary-topic {{
            font-weight: 600;
            color: var(--accent);
            margin-right: 0.5rem;
        }}

        .summary-content {{
            color: var(--text-secondary);
        }}

        /* News Sections */
        .news-section {{
            margin-bottom: 3rem;
        }}

        .section-header {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
            margin-bottom: 1.5rem;
            padding-bottom: 0.75rem;
            border-bottom: 2px solid var(--border);
        }}

        .section-name {{
            font-size: 1.25rem;
            font-weight: 600;
        }}

        .star-rating {{
            color: var(--star);
            font-size: 0.875rem;
        }}

        .news-item {{
            padding: 1.5rem;
            margin-bottom: 1rem;
            background: white;
            border: 1px solid var(--border-light);
            border-radius: 8px;
            transition: all 0.2s;
        }}

        .news-item:hover {{
            border-color: var(--accent);
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.08);
        }}

        .news-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 1rem;
            margin-bottom: 0.75rem;
        }}

        .news-title {{
            font-size: 1.125rem;
            font-weight: 600;
            color: var(--text-primary);
            text-decoration: none;
            line-height: 1.4;
        }}

        .news-title:hover {{
            color: var(--accent);
        }}

        .news-meta {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.75rem;
            color: var(--text-muted);
            background: var(--code-bg);
            padding: 0.25rem 0.5rem;
            border-radius: 4px;
            white-space: nowrap;
        }}

        .news-summary {{
            color: var(--text-secondary);
            line-height: 1.7;
        }}

        /* Footer */
        .footer {{
            margin-top: 4rem;
            padding-top: 2rem;
            border-top: 1px solid var(--border);
            text-align: center;
            color: var(--text-muted);
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.875rem;
        }}

        /* Responsive */
        @media (max-width: 768px) {{
            .container {{
                padding: 1.5rem;
            }}

            .page-title {{
                font-size: 1.75rem;
            }}

            .news-header {{
                flex-direction: column;
                gap: 0.5rem;
            }}

            .nav-container {{
                padding: 0.75rem 1rem;
            }}
        }}
    </style>
</head>
<body>
    <header class="terminal-header">
        <div class="terminal-line">
            <span class="terminal-prompt">$</span>
            <span>daily-news --date {data.get('date', '')}</span>
            <span class="terminal-cursor"></span>
        </div>
        <div class="terminal-line">
            <span class="terminal-prompt">&gt;</span>
            <span>Generating report... Done.</span>
        </div>
    </header>

    <nav class="nav-container">
        <div class="date-nav">
            {date_nav}
        </div>
    </nav>

    <main class="container">
        <h1 class="page-title">Daily News</h1>
        <p class="page-subtitle">// {data.get('date', '')}</p>

        <section class="summary-section">
            <div class="section-title">$ cat summary.md</div>
            {summary_html if summary_html else '<p class="text-muted">暂无导读</p>'}
        </section>

        {f'''
        <section class="news-section">
            <div class="section-header">
                <span class="section-name">五星推荐</span>
                <span class="star-rating">{star_icons[5]}</span>
            </div>
            {five_star_html}
        </section>
        ''' if five_star_html else ''}

        {f'''
        <section class="news-section">
            <div class="section-header">
                <span class="section-name">四星推荐</span>
                <span class="star-rating">{star_icons[4]}</span>
            </div>
            {four_star_html}
        </section>
        ''' if four_star_html else ''}

        {f'''
        <section class="news-section">
            <div class="section-header">
                <span class="section-name">值得一看</span>
                <span class="star-rating">{star_icons[3]}</span>
            </div>
            {worth_html}
        </section>
        ''' if worth_html else ''}

        <footer class="footer">
            <p>Generated by Daily News Skill | Cloudflare Pages</p>
        </footer>
    </main>
</body>
</html>'''

    return html

def build():
    """构建网站"""
    workspace = Path.home() / 'Documents/1-Projects/每日资讯日报'
    output_dir = workspace / 'output'
    dist_dir = workspace / 'website/dist'

    # 清理并重建 dist
    if dist_dir.exists():
        shutil.rmtree(dist_dir)
    dist_dir.mkdir(parents=True)

    # 获取所有日期
    all_dates = []
    for md_file in sorted(output_dir.glob('*.md')):
        date = md_file.stem
        all_dates.append(date)

    print(f"找到 {len(all_dates)} 个日报文件")

    # 生成每个页面的 HTML
    for md_file in output_dir.glob('*.md'):
        date = md_file.stem
        md_content = md_file.read_text(encoding='utf-8')
        data = parse_markdown(md_content)
        data['date'] = date

        html = generate_html(data, all_dates)

        output_file = dist_dir / f'{date}.html'
        output_file.write_text(html, encoding='utf-8')
        print(f"生成: {output_file.name}")

    # 复制最新的作为 index.html
    if all_dates:
        latest = max(all_dates)
        shutil.copy(dist_dir / f'{latest}.html', dist_dir / 'index.html')
        print(f"首页: {latest}.html -> index.html")

    print(f"\n构建完成！输出目录: {dist_dir}")

if __name__ == '__main__':
    build()
