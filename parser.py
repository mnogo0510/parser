import os
import re

import requests


# src=\"(https?://icdn\.lenta\.ru/images/[\d/]+[\d\w]+\.(png|jpeg|jpg))\"
#https://regex101.com/

proxies = {
  'http': 'http://proxy.proxy.ru:8080',
  'https': 'https://proxy.proxy.ru:8080'
}

page = requests.get('https://lenta.ru/articles/2017/07/05/navysalon/', proxies=proxies)

text = page.text.split('/n')
pattern = re.compile('src=\"(https?://icdn\.lenta\.ru/images/[\d/]+[\d\w]+\.(png|jpeg|jpg))\"')

image_list = []

for each_line in text:
    search_result = re.search(pattern, each_line)
    if search_result is not None:
        image_list.append(search_result.group(1))

for element in image_list:
    image = requests.get(element, proxies=proxies)
    image_path = os.path.join('.', os.path.basename(element))
    with open(image_path, mode='bx') as temp_file:
        temp_file.write(image.content)
