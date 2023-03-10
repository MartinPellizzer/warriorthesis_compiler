import time
import os
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageColor

options = webdriver.ChromeOptions()
options.add_argument("--log-level=3")
options.add_argument("user-data-dir=C:\\Users\\admin\\AppData\\Local\\Google\\Chrome Beta\\User Data\\")
options.binary_location = "C:\\Program Files\\Google\\Chrome Beta\\Application\\chrome.exe"

driver = webdriver.Chrome(executable_path='C:\\drivers\\chromedriver', chrome_options=options)
driver.maximize_window()

articles = [a for a in os.listdir('articles')]
for article in articles:
    with open(f'./articles/{article}/h1.txt') as f:
        title = f.read().strip()
    sections = [s for s in os.listdir(f'./articles/{article}/sections')]
    section = random.choice(sections)
    with open(f'./articles/{article}/sections/{section}') as f:
        description = f.read().strip()[:280] + '...'
    link = f'https://warriorthesis.com/{article}.html'



    images = [img for img in os.listdir('F:\\images\\1000x1500\\')]
    image_random = random.choice(images)
    img = Image.open(f'F:\\images\\1000x1500\\{image_random}')

    font_size = 96

    text = title.upper()
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('./fonts/Helvetica-Bold.ttf', font_size)

    img_w, _ = img.size

    lines = []
    line = ''
    for word in text.split():
        word_w, _ = draw.textsize(word, font=font)
        line_w, _ = draw.textsize(line, font=font)
        if line_w + word_w < img_w:
            line += word + ' '
        else:
            lines.append(line.strip())
            line = word + ' '
    lines.append(line.strip())
    print(lines)

    _, line_h = draw.textsize(text, font=font)
    n_lines = len(lines)
    line_spacing = 1.2
    center_v = 1500//2
    padding_y = line_h * 0.66
    offset_top =  line_h * n_lines // 2

    draw.rectangle((
        (0, center_v - line_h//2 - padding_y - offset_top), 
        (1000, center_v + line_h//2 + padding_y + line_h * (n_lines-1) * line_spacing - offset_top)
        ), fill=(11, 11, 11))

    for i, line in enumerate(lines):
        w, _ = draw.textsize(line, font=font)
        draw.text((
            1000//2 - w//2, 
            center_v - line_h//2 + line_h * i * line_spacing - offset_top
            ), line, (255, 255, 255), font=font)

    # img.show()
    image_path = f"./pins/{article}.jpg"
    img.save(image_path)



    driver.get("https://pinterest.com")
    time.sleep(3)

    driver.get("https://www.pinterest.com/pin-builder/")
    time.sleep(3)

    path = os.path.abspath(image_path)
    e = driver.find_element(By.XPATH, '//input[@type="file"]')
    e.send_keys(path)
    time.sleep(10)

    e = driver.find_element(By.XPATH, '//textarea')
    e.send_keys(Keys.CONTROL + "a")
    e.send_keys(Keys.DELETE)
    e.send_keys(title)
    time.sleep(10)

    e = driver.find_element(By.XPATH, '//div[@class="DraftEditor-editorContainer"]/div')
    e.send_keys(Keys.CONTROL + "a")
    e.send_keys(Keys.DELETE)
    e.send_keys(description)
    time.sleep(10)

    e = driver.find_elements(By.XPATH, '//textarea')
    e[1].send_keys(Keys.CONTROL + "a")
    e[1].send_keys(Keys.DELETE)
    e[1].send_keys(link)
    time.sleep(10)

    e = driver.find_element(By.XPATH, '//button[@data-test-id="board-dropdown-save-button"]')
    e.click()
    time.sleep(30)

    driver.get("https://google.com")
    time.sleep(3)

    time.sleep(300)