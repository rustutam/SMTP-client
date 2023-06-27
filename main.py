from сonstruct.constructor import build_msg
from сonstruct.executor import handle_pswd
from SMTP_client import SMTP_Client

if __name__ == '__main__':
    header, message, names_to_copy = build_msg()
    password = handle_pswd()
    client = SMTP_Client()
    client.send_message(header, message, password, names_to_copy)
