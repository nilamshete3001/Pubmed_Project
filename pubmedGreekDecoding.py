'''
Created on Mar 13, 2016
@author: Nilam

'''
import nltk
from collections import Counter
import os

ls = list()
data_root="F:\\Nilam\\MSBA_Degree\\CISI\\pubmed\\greek\\"
files_in_dir = os.listdir(data_root)

for file in files_in_dir:
    #Open file in binary mode
    with open(data_root + file, "rb") as f:
        data = f.read()
        data = data.lower();
        
        #Decode data from utf-8 format
        data = data.decode("utf-8","replace")
        text = ' '.join([word for word in data.split()])    
        tokens = nltk.word_tokenize(text)
        ls.append(Counter(tokens))        