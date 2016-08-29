'''
Created on Oct 7, 2015
@author: Nilam

'''
from Bio import Entrez
import os

Entrez.email="shete_nila@bentley.edu"

#List of keywords you want to search
keywords = {"cystic fibrosis transmembrane conductance regulator[MeSH Terms]", "monoclonal antibody"}


for key in keywords:
    #Connect to pubmed database
    data = Entrez.esearch(db="pubmed",retmax=1000000, term = key, sort="pubDate")
    
    #Read data
    res=Entrez.read(data)
    
    #Extract all pubmed IDs for each keyword
    PMID = res["IdList"]
    
    #Create output directory if it does not exist
    directory = '/Nilam/MSBA_Degree/CISI/pubmed/Output/'+key
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    #Extract Data for all pubmed IDs
    for pubid in PMID:
        
        #Fetch Data in XML format
        handle = Entrez.efetch(db='pubmed', id=pubid, retmode='xml')
        xml_data = Entrez.read(handle)[0]
        
        #Extract data for title, date, Abstract
        try:
            article = xml_data['MedlineCitation']['Article']
            title = article['Journal']['Title']
            title = title.encode('utf-8','xmlcharrefreplace')
                
            jl = article['Journal']['JournalIssue']
            if u'Year' in jl['PubDate']:
                year = jl['PubDate']['Year']    
            else:
                year = jl['PubDate']['MedlineDate'][0:4]
            directory1 = directory+"/"+year
            if not os.path.exists(directory1):
                os.makedirs(directory1)
            if u'Abstract' in article:    
                abstract = article['Abstract']['AbstractText'][0]                
                abstract = abstract.encode('utf-8','xmlcharrefreplace')
                        
            #Write data to text files            
            fileFullText =  directory1+'/'+pubid+'.txt'
            file1 = open(fileFullText, "w")
            if(title or abstract):
                file1.write('Title:'+str(title)+'\n')
                file1.write('Abstract:'+str(abstract)+'\n')
        except:
            print("No MedlineCitation")
            