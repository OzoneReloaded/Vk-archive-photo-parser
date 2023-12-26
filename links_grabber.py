import os
import re
import locale
from datetime import datetime
from bs4 import BeautifulSoup
from tqdm import tqdm

locale.setlocale(locale.LC_ALL, 'ru_RU')


def grabber(input_path: str, links_path: str):
    photo_num_dict = {}
    dialogue_folder_list = [d_dir for d_dir in os.listdir(input_path) if os.path.isdir(os.path.join(input_path, d_dir))]
    print(f'Диалогов найдено: {len(dialogue_folder_list)}')
    for folder in tqdm(dialogue_folder_list):
        deleted_count = 0
        dialogue_path = os.path.join(input_path, folder)
        with open(f'{dialogue_path}/1.html', 'r', encoding='windows-1251') as x:
            soup = BeautifulSoup(x, 'html.parser', from_encoding='windows-1251')
            try:
                dialogue_name = soup.select('div[class="ui_crumb"]')[-1].text
            except IndexError:
                continue
        if dialogue_name == 'DELETED':
            dialogue_name = f'{deleted_count}DELETED'
            deleted_count += 1
        dialogue_name = re.sub(r'[<>:"/\\|?*]', '', dialogue_name)
        with open(os.path.join(links_path, f'{dialogue_name}_links.txt'), 'w') as y:
            messages = [f for f in os.listdir(dialogue_path) if os.path.isfile(os.path.join(dialogue_path, f))]
            for msg_page in messages:
                with open(os.path.join(dialogue_path, msg_page), 'r', encoding='windows-1251') as x:
                    soup = BeautifulSoup(x, 'html.parser')
                    links = soup.select('a[href^="https://sun"]')
                    prev_datetime = ''
                    duplicate_num = 0
                    total_links = 0
                    for link in links:
                        format_str = "%d %b %Y в %H:%M:%S"
                        raw_date = link.find_parents()[2].find_previous_sibling().text.split(', ')[-1]
                        raw_date = raw_date.replace('мая', 'май').replace(' (ред.)', '')
                        curr_datetime = datetime.strptime(raw_date, format_str).strftime("%Y%m%d_%H%M%S")
                        if curr_datetime == prev_datetime.split('(')[0]:
                            duplicate_num += 1
                            curr_datetime = curr_datetime + f'({duplicate_num})'
                        else:
                            duplicate_num = 0
                        prev_datetime = curr_datetime
                        x = link.get('href')
                        y.write(f'{curr_datetime}___{x}\n')
                        total_links += len(links)
        if total_links == 0:
            os.remove(os.path.join(links_path, f'{dialogue_name}_links.txt'))
        else:
            photo_num_dict[dialogue_name] = total_links
    return photo_num_dict
