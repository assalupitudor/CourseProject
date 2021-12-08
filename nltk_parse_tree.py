#Import required libraries in your program

import nltk
#import ssl

# NLTK provides set of default datasets that can be imported to your program depending on the need
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

from nltk import pos_tag, word_tokenize, RegexpParser

#Provide your sentence that you would like to display parse tree for

text_sentence = "This is a testing sentence to display a parse tree as part of demo."


#Find all parts of speech in above sentence
tagged = pos_tag(word_tokenize(text_sentence))


#Extract all parts of speech from any text
chunker = RegexpParser("""
					NP: {<DT>?<JJ>*<NN>} #To extract Noun Phrases
					P: {<IN>}			 #To extract Prepositions
					V: {<V.*>}			 #To extract Verbs
					PP: {<p> <NP>}		 #To extract Prepositional Phrases
					VP: {<V> <NP|PP>*}	 #To extract Verb Phrases
					""")


#Print all parts of speech in above sentence
output = chunker.parse(tagged)
print("After Extracting\n", output)


#Display the parts tagged above as a parse tree
output.draw()


