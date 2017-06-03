# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 15:06:34 2017

@author: lenovo
"""

import numpy as np

def loadDataSet():
  postingList=[['my','dog','has','a'],
               ['i','am','not','an','good'],
               ['his','is','well','designed']]
  classVec = [0,1,1]
  return postingList,classVec

class bayes(obj):
  def _init_(self):
    self.vocab = []
    self.idf = 0 # matrix
    self.tf = 0 # matrix
    self.tdm = 0 # P(x|y)
    self.Pcates = {}
    self.labels = []
    self.doclenth = 0
    self.vocablen = 0
    self.testset = 0
    
  def train_set(self,trainset,classvec):
    self.cate_pro(classvec)
    self.doclenth = len(trainset)
    
    tempset = set()
    [tempset.add(word) for doc in trainset for word in doc]
    self.vocab = list(tempset)
    
    self.vocablen = len(self.vocab)
    self.cul_word_freq(trainset)
    self.build_tdm()
    
  def cate_pro(self,classvec):
    self.labels = classvec
    labeltmp = set(self.labels)
    for label in labeltmp:
      self.Pcates[label] = float(self.labels.count(label)/float(len(self.labels)))
    
  def cul_word_freq(self,trainset):
    self.idf = np.zeros([1,self.vocab])  # build two matrics? 
    self.tf = np.zeros([self.doclenth,self.vocablen])
    for f in range(self.doclenth):
      for word in trainset[f]:
        self.tf[f,self.vocab.index(word)]+=1
      for signalword in set(trainset[f]):
        self.idf[0,self.vocab.index(signalword)]+=1
  
  def build_tdm(self):
    self.tdm = np.zeros([len(self.Pcates),self.vocablen])
    sumlist = np.zeros(len(self.Pcates),1)
    for index in range(self.doclenth):
      self.tdm[self.labels[index]] = np.sum(self.tdm[self.labels[index])
    self.tdm = self.tdm/sumlist
    
  def mapTolist(self,testdata):
    self.testset = np.zeros([1,self.vocablen])
    for w in testdata:
      self.testset[0,self.vocab.index(w)]+=1
  
  def predict(self,testset):
    if np.shape(testset)[1] != self.vocablen:
      print("dimension error")
      exit(0)
    else:
      prevalue = 0
      preclass ""
      for tdm_vec, keyclass in zip(self.tdm,self.Pcates):
        tmp = np.sum(testset * tdm_vec * self.Pcates[keyclass])
        if tmp > prevalue:
          prevalue = tmp
          preclass = keyclass
    return preclass
                   
    
    
    
               