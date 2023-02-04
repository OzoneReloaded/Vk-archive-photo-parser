# Vk-archive-photo-parser
Скрипт позволяет получить ссылки и скачать фотографии из любого диалога, используя файлы из [официального архива ВК](https://vk.com/data_protection?section=rules&scroll_to_archive=1), сортируя скачанное в хронологическом порядке
## Алгоритм
1. Сортировка файлов типа ```messagesXXX.html``` в нужном порядке
2. Поиск ссылок на фотографии
3. Загрузка фото
## Установка
1. Скачать архив, распаковать в папку
2. Установить библиотеки ```pip install -r requirements.txt```
3. Создать папки ```input``` и ```photo```
## Запуск
1. В папку ```input``` переместить файлы формата ```messagesXXX.html```
2. Открыть файл main.py
