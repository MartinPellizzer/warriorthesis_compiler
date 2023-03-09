import shutil
import os
import re


header = f'''
    <header>
        <nav class="container-xl mx-auto px-32">
            <a href="index.html">WarriorThesis</a>
            <ul>
                <li><a href="index.html">Home</a></li>
                <li><a href="free-ebook.html">FREE Ebook</a></li>
                <li><a href="about.html">About</a></li>
                <li><a href="./resources/workplace-bullying-survival-kit.pdf">WBSK</a></li>
            </ul>
        </nav>
    </header>
'''

footer = f'''
    <footer>
        <div class="container-xl mx-auto px-32">
            <p>&#169; 2023 WarriorThesis | All Rights Reserved - <a href="privacy-policy.html">Privacy Policy</a></p>
            <a href="https://twitter.com/warriorthesis" target="_blank">
                <svg xmlns="http://www.w3.org/2000/svg" class="ionicon" viewBox="0 0 512 512">
                    <title>Logo Twitter</title>
                    <path
                        d="M496 109.5a201.8 201.8 0 01-56.55 15.3 97.51 97.51 0 0043.33-53.6 197.74 197.74 0 01-62.56 23.5A99.14 99.14 0 00348.31 64c-54.42 0-98.46 43.4-98.46 96.9a93.21 93.21 0 002.54 22.1 280.7 280.7 0 01-203-101.3A95.69 95.69 0 0036 130.4c0 33.6 17.53 63.3 44 80.7A97.5 97.5 0 0135.22 199v1.2c0 47 34 86.1 79 95a100.76 100.76 0 01-25.94 3.4 94.38 94.38 0 01-18.51-1.8c12.51 38.5 48.92 66.5 92.05 67.3A199.59 199.59 0 0139.5 405.6a203 203 0 01-23.5-1.4A278.68 278.68 0 00166.74 448c181.36 0 280.44-147.7 280.44-275.8 0-4.2-.11-8.4-.31-12.5A198.48 198.48 0 00496 109.5z" />
                </svg>
            </a>
        </div>
    </footer>
'''

def generate_post(filename):
    with open(f'./private/articles-html/{filename}') as f:
        content = f.read()

    with open(f'./public/{filename}', 'w') as f:
        f.write(f'''
            <!DOCTYPE html>
            <html lang="en">

            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="style.css">
                <title>Warrior Thesis</title>
            </head>

            <body>
                {header}
                <main class="container-md mx-auto px-32">
                    {content}
                </main>
                {footer}
            </body>

            </html>
        ''')

def generate_posts():
    filenames = [f for f in os.listdir('./private/articles-html/')]

    for filename in filenames:
        generate_post(filename)

def generate_assets():
    asset_list = [asset for asset in os.listdir('./public/assets/')]

    for asset in os.listdir('./private/assets/'):
        if asset not in asset_list:
            shutil.copy2(f'./private/assets/{asset}', './public/assets/')

def generate_page_home():
    article_list = [article for article in os.listdir('./private/articles/')]

    articles_html = []
    for article in article_list:
        with open(f'./private/articles/{article}') as f:
            lines = f.readlines()
    
            title = ''
            image_name = article.split('.')[0]
            image = f'<img alt="{image_name}" title="{image_name}" src="./images/{image_name}/{image_name}.jpg" />'
            text = ''
            for line in lines:
                if 'h1' in line:
                    title = line.replace('<h1>', '<h2>').replace('</h1>', '</h2>').strip() 
                # elif 'img' in line:
                #     image = line 
                elif '<p>' in line:
                    text += line.replace('<p>', '').replace('</p>', '')

            articles_html.append([title, image, f'<p>{text[:100]}...</p>', article])

            print(title)

    hero = f'''
        <div class="hero">
            <div class="container-xl mx-auto px-32 h-full">
                <div class="flex items-center h-full">
                    <div class="flex-3">
                        <p>Attention Warrior: New Report Released (FREE for Limited Time).</p>
                        <h1>Become a workplace bullies worst nightmare! (without guilt)</h1>
                        <p>Sick of being bullied? Sick of going to bed drained? Sick of waking up strangled by
                            anxiety? Do yourself a favor and click the button below. Thank me later.</p>
                        <a href="./free-ebook.html">Download The Workplace Bullying Survival Kit</a>
                    </div>
                    <div class="flex-1"></div>
                </div>
            </div>
        </div>
    '''

    final_html = ''
    for article_html in articles_html:
        final_html += f'''
            <div class="flex">
                <div class="flex-3 flex items-center gap-32">
                    <div class="flex-1">
                        {article_html[1]}
                    </div>
                    <div class="flex-1">
                        {article_html[0]}
                        {article_html[2]}
                        <p><a href="./{article_html[3]}">read more -></a></p>
                    </div>
                </div>
                <div class="flex-1"></div>
            </div>
        '''

    with open(f'./public/index.html', 'w') as f:
        f.write(f'''
            <!DOCTYPE html>
            <html lang="en">

            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="style.css">
                <title>Warrior Thesis</title>
            </head>

            <body>
                {header}
                {hero}
                <main class="post-list container-xl mx-auto px-32 flex flex-col gap-32">
                    {final_html}
                </main>
                {footer}
            </body>

            </html>
        ''')


def generate_page_privacy_policy():
    with open(f'./private/privacy-policy.html') as f:
        content = f.read()

    with open(f'./public/privacy-policy.html', 'w') as f:
        f.write(f'''
            <!DOCTYPE html>
            <html lang="en">

            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="style.css">
                <title>Warrior Thesis</title>
            </head>

            <body>
                {header}
                <main class="container-md mx-auto px-32">
                    {content}
                </main>
                {footer}
            </body>

            </html>
        ''')


def generate_page_about():
    input_file = f'./private/pages/about.txt'
    output_file = f'./private/pages/about.html'

    convert_txt_to_html(input_file, output_file)

    with open(f'./private/pages/about.html') as f:
        content = f.read()

    with open(f'./public/about.html', 'w') as f:
        f.write(f'''
            <!DOCTYPE html>
            <html lang="en">

            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="style.css">
                <title>Warrior Thesis</title>
            </head>

            <body>
                {header}
                <main class="container-md mx-auto px-32">
                    {content}
                </main>
                {footer}
            </body>

            </html>
        ''')


def generate_homepage2():
    article_list = [article for article in os.listdir('./private/articles/')]

    articles = []
    for article in article_list:
        with open(f'./private/articles/{article}') as f:
            lines = f.readlines()
    
            title = ''
            image = ''
            text = ''
            for line in lines:
                if line.startswith('### '):
                    pass 
                elif line.startswith('## '):
                    pass 
                elif line.startswith('# '):
                    title = line.replace('# ', '<h2>')
                    title += '</h2>'
                    title = title.strip() 
                elif line.startswith('!'):
                    image = md_to_html_image(line)
                else:
                    text += line

            link = article.replace('md', 'html')
            articles.append([title, image, f'<p>{text[:100]}...</p>', link])

            print(title)

    final_html = ''
    for article_html in articles:
        final_html += f'''
            <div class="flex">
                <div class="flex-3 flex items-center gap-32">
                    <div class="flex-1">
                        {article_html[1]}
                    </div>
                    <div class="flex-1">
                        {article_html[0]}
                        {article_html[2]}
                        <p><a href="./{article_html[3]}">read more -></a></p>
                    </div>
                </div>
                <div class="flex-1"></div>
            </div>
        '''

    with open(f'./public/index.html', 'w') as f:
        f.write(f'''
            <!DOCTYPE html>
            <html lang="en">

            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="style.css">
                <title>Warrior Thesis</title>
            </head>

            <body>
                {header}
                <main class="post-list container-xl mx-auto px-32 flex flex-col gap-32">
                    {final_html}
                </main>
                {footer}
            </body>

            </html>
        ''')




def md_to_html_image(text):
    title = re.findall('"([^"]*)"', text)[0]

    src_index_start = text.find('(')
    src_index_end = text.find(')')
    src = text[src_index_start+1:src_index_end].split()[0]
    
    alt_index_start = text.find('[')
    alt_index_end = text.find(']')
    alt = text[alt_index_start+1:alt_index_end].replace('-', ' ')

    return f'<p><img alt="{alt}" title="{title}" src="{src}" /></p>'

def generate_article_html(filename):
    input_filename = filename
    output_filename = filename.replace('md', 'html')

    with open(f'./private/articles/{input_filename}') as f:
        lines = f.readlines()

    html = ''
    for line in lines:
        html_tmp = ''
        if line == '\n': continue

        line = line.replace('\n', '')
        
        if 0: pass
        elif line.startswith('!'):
            html_tmp = md_to_html_image(line)
        elif line.startswith('###'): 
            line = line.replace('###', '').strip()
            html_tmp = f'<h3>{line}</h3>'
        elif line.startswith('##'): 
            line = line.replace('##', '').strip()
            html_tmp = f'<h2>{line}</h2>'
        elif line.startswith('#'): 
            line = line.replace('#', '').strip()
            html_tmp = f'<h1>{line}</h1>'
        else: 
            html_tmp = f'<p>{line}</p>'

        print(html_tmp)
        html += html_tmp

    with open(f'./private/articles-html/{output_filename}', 'w') as f:
        f.write(html)

def generate_articles_html():
    for article in os.listdir('./private/articles/'):
        generate_article_html(article)

def convert_txt_to_html(input_file, output_file):
    with open(input_file) as f:
        lines = f.readlines()

    html = ''
    for line in lines:
        if line == '\n': pass
        else: html += f'<p>{line}</p>'
        
    with open(output_file, 'w') as f:
        f.write(html)


# generate_articles_html()


# generate_posts()
# generate_assets()
generate_page_home()
generate_page_about()
generate_page_privacy_policy()






