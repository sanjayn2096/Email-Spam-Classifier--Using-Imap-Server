from pathlib import Path


#generates a folder containing 'n' number of emails in my gmail INBOX
def ham_generator(n):
    folder = 'INBOX'
    for mailboxnum in range(2):
        for i in range(1,n):
            #b = i.encode('utf-8')
            text_file = extractMails(i , 'INBOX' , mailboxnum)
            data_folder = Path("C:/Users/Desktop/email/ham1")   #insert the name of datapath where you want to store these files
            if not os.path.exists(data_folder):
                os.makedirs(data_folder)
            filename = gen_filename(folder , mailboxnum+1 , i,'ham')
            file_to_open = data_folder/filename
            file1 = open(file_to_open, "w")
            file1.write(text_file)
            file1.close()

#generates a folder containing 'n' number of spam mails in my gmail
def spam_generator(n,folder):
    foldername = folder
    if(folder == 'newspam'):                
        count = 1
    else:
        count = 2
        
    for mailboxnum in range(count):          #0 is example1@gmail.com   and #1 is example2@gmail.com
        if(mailboxnum == 1 & n >46 ):        # if mail box is sanjaygaddar@gmail.com
            n = 46
            
        for i in range(1,n):
            #b = i.encode('utf-8')
            if(folder == '[Gmail]/Spam'):
                foldername = 'actualspam'
            text_file = extractMails(i , folder , mailboxnum)
            data_folder = Path("C:/Users/email/spam1")  #insert the name of datapath where you want to store these files
            if not os.path.exists(data_folder):
                os.makedirs(data_folder)
            filename = gen_filename(foldername, mailboxnum+1, i,'spam')
            print(filename)
            file_to_open = data_folder/filename
            file1 = open(file_to_open, "w")
            file1.write(text_file)
            file1.close()
        
        
ham_generator(300)
#spam_generator(50)
#spam_generator(1000,'newspam')
spam_generator(99, '[Gmail]/Spam')