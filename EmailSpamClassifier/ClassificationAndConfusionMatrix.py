from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn import neighbors
from sklearn.metrics import confusion_matrix
from sklearn import metrics
import seaborn as SNS
%matplotlib inline
import matplotlib.pyplot as plt
count=0
Index=[]
second=[]


x_train , x_test, y_train,y_test = tts(features_all,labels_all,test_size = 0.3)
#print(y_train[0:10])
#print(len(y_test))
classifier = MultinomialNB()
classifier.fit(x_train,y_train)
preds = classifier.predict(x_test)


classifier2 = SVC()
classifier2.fit(x_train,y_train)
preds2 = classifier2.predict(x_test)


classifier3 = neighbors.KNeighborsClassifier()
classifier3.fit(x_train,y_train)
preds3 = classifier2.predict(x_test)


print("accuracy score of Naive = " , accuracy_score(y_test , preds))
print("accuracy score of SVM = " , accuracy_score(y_test , preds2))
print("accuracy score of KNN = " , accuracy_score(y_test , preds3))


#plt.scatter(x_test,y_test)



mat_naive = confusion_matrix(y_test, preds)
mat_SVM = confusion_matrix(y_test, preds2)
mat_knn = confusion_matrix(y_test, preds3)

print(zip(y_test,preds))
for index, (first, second) in enumerate(zip(y_test, preds)):
   
    if first != second:
        print(index, second)
        Index.append(index)
        count=count+1
#print(count)
#print(second)

plt.figure(figsize = (10,5))

SNS.heatmap(mat_naive.T, square=True, annot=True, fmt='d', cmap="BuPu",cbar=False,xticklabels=['spam' , 'not spam'], yticklabels=['spam' , 'not spam'])


#SNS.heatmap(mat.T, square=True, annot=True, fmt='d', cmap="BuPu",cbar=False,xticklabels=['spam' , 'not spam'], yticklabels=['spam' , 'not spam'])

plt.xlabel('true label' , fontsize =10)
plt.ylabel('predicted label', fontsize =10);
plt.title("Confusion Matrix of Naive Bayes Classifier")
