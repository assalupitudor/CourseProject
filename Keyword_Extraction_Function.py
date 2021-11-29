import spacy
from string import punctuation

#loading the english core language model(small)
nlp = spacy.load("en_core_web_sm")

def extract_keywords(string):
    output = []
    """
    list containing the part of speech tag that we want to extract. 
    We are extracting noun, adjective and verb in this program.
    This can be customized according to our requirement. 
    """
    pos_tag = ['NOUN','ADJ','VERB']

    """tokenize the input text"""
    doc = nlp(string.lower())

    for token in doc:
        """
        Looping over each of the token and checking if the tokenized text is part of the stopwords or punctuation. 
        We will ignore the token if it is and move on to the next token.
        """
        if (token.string in nlp.Defaults.stop_words or token.string in punctuation):
            continue

        """we will store the output if the pos tag of the tokenized text is the one we have mentioned above."""
        if (token.pos_ in pos_tag):
            output.append(token.text)

    """returning the output as a list of strings."""
    return output

#value = input("Enter your text: ")
#print(value)
#result = extract_keywords(value)
#print(result)

sample_output = extract_keywords('This program will extract keywords from the input document and print all the nouns, adjectives and verbs.')
print(sample_output)