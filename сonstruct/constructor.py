from сonstruct.information import Header
from сonstruct.executor import h_conf, handle_msg_text, h_file

LIMIT = "bound.40629"


def build_msg():
    header, path_to_send_files, file_with_message, names_to_copy = h_conf()
    _text_message = handle_msg_text(file_with_message)
    files = h_file(path_to_send_files)

    header_message = _const_header(header)
    text_message = _build_msg_text(_text_message)
    files_message = _build_msg_file(files)
    message = header_message + text_message + files_message + f'--{LIMIT}--\n.'
    return header, message, names_to_copy


def _build_msg_file(files):
    files_body = ''
    for file in files:
        files_body += f'--{LIMIT}\n' \
                      f'Content-Disposition: attachment;\n' \
                      f'filename="{file.name_file}"\n' \
                      f'Content-Transfer-Encoding: base64\n' \
                      f'Content-Type: {file.file_type}; ' \
                      f'name="{file.name_file}"\n\n' \
                      f'{file.data}\n\n'
    return files_body


def _build_msg_text(text_message):
    text_body = f'--{LIMIT}\n' \
                f'Content-Type: text/plain; charset=utf-8\n\n' \
                f'{text_message}\n\n'
    return text_body
# Собираем текст сообщения


# Собираем часть сообщения с файлами

def _const_header(header: Header) -> str:
    header_message = f'From: {header.name_from}\n' \
                     f'To: {header.name_to}\n' \
                     f'Cc: {header.names_to_copy}\n' \
                     f'Subject: {header.subject}\n' \
                     f'MIME-Version: 1.0\n' \
                     f'Date: {header.date}\n' \
                     f'Content-Type: multipart/mixed; ' \
                     f'LIMIT={LIMIT}\n\n'
    return header_message
