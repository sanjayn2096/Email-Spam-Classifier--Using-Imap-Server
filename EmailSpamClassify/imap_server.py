import imaplib, email, os
import nltk, re, pprint
import getpass
from nltk import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
nltk.download('punkt')
nltk.download('wordnet')

password = getpass.getpass("Password for sanjaynagraj@gmail.com: ")    # prompt for user to enter his password
user = 'sanjaynagraj@gmail.com'

user2 = 'sanjaygaddar@gmail.com'
password2 = getpass.getpass("Password for sanjaygaddar@gmail.com: ")    # prompt for user to enter his password

imap_url = 'imap.gmail.com'
#Where you want your attachments to be saved (ensure this directory exists) 
attachment_dir = 'your_attachment_dir'
# sets up the auth
def auth(user,password,imap_url):
    con = imaplib.IMAP4_SSL(imap_url)
    con.login(user,password)
    return con
# extracts the body from the email
def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None,True)

#extracts emails from byte array
def get_emails(result_bytes):
    msgs = []
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.append(data)
    return msgs



con = auth(user,password,imap_url)
con2 = auth(user2,password2,imap_url)


for i in con.list()[1]:
    print(i)

