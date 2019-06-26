import os 
from collections import Counter

def make_dictionary():
    #the path of files with a dictionary containing all the 
    path = "C:/Users/sanja/OneDrive/Desktop/email/all1/"

    files = os.listdir(path)

    emails = [path + email for email in files]    #the adresse of all the files in the path

    words = []
    
    for e in emails:
        f = open(e)
        content = f.read()
        words+= content.split(" ")

    words_count = Counter(words)

    del words_count['http']
    del words_count['height']
    del words_count['border']
    
    return words_count.most_common(6000)


def make_features_labels(dictionary):
    #C:\Users\sanja\OneDrive\Desktop\email
    path = "C:/Users/sanja/OneDrive/Desktop/email/all1/"
    #os.chdir(path)

    files = os.listdir(path)

    emails = [path + email for email in files]    #the list contains the addresses of all the files in the path

    feature_set = []
    labels = []
    
    c = len(emails)
    for email in emails:
        data = []
        f = open(email)
        words = f.read().split(' ')
        for entry in dictionary:
            #entry[0]
            data.append(words.count(entry[0]))  #how many times a particular key in the dictionary occurs in the email list occurs
                                                #entry[0] means key value of the dictionary element
                                                # append the count of the word found in the email to the 
        feature_set.append(data)
        
        # for convenience i had labelled all the emails as spam or ham in the beginning
        if "ham" in email:     
            labels.append(0)
        if "spam" in email :
            labels.append(1)
            
    return feature_set,labels

dall = make_dictionary()
features_all, labels_all = make_features_labels(dall)

ALL ={}
for k,v in dall:
    ALL[k] = v
print("List containing all the words")
print()
print(ALL)


C1=C2=C=dict()
print(type(dall))
C1 = {k:v for k,v in ALL.items() if k not in HAM}
C2 = {k:v for k,v in ALL.items() if k not in SPAM}
def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z
C = merge_two_dicts(C1, C2)
print(C)
features1, labels1 = make_features_labels(C.items())

