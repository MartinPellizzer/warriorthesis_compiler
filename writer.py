from urllib.request import urlopen
from bs4 import BeautifulSoup
from googlesearch import search

def scrape_headers(query):
    urls = [url for url in search(query, tld="co.in", num=10, stop=10, pause=2)]

    for url in urls:
        try: html = urlopen(url)
        except: continue
        soup = BeautifulSoup(html, "html.parser")
        titles = soup.find_all(['h1', 'h2','h3','h4','h5','h6'])

        for title in titles:
            s = ''
            for content in title.contents:
                soup = BeautifulSoup(str(content), "html.parser")
                s += str(soup.text.strip())
            print(title.name + ' ' + s.strip())

        print('\n\n\n')


def convert_md_to_html():
    with open('article-wip/draft/content.md') as f: lines = f.readlines()
    with open('article-wip/keyword.txt') as f: keyword = f.read()

    html = ''
    is_ul = False
    i = 1
    added_toc = False
    k = 1
    for line in lines:
        line = line.strip()
        if not line: pass
        elif line.startswith('### '):
            line = line.replace('### ', '')
            if is_ul:
                html += f'</ul>'
                is_ul = False
            html += f'<h3 id="{k}">{i}. {line}</h3>'
            i += 1
            k += 1
        elif line.startswith('## '):
            if not added_toc:
                added_toc = True
                html += '[insert-toc-here]'
            line = line.replace('## ', '')
            if is_ul:
                html += f'</ul>'
                is_ul = False
            html += f'<h2 id="{k}">{line}</h2>'
            k += 1
            if 'conclusion' not in line.lower():
                img_src = line.lower().replace(' ', '-').strip() + '.jpg'
                html += f'<img class="post-img" alt="{line}" title="{line}" src="./images/workplace-bullying-effects/{img_src}" />'
        elif line.startswith('# '):
            line = line.replace('# ', '')
            if is_ul:
                html += f'</ul>'
                is_ul = False
            html += f'<h1>{line}</h1>'
            keyword_formatted = keyword.strip().replace(' ', '-') + '.jpg'
            html += f'<img class="post-img" alt="{keyword}" title="{keyword}" src="./images/workplace-bullying-effects/{keyword_formatted}" />'
        elif line.startswith('- '):
            line = line.replace('- ', '')
            if not is_ul:
                html += f'<ul>'
                is_ul = True
            html += f'<li>{line}</li>'
        else:
            if is_ul:
                html += f'</ul>'
                is_ul = False
            html += f'<p>{line}</p>'

    toc = ''
    toc += f'<div class="toc">'
    toc += f'<p><strong>Table of Contents</strong></p>'
    toc += f'<ul>'
    new_subsection = False
    i = 1
    k = 1
    for line in lines:
        if 0: pass
        elif line.startswith('### '):
            line = line.replace('### ', '')
            if not new_subsection:
                new_subsection = True
                toc += f'<ul>'
            toc += f'<li><a href="#{i}">{k}. {line}</a></li>'
            i += 1
            k += 1
        elif line.startswith('## '):
            if new_subsection:
                new_subsection = False
                toc += f'</ul>'
            line = line.replace('## ', '')
            toc += f'<li><a href="#{i}">{line}</a></li>'
            i += 1
    toc += f'</ul>'
    toc += f'</div>'
    
    html = html.replace('[insert-toc-here]', toc)

    keyword_formatted = keyword.strip().replace(' ', '-')
    with open(f'article-wip/draft/content.html', 'w') as f: f.write(html)

    


# scrape_headers("workplace bullying effects")
convert_md_to_html()