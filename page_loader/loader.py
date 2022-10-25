import pathlib
import requests
import re


def download(url, output=pathlib.Path.cwd()):
    save_file = requests.request('GET', url).text
    if url.startswith('http:'):
        file_name = re.sub(r'\W', '-', url[7::])
    elif url.startswith('https:'):
        file_name = re.sub(r'\W', '-', url[8::])
    with open(f'{output}/{file_name}.html', 'w', encoding='utf-8') as f:
        f.write(save_file)
    return f'{output}/{file_name}.html'
