# CourseProject

## Domain-specific Keyword extraction (Vedant-vedantj2)
Using the SpaCy library, I created a python script(keyword_extraction.py) which can take data and labels as text and run keyword extraction using the label and data provided for any user input sentence. Libraries needed: spacy, pandas. 

pip install spacy/pandas. random library comes with python. 

### Run the file
Run by typing "python keyword_extraction.py" in the terminal after going into the folder where file exists 

Enter the number of iterations 

Model Name should ALWAYS be 'ner'; Added modifiable model name so future updates can use other models 

Enter sample sentence, gives keyword and keywork type /n



# Project Subtopic: Display Parse Tree using NLTK 
## Implemented by: Sagar Dalwadi (sagardd2) 
### Github Link: https://github.com/assalupitudor/CourseProject.git
### Program code file: nltk_parse_tree.py
### Program Input data: ParseTree_InputData
### Program Output: Screenshots named – nltk_pt_ss1 to nltk_pt_ss4
### Project Presentation Demo link (only parse tree): https://drive.google.com/file/d/1aq4-yEF0332KZ0w24pvII4G4_aXx_1k-/view?usp=sharing

### You can also find the documentation in a word format in this Git repository named as NLTK_Parse Tree_Project Documentation.docx


### 1) An overview of the function of the code (i.e., what it does and what it can be used for). 

Background context for a Project topic:

What is Syntax?
A natural language typically follows a hierarchical structure, and contains the following components: 
 
•	Sentences
•	Clauses
•	Phrases
•	Words

Syntax refers to the set of rules, principles, processes that govern the structure of sentences in a natural language. One basic description of syntax is how different words such as Subject, Verbs, Nouns, Noun Phrases, etc. are sequenced in a sentence.

Some of the syntactic categories of a natural language are as follows:

•	Sentence(S)
•	Noun Phrase(NP)
•	Determiner(Det)
•	Verb Phrase(VP)
•	Prepositional Phrase(PP)
•	Verb(V)
•	Noun(N)

Syntax Tree: 
A Syntax tree or a parse tree is a tree representation of different syntactic categories of a sentence. It helps us to understand the syntactical structure of a sentence.

Objective (What it does):
•	I have implemented a python program using NLTK library to display a parse tree for a given sentence in English that helps visualize the syntactic structure of a sentence. 
•	The program imports an NLTK toolkit into python and uses the pre-defined libraries to extract the syntactic categories from a sentence, print these categories and finally display a parse tree for the sentence. 

Purpose (What it can be used for):

This can be used as: 
•	An independent python program in your application extending your application need to either display a parse tree for the input data it’s receiving from its upstream or extracting the syntactic categories of a sentence in your NLP specific application to further apply other NLP techniques.
•	Can be converted into a python function that can be incorporated into python bindings of MeTA (metapy) and act as an extension to the MeTA library for NLP.

### 2) Documentation of how the software is implemented with sufficient detail so that others can have a basic understanding of your code for future extension or any further improvement. 

•	My program is implemented using an open source toolkit available to build python programs called Natural language Toolkit (NLTK). It provides easy to use interfaces and suite of text processing libraries for different NLP techniques.
•	First import required libraries corresponding to the function of the application along with nltk library
•	NLTK provides set of default datasets available that can be imported for the use in your application. These datasets can be downloaded using nltk.download function.
•	In order to use functions within NLTK, import the required libraries
•	At this step an input is required for your program. I have declared a variable to provide a sentence for which parse tree is to be displayed. You can also integrate directly with a front-end application that provides an input data or read the input data from a file as well.
•	Now use the functions available from NLTK library to extract the different syntactic categories from a sentence and then print these categories as well as display a parse tree.
•	As a further enhancement to this program these categories can be provided as an input to your software for the next steps of NLP.



### 3) Documentation of the usage of the software including either documentation of usages of APIs or detailed instructions on how to install and run a software, whichever is applicable. 

•	First of all, ensure you have python as well as NLTK installed on your system. Below are the instructions on how to install NLTK:

NLTK requires Python versions 3.6, 3.7, 3.8, or 3.9

Mac/Unix :
   1.	Install NLTK: run sudo pip install -U nltk
   2.	Install Numpy (optional): run sudo pip install -U numpy
   3.	Test installation: run python then type import nltk

Windows :
   1.	Install Numpy (optional): http://sourceforge.net/projects/numpy/files/NumPy/ (the version that specifies pythnon3.5)
   2.	Install NLTK: http://pypi.python.org/pypi/nltk
   3.	Test installation: Start>Python35 , then type import nltk

•	You can setup python virtual environments if you want to run this program
•	Below are the steps in order to run the program:

   1.	First, provide an input sentence for which you would like to display a parse tree. Open a program in python editor and update/provide your sentence in the variable text_sentence.
   2.	Go to terminal and execute the command python3 nltk_parse_tree.py
   3.	Once the program is executed successfully it would open a new nltk window and display the parse tree for the sentence provided as an input.


### 4) Brief description of contribution of each team member in case of a multi-person team. 

Our project proposal included 2 different subtopics for system extension to implement keyword extraction using SpaCy as well as display parse tree using NLTK.

•	To distribute the work among the team members, we have divided based on the subtopics of the project.
•	I have contributed towards the subtopic of displaying a parse tree using NLTK and end to end implementation of python program corresponding to this subtopic.

# Keyword Extraction: Implemented by Sindhu Kopparam(sgk6)

The main purpose of a keyword extraction function is to help us in identifying the important keywords. Extracting specific keywords from a chunk of text will make it easier for the user to decide whether they want to read that article, social media comment, reviews, etc. Analyzing the unstructured text and choosing what to select is made easier by keyword extraction. For this project, we are implementing a function that takes a chunk of text as an input and extracts the specified POS tags (Noun, Verb, Adjective, etc.) as an output. 

Implementing this function in MeTA will enhance the library and allow users to extract keywords effectively. Let’s look at the set up and the implementation of this function using SpaCy library.

## Setup:

1.	Install the spaCy module via the pip install.
*pip install -U spacy*
2.	Next step would be to download the English model. We are using small English model for simplicity reason. Download “en_core_eng_sm”
*python -m spacy download en_core_web_sm*
3.	Run the following command to validate if spaCy is working properly.
*python -m spacy validate*

## Implementation:

•	We will firstly import the libraries needed to implement this function. One library essential for this implementation would be spaCy as we are using its language model for text extraction.Apart from spaCy another library needed would be punctuation that contains the most commonly used punctuation.
*import spacy*
*from string import punctuation*

•	We can now load the language model that is downloaded using the below command.
*nlp = spacy. load(“en_core_Web_sm”)*

•	We can now write a function extract_keywords for the keyword extraction that can be easily called anywhere when we need to extract keywords from a chunk of text. This function will accept a string as an input parameter.

•	The output is stored as a list containing all the keywords extracted. We will create another list “pos_tag” that contains the part of speech tags that we want to be extracted. I have chosen Noun (NOUN), Adjective (ADJ) and Verb (VERB) in the above code but this can be customized to our requirement.

•	Next step is tokenization. The input text is converted into lowercase and tokenized via the spacy model. This is stored in an object doc. This object contains token objects from the tokenization process.

•	The next step would be to identify any stopwords or punctuation in the tokenized text. For this purpose, we can loop over each of the token and ignore if any stopwords or punctuation is part of the text. Move on to the next if it is not.

•	We will finally store the output if it contains the pos tags of the tokenized text that we have mentioned above.

•	Return the output as a list of strings.

•	Let’s test the above code by using a sample text. 

*sample_output = extract_keywords (‘This program will extract keywords from the input document and print all the nouns, adjectives and verbs.’)*

The output will look like this:
['program', 'will', 'extract', 'keywords', 'input', 'document', 'print', 'all', 'nouns', 'adjectives', 'verbs']

•	There is also an option for the user to enter text of their choice which will then be served as an input for the keyword function to extract the words.
