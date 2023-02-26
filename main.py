import shutil
import os

# if not os.path.exists('./public/assets/'):
#     os.makedirs('./public/assets/')

# shutil.copy2()


header = f'''
    <header>
        <nav class="container-xl mx-auto px-32">
            <a href="index.html">WarriorThesis</a>
            <ul>
                <li><a href="index.html">Home</a></li>
                <li><a href="./resources/bully-bending-secrets-v1.0.pdf">Bully-Bending Secrets</a></li>
                <li><a href="about.html">About</a></li>
                <li><a href="privacy-policy.html">Privacy Policy</a></li>
            </ul>
        </nav>
    </header>
'''

footer = f'''
    <footer>
        <div class="container-xl mx-auto px-32">
            <p>&#169; 2023 WarriorThesis | All Rights Reserved</p>
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

def generate_homepage():
    article_list = [article for article in os.listdir('./private/articles-html/')]

    with open(f'./private/articles-html/{article_list[0]}') as f:
        content_1 = f.read()
        
    with open(f'./private/articles-html/{article_list[1]}') as f:
        content_2 = f.read()
        
    with open(f'./private/articles-html/{article_list[2]}') as f:
        content_3 = f.read()

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
                <main class="container-xl mx-auto px-32">
                    <div class="flex">
                        <div class="flex-1">
                        {content_1[:480]}...
                        <a href="./{article_list[0]}">read more -></a>
                        </div>
                        <div class="flex-1">
                        {content_2[:480]}...
                        <a href="./{article_list[1]}">read more -></a>
                        </div>
                        <div class="flex-1">
                        {content_3[:480]}...
                        <a href="./{article_list[2]}">read more -></a>
                        </div>
                    </div>
                </main>
                {footer}
            </body>

            </html>
        ''')

generate_posts()

# generate_assets()
# generate_homepage()
