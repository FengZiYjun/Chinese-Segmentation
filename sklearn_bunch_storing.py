# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 09:27:26 2017

@author: lenovo
"""

import sys
import os
import pickle
from sklearn.datasets.base import Bunch

bunch = Bunch(target_name = [],label=[],filename=[],contents=[])

# seg_path = "D:/Data Science Experiment/Chinese Text Clustering/corpus_segments/"
# bunch_path = "D:/Data Science Experiment/Chinese Text Clustering/words_bag.dat"
seg_path = "D:/Data Science Experiment/Chinese Text Clustering/test_segment/"
bunch_path = "D:/Data Science Experiment/Chinese Text Clustering/bayes_bunch.dat"

catelist = os.listdir(seg_path)
print(catelist)
for mydir in catelist:
  class_path = seg_path + mydir + "/"
  file_list = os.listdir(class_path)
  for file_path in file_list:
    fullname = class_path + file_path
    bunch.label.append(mydir)
    bunch.filename.append(fullname)
    fileObj = open(fullname)
    bunch.contents.append(fileObj.read().strip())
    fileObj.close()

file_obj = open(bunch_path,"wb")
pickle.dump(bunch,file_obj)
file_obj.close()
print("finished!")
