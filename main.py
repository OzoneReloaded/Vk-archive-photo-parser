import os

from dowloader import downloader
from links_grabber import grabber
from renamer import rename

paths = {'in_path': './input',
         'out_path': './photo',
         'links_path': './links'}


def main():
    print(''' __      ___  __                 _     _                   _           _                                         
 \ \    / / |/ /                | |   (_)                 | |         | |                                        
  \ \  / /| ' /    __ _ _ __ ___| |__  ___   _____   _ __ | |__   ___ | |_ ___    _ __   __ _ _ __ ___  ___ _ __ 
   \ \/ / |  <    / _` | '__/ __| '_ \| \ \ / / _ \ | '_ \| '_ \ / _ \| __/ _ \  | '_ \ / _` | '__/ __|/ _ \ '__|
    \  /  | . \  | (_| | | | (__| | | | |\ V /  __/ | |_) | | | | (_) | || (_) | | |_) | (_| | |  \__ \  __/ |   
     \/   |_|\_\  \__,_|_|  \___|_| |_|_| \_/ \___| | .__/|_| |_|\___/ \__\___/  | .__/ \__,_|_|  |___/\___|_|   
                                                    | |                          | |                             
                                                    |_|                          |_|                             ''')
    input('Press Enter')

    for path_value in paths.values():
        if not os.path.exists(path_value):
            os.makedirs(path_value)
            print(f"Создана папка '{path_value}'")

    for dialogue_path in [os.path.join(paths['in_path'], folder)
                          for folder in os.listdir(paths['in_path'])
                          if os.path.isdir(os.path.join(paths['in_path'], folder))]:
        rename(dialogue_path)
    print('Файлы отсортированы.')
    amount = grabber(paths['in_path'], paths['links_path'])
    print(f'Найдено {sum(amount.values())} изображений в {len(amount)} диалогах')
    downloader(paths['links_path'], paths['out_path'])
    print(f'Фотографии находятся в /photo')
    input('Press Enter to close')


def clear():
    if os.sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')


if __name__ == '__main__':
    clear()
    main()
