# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 10:02:38 2017

@author: lenovo
"""

from sklearn.naive_bayes import MultinomialNB
from sklearn.datasets.base import Bunch
import pickle
from sklearn import metrics
import numpy as np

def readBunchObj(path):
  fileObj = open(path,"rb")
  bunch = pickle.load(fileObj)
  fileObj.close()
  return bunch

def writeBunchObj(path,bunchObj):
  fileObj = open(path,"wb")
  pickle.dump(bunchObj,fileObj)
  fileObj.close()
  
train_path = "D:/Data Science Experiment/Chinese Text Clustering/tfidf_space.dat"
test_path = "D:/Data Science Experiment/Chinese Text Clustering/bayes_tfidf_space.dat"

train_set = readBunchObj(train_path)
test_set = readBunchObj(test_path)

clf = MultinomialNB(alpha=0.01).fit(train_set.tdm,train_set.label)

print(np.shape(test_set.tdm))
print(np.shape(train_set.tdm))
# here is a problem: dot conduct requires coroperate dimensions
predicted = clf.predict(test_set.tdm)
total = len(predicted);rate = 0
for a,b,c in zip(test_set.label,test_set.filename,predicted):
  if a != c:
    rate+=1
    print(b,"real:",a," predicted:",c)
  print("error rate:",float(rate*100)/float(total),"%")

  
def metrics_result(actual,predict):
  print("precision: ",metrics.precision_score(actual,predict))
  print("recall:",metrics.recall_score(actual,predict))
  print("f1_score:",metrics.f1_score(actual,predict))

metrics_result(test_set.label,predicted)
  
print("finished!")
