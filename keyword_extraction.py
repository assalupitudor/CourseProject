import spacy 
import pandas as pd
import random
import re
from spacy.lang.en import English
from spacy.training.example import Example

'''
Run by typing "python keyword_extraction.py"
Enter the number of iterations
Model Name should ALWAYS be 'ner'; Added modifiable model name so future updates can use other models
Enter sample sentence, gives keyword and keywork type
'''

def extract(file_path, label_path):
    file = open(file_path, 'r', encoding='cp1252')
    doc = file.read()
    # read the label data
    labels = pd.read_csv(label_path)
    word_dict = labels.set_index('entities')['labels'].to_dict() #initialize this with labels

    #using eglish words create sentencizer to process the document/file
    process = English()
    process.add_pipe('sentencizer') 
    doc = process(doc)
    sentences = [sentence.text.strip() for sentence in doc.sents]

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
    return data

def train(data, itr):
    #create a blank language class
    nlp = spacy.blank('en')
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe('ner', last=True)
    
    for _, annotations in data:
        for ent in annotations.get('entities'):
            ner.add_label(ent[2])
    
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  # only train NER
        optimizer = nlp.begin_training()
        for itn in range(itr):
            #print("Starting iteration " + str(itn))
            random.shuffle(data)
            losses = {}
            for text, annotations in data:
                
                doc = nlp.make_doc(text)
                
                expl = Example.from_dict(doc, annotations)
                nlp.update(
                    [expl],  # batch of Example objects
                    drop=0.2,  # dropout - make it harder to memorise data
                    sgd=optimizer,  # callable to update weights
                    losses=losses)
            #print(losses)
    return nlp


#Get number of iterations as input
data = extract('data.txt', 'labels.csv')
iterations_input = int(input("Enter number of iterations: "))
prdnlp = train(data, iterations_input)

# Save our trained Model
modelfile = input("Enter your Model Name: ")
prdnlp.to_disk(modelfile)

#Test your text
test_text = input("Enter your testing text: ")
doc = prdnlp(test_text)
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
spacy.displacy.render(doc, style="ent", page="true")