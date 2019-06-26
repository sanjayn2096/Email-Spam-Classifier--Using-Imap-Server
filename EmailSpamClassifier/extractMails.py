def extractMails(email_num , category , mailboxnum):
    
    n = str(repr(email_num))
    print(n)
    bytes_n = bytes(n, 'utf-8')    # converting the number into utf-8 encoding 
   
    if(mailboxnum == 0):
        con.select(category)  # whether to access mails from inbox or spam
        result, data = con.fetch(bytes_n,'(RFC822)')
        raw = email.message_from_bytes(data[0][1])
    if(mailboxnum == 1):
        con2.select(category)  # whether to access mails from inbox or spam
        result, data = con2.fetch(bytes_n,'(RFC822)')
        raw = email.message_from_bytes(data[0][1])
        
    
                                              ###  NLP TECHNIQUES TO FILTER THE TEXT###
        
    #tokenizes the words in  the data set
    tokens = word_tokenize(str(get_body(raw)))    
    # creating an object of lemmatizer
    lmtzr = WordNetLemmatizer()
    # filter the unwanted character in the mail that we get i.e remove the non alpha numeric characters
    # checks if the words in the list 'tokens' are alphabets or not , else just removes them
    words = []
    for word in tokens:
        if(word.isalpha() and len(word) > 2 ):
            word = word.lower()                  #convert everything to lower case
            word = lmtzr.lemmatize(word)         # lemmatize the word
            words.append(word)                   # append it to a list called words[]
    
    
    #removing some unwanted repetitive words like 
    unwanted = [ ':' , ';' , "''" , ","," " , "/","<",">","(",")","*","&","^","`","~","|","'", "xml", "http" ,'color','rgb','weight','https' ,'helvetica','georgia','top','collapse','important','border' , 'http','width' ,'height','border','elseif', 'if']
    for i  in words:
        if(i in unwanted):
            words.remove(i) 
            
    #create a seperate list to attach all the owrds and then to convert it to a string to be attached into a text file
    text = []
    for word in words:
        text.append(word)
        text.append(" ")
    
    #for training purpose let us append a word , spam or ham
    if(category == 'INBOX'):
        text.append('ham')
    if(category == '[Gmail]/Spam'):
        text.append('spam')
        
        
    text_file = "".join(text)
    
    
    return text_file