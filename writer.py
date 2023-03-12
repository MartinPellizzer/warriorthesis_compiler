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

    html = ''
    is_ul = False
    i = 1
    for line in lines:
        line = line.strip()
        if not line: pass
        elif line.startswith('### '):
            line = line.replace('### ', '')
            if is_ul:
                html += f'</ul>'
                is_ul = False
            html += f'<h3>{i}. {line}</h3>'
            i += 1
        elif line.startswith('## '):
            line = line.replace('## ', '')
            if is_ul:
                html += f'</ul>'
                is_ul = False
            html += f'<h2>{line}</h2>'
            img_src = line.lower().replace(' ', '-').strip() + '.jpg'
            html += f'<img class="post-img" alt="{line}" title="{line}" src="./images/workplace-bullying-effects/{img_src}" />'
        elif line.startswith('- '):
            line = line.replace('- ', '')
            if not is_ul:
                html += f'<ul>'
                is_ul = True
            html += f'<li>{line}</li>'
        elif line.startswith('# '):
            line = line.replace('# ', '')
            if is_ul:
                html += f'</ul>'
                is_ul = False
            html += f'<h1>{line}</h1>'
        else:
            html += f'<p>{line}</p>'

    with open('article-wip/draft/content.html', 'w') as f: f.write(html)

        


# scrape_headers("workplace bullying effects")
convert_md_to_html()