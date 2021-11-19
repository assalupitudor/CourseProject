import spacy 
import pandas as pd
import random
import re
from spacy.lang.en import English


file_path = 'some_path.txt'
file = open(file_path, 'r')
doc = file.read()

word_dict = {} #initialize this with labels

#using eglish words create sentencizer to process the document/file
process = English()
process.add_pipe(process.create_pipe('sentencizer')) 
doc = process(doc)
sentences = [sentence.string.strip() for sentence in doc.sents]

data = []
#corpus builder
for sentence in sentences:
    #replace
    word_list = re.sub("[^\w]", " ",  sentence).split()
    for word in word_list:
        d = {}
        l = []
        if word in word_dict:
            start_word = sentence.find(word)
            end_word = start_word+len(word)
            label = word_dict.get(word)
            list_t = (start_word,end_word,label)
            l.append(list_t)
            d['entities'] = l
            data_t = (sentence,d)
            data.append(data_t)

#TRAIN_DATA = outer_list
print(data)

def train():
    #create a blank language class
    nlp = spacy.blank('en')