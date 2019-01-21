#initialize functions for prefixes and suffixes of malay
#use malaysiawordnet.txt for malay dictionary

import re
import nltk
import time
import malaya
import pandas as pd


malaywords = open("malaysiawordnet.txt").read().splitlines()
vowels = ['a','e','i','o','u']

def replace_last(source_string, replace_what, replace_with):
    head, _sep, tail = source_string.rpartition(replace_what)
    return head + replace_with + tail



def m_Prefix(text):
    if (text[:6] =='memper'):
        stemmed = text[6:]
    elif (text[:4] =='meny'):
        stemmed = re.sub('meny', 's', text)
    elif (text[:4] =='meng'):
        if (text[4] == 'g' or text[4] == 'k' or text[4] == 'h'):
            stemmed = re.sub('meng', '', text)
        else:
            stemmed = re.sub('meng', 'k', text)   
    elif (text[:3] =='mem'):
        if text[3] == 'b':
            stemmed = re.sub('mem', '', text)
        else:
            stemmed = re.sub('mem', 'p', text)
    elif (text[:3] =='men'):
        if text[3] in vowels:
            stemmed = re.sub('men', 't', text)
        else:
            stemmed = re.sub('men', '', text)
    elif (text[:2] =='me'):
        stemmed = text[2:]
    else:
        stemmed = text
        
    temp = Suffix(stemmed)
    
    return Verify(temp, text)




def p_Prefix(text):
    if (text[:4]  =='peny'):
        stemmed = re.sub('peny', 's', text)
    elif (text[:4] =='peng'):
        if not text[4] in vowels:
            stemmed = re.sub('peng', '', text)
        else:
            stemmed = re.sub('peng', 'k', text)   
    elif (text[:3] =='pem'):
        if text[3] == 'b':
            stemmed = re.sub('pem', '', text)
        else:
            stemmed = re.sub('pem', 'p', text)
    elif (text[:3] =='pen'):
        if text[3] in vowels:
            stemmed = re.sub('pen', 't', text)
        else:
            stemmed = re.sub('pen', '', text)
    elif (text[:3] =='per'):
            stemmed = re.sub('per', '', text)
    elif (text[:2] =='pe'):
        stemmed = text[2:]
    else:
        stemmed = text
   

    temp = Suffix(stemmed)
    
    return Verify(temp, text)



def di_Prefix(text):
    stemmed = text[2:]
    
    temp = Suffix(stemmed)
    
    return Verify(temp, text)  

def ke_Prefix(text):
    if (text[-2] + text[-1] =='an'):
        stemmed = text[2:-2]
    else:
        stemmed = text[2:]
    
    return Verify(stemmed, text)  

def ter_Prefix(text):
    stemmed = text[3:]
    
    temp = Suffix(stemmed)
    
    return Verify(temp, text) 

def ber_Prefix(text):
    stemmed = text[3:]
    
    temp = Suffix(stemmed)
    
    return Verify(temp, text) 



def Suffix(stemmed):
    try:
        if (stemmed[-3] + stemmed[-2] + stemmed[-1] =='kan'):
            temp = stemmed[:-3]
        elif (stemmed[-3] + stemmed[-2] + stemmed[-1] =='nya'):
            temp = stemmed[:-3]
        elif (stemmed[-2] + stemmed[-1] =='an'):
            temp = stemmed[:-2]
        elif stemmed[-1] == 'i' and len(stemmed)>4:
            temp = replace_last(stemmed, 'i', '')
        #nya
        else:
            temp = stemmed
    except:
        temp = stemmed
    
        
    return temp



#verify whether stemmed word exists in malay dictionary
def Verify(temp, text):
    if (temp in malaywords and len(temp)>3):
        stemmed = temp
    else:
        stemmed = text
        
    return stemmed


