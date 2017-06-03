# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 15:17:16 2017

@author: lenovo
"""

import sys
import os
from sklearn.datasets.base import Bunch
import pickle
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

def readBunchObj(path):
  fileObj = open(path,"rb")
  bunch = pickle.load(fileObj)
  fileObj.close()
  return bunch

def writeBunchObj(path,bunchObj):
  fileObj = open(path,"wb")
  pickle.dump(bunchObj,fileObj)
  fileObj.close()

# path = "D:/Data Science Experiment/Chinese Text Clustering/words_bag.dat"
path = "D:/Data Science Experiment/Chinese Text Clustering/bayes_bunch.dat"
bunch = readBunchObj(path)

tfispace = Bunch(target_name = bunch.target_name,label=bunch.label,filename=bunch.filename,tdm=[],vocabulary={})

vectorizer=TfidfVectorizer(max_df=0.5)
tansformer = TfidfTransformer()

tfispace.tdm=vectorizer.fit_transform(bunch.contents)
print(tfispace.tdm) # matrix about what?
tfispace.vocabulary = vectorizer.vocabulary_
# dictionary of IF-DIF of each word
print(tfispace.vocabulary) 

space_path = "D:/Data Science Experiment/Chinese Text Clustering/bayes_tfidf_space.dat"
writeBunchObj(space_path,tfispace)

print("finished!")



