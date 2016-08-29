'''
Created on May 30, 2016
@author: Nilam
'''

import os
import nltk, re
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import csv

for year in range(1964,2015):
    #Open directory if it exists
    if os.path.exists("F:/Nilam/MSBA_Degree/CISI/pubmed/MonoClonal_Antibody/Pubmed_Data/"+str(year)+"/"):
        with open("F:/Nilam/MSBA_Degree/CISI/pubmed/MonoClonal_Antibody/Pubmed_Data/"+str(year)+"/file_one.txt") as f:
            data = f.read()
            
            #Clean Data
            data = data.replace('FullText :b','')
            data = data.replace('\\n','');
            data = data.replace('-', ' ');
            data = re.sub('[,$:;\\\]*', '', data);
            data = re.sub('[\s]+', ' ',data);
            
            #Convert to lower case
            txt = data.lower();
            
            #List of stop words that we want to remove
            stop_words = set(stopwords.words('english'));

            #List of other words that we want to remove
            remove_words = ['titleb',
                'abstractb','cells','cell','b','il','c','p','official',
                'journal','american','clinical','present','study','long',
                'term','result','suggest','american','society','journal',
                'aim','study','important','role','ng','ml','year','old',
                'immunology','mg','kg','official','publication','microg',
                'ml','first','line','association','baltimore','md','ki',
                '67','sars','cov','e','g','baltimore','md','1950','za','zhi',
                'journal','biological','determine','whether','british','journal',
                'play','important','japanese','journal','gastroenterology',
                '24','h','chinese','journal','expert','international','xue','za','america',
                'sciences','united','proceedings','national','academy','states','mol','wt','000',
                'dalton','results','obtained','molecular','weights','m','w','could','detected',
                '37','degrees','previously','described','x','m','et','al','daltons','less','001',
                'results','show','mol','may','useful'
                ]
            
            #Load tokenizer and lemmatizer
            tokenizer =  RegexpTokenizer(r'\w+')
            lemmatizer = nltk.stem.WordNetLemmatizer()
            
            #Tokenize into words
            word_tokens = tokenizer.tokenize(txt)
            
            #Remove all stop words and extra words we are not interested in
            filtered_sentence = []
            for w in word_tokens:
                if w not in stop_words and w not in remove_words:
                        filtered_sentence.append(w)
            
            #Perform lemmatization
            lemmas = [lemmatizer.lemmatize(t) for t in filtered_sentence]
            filtered_sentence = lemmas
            
            #Open CSV file to write ngrams
            file1 = csv.writer(open("F:/Nilam/MSBA_Degree/CISI/pubmed/MonoClonal_Antibody/Output/"+str(year)+"_ngram.csv", 'w', newline =''))
            
            #Create bigrams, rigrams and four grams
            fd1 = nltk.bigrams(filtered_sentence)
            fd2 = nltk.trigrams(filtered_sentence)
            fd3 = nltk.ngrams(filtered_sentence,4)
            fd5 = nltk.FreqDist(fd1)
            fd6 = nltk.FreqDist(fd2)
            fd7 = nltk.FreqDist(fd3)

            #Write top 100 bigrams, trigrams and 4-grams to output file
            for key, count in fd5.most_common(100):
                file1.writerow([key, count])
            for key, count in fd6.most_common(100):
                file1.writerow([key, count])
            for key, count in fd7.most_common(100):
                file1.writerow([key, count])