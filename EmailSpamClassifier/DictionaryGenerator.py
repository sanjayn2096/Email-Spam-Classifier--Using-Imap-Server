import os 
from collections import Counter

#HAM DICTIONARY GENERATOR

def make_ham_dictionary():
    #the path of files with a dictionary containing all the 
    path = "C:/Users/sanja/OneDrive/Desktop/email/ham1/"

    files = os.listdir(path)

    emails = [path + email for email in files]    #the adrdess of all the files in the path

    words = []
    
    for e in emails:
        f = open(e)
        content = f.read()
        words+= content.split(" ")

    words_count = Counter(words)

    del words_count['http']
    del words_count['height']
    del words_count['border']
    
    return words_count.most_common(3000)
	
h = make_ham_dictionary()
HAM ={}

for k,v in h:
    HAM[k] = v
print("The non spam list is as follows")
print(HAM)



#SPAM DICTIONARY GENERATOR
def make_spam_dictionary():
    #the path of files with a dictionary containing all the 
    path = "C:/Users/sanja/OneDrive/Desktop/email/spam1/"

    files = os.listdir(path)

    emails = [path + email for email in files]    #the address of all the files in the path

    words = []
    
    for e in emails:
        f = open(e)
        content = f.read()
        words+= content.split(" ")

    words_count = Counter(words)

    del words_count['http']
    del words_count['height']
    del words_count['border']
    
    return words_count.most_common(3000)


s = make_spam_dictionary()
SPAM ={}
for k,v in s:
    SPAM[k] = v
print("SPAM Mail Words List")
print()
print(SPAM)
