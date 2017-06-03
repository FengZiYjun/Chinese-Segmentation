#coding: utf-8
"""
Spyder Editor

This is a temporary script file.
"""
import sys 
import os
import jieba
import codecs
 #reload(sys)
 #sys.setdefaultencoding('unicode')

def savefile(path,content):
    fp = open(path,"w")
    fp.write(content)
    fp.close()
    
def readfile(path):
    #content=""
    #with open(path) as f:
    #    for line in f:
    #        if "　" in line:
    #            line = line.replace("　","")
    #        content+=line
    #return content
    
    fp = open(path,"r")
    try:
        content = fp.read()
    except:
        content = ""
    fp.close()
    return content
    
    
# corpus_path = "D:/Data Science Experiment/Chinese Text Clustering/train_corpus/"
corpus_path = "D:/Data Science Experiment/Chinese Text Clustering/test_corpus/"
seg_path = "D:/Data Science Experiment/Chinese Text Clustering/test_segment/"

catelist = os.listdir(corpus_path)
print(catelist)
for mydir in catelist:
    class_path = corpus_path + mydir + "/"
    seg_dir = seg_path + mydir + "/"
    if not os.path.exists(seg_dir):
        os.makedirs(seg_dir)
    file_list = os.listdir(class_path)
    print(file_list)
    for file_path in file_list:
        print(file_path)
        fullname = class_path+file_path
        content = readfile(fullname).strip()
        content = content.replace("\r\n","").strip()
        content_seg = jieba.cut(content)
        savefile(seg_dir + file_path, " ".join(content_seg))

        
    

