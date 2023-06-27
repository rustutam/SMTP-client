import base64
import json
import os
from datetime import datetime

from сonstruct.information import Header, File, content_types


def h_conf():
    with open('reliances/config.json', 'r', encoding="utf-8") as json_file:
        file = json.load(json_file)

        name_from = file['from']
        name_to = file['to']
        subject = file['subject']
        path_to_files = file['attachments']
        names_to_copy = file['cc']
        address = names_to_copy.split(', ')
        file_with_message = file['file_with_message']

        subject_to_message = _h_sub(subject)
        date = _h_date()

        return Header(name_from, name_to, subject_to_message, 
                      names_to_copy, date), \
               path_to_files, file_with_message, address


def _h_date():
    real_time = datetime.now()
    format = real_time.strftime('%a, %d %b %Y %H:%M:%S %z')
    return format


def _h_sub(subject: str):
    max_length = 998
    h = ""

    while len(subject) > max_length:
        h += subject[:max_length] + "\r\n "
        subject = subject[max_length:]

    h += subject

    return h


# Обрабатываем текст сообщения
def h_file(path_to_send_files):
    files = []
    for filename in os.listdir(path_to_send_files):
        file_path = os.path.join(path_to_send_files, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file_path)[1]
            with open(file_path, 'rb') as f:
                send_file = base64.b64encode(f.read()).decode()
                file_type = content_types.get(file_extension)
                files.append(File(filename, file_type, send_file))
    return files


# Обрабатываем файлы
def handle_pswd():
    with open("reliances/your_pswd.txt", "r", encoding="UTF-8") as file:
        password = file.read().strip()
    return password


def handle_msg_text(file_with_message):
    with open(file_with_message, encoding='utf-8') as file:
        text = file.read().split('\n')
        new_text = ''
        for i in range(len(text)):
            if text[i] == len(text[i]) * '.':
                new_text += text[i] + '.\n'
            else:
                new_text += text[i] + '\n'
    return new_text
