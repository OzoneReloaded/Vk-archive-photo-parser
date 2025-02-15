import time
import os
import requests
from tqdm import tqdm


def downloader(link_path: str, output_path: str):
    links = [d_dir for d_dir in os.listdir(link_path) if "_links.txt" in d_dir]
    for link_item in tqdm(links):
        dialogue_folder = link_item.rsplit('_')[0]
        if not os.path.exists(os.path.join(output_path, dialogue_folder)):
            os.makedirs(os.path.join(output_path, dialogue_folder))
        with open(os.path.join(link_path, link_item), 'r') as f:
            line = f.readline()
            try:
                while line:
                    try:
                        datetime_name, x = line.strip().split('[SEP]')
                    except ValueError:
                        print(line.strip())
                    line = f.readline()
                    target_path = f'{output_path}/{dialogue_folder}/{datetime_name}.jpg'
                    if not os.path.exists(target_path):
                        r = requests.get(x, stream=True)
                        with open(target_path, 'wb') as fd:
                            for chunk in r.iter_content():
                                fd.write(chunk)
                    else:
                        continue
            except TimeoutError:
                print('Задержка ответа от сервера, ожидайте')
                time.sleep(5)
                pass
