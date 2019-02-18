import numpy as np
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

# iris data set contains 50*3(category)=150 samples  ,each record has 4 attributes
iris=datasets.load_iris()
print('Samples set size：',iris.data.shape,iris.target.shape)  #  data:features target:labels

#use cross validation to create training and testing part
# the test set  and training set for Byes and SVM are same
X_train,X_test,y_train,y_test=train_test_split(iris.data,iris.target,test_size=0.4,random_state=0)#test:0.4 train:0.6
print('Train set size：',X_train.shape,y_train.shape)  # the size of training
print('Test set size：',X_test.shape,y_test.shape)  # the size of test

# question1 by naive byes
clf2 = GaussianNB()
y_nb=clf2.fit(X_train, y_train)
y_nb_pred = y_nb.predict(iris.data)    #predict() method is used to predict data from already fitted model
print("The accuracy by Gaussian Naive Bayes is",y_nb.score(X_test, y_test))

#question 2 by linear svm

clf = svm.SVC(kernel='linear', C=1)
y_svm=clf.fit(X_train, y_train)
y_svm_pred=y_svm.predict(iris.data)
print('SVM Accuracy：',y_svm.score(X_test, y_test))


from sklearn.metrics import classification_report,accuracy_score, auc, confusion_matrix, f1_score, precision_score, recall_score
recall_str=classification_report(iris.target,y_nb_pred) #make a comparison between orignal data and the predicted label with our new model
print("Naive Bayes:")
print(recall_str)
recall_str_nb=classification_report(iris.target,y_svm_pred)
print("SVM:")
print(recall_str_nb)