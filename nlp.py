
#**********************************************************###

"""from nltk import *
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


text = open("Data/sampletext.txt", "r+")
myText=text.read()
array_wordTokenize=word_tokenize(myText) #Word Tokenizing
array_sentTokenize=sent_tokenize(myText) #Sentence Tokenizing
stop_words=set(stopwords.words("english"))
array_stopFiltered=[]                    #Stop Words Filtered
for w in array_wordTokenize:
 if w not in stop_words:
  array_stopFiltered.append(w)
ps=PorterStemmer()
stemmed_list=[]                          #List of stemmed words
for w in array_wordTokenize:
 stemmed_list.append(ps.stem(w))
"""


###*************************************************##########


###**************Part of Speech Tagging*********************###

"""   
Part of Speech Tagging with NLTK




One of the more powerful aspects of the NLTK module is the Part of Speech tagging that it can do for you. This means labeling words in a sentence as nouns, adjectives, verbs...etc. Even more impressive, it also labels by tense, and more. Here's a list of the tags, what they mean, and some examples:

POS tag list:

CC	coordinating conjunction
CD	cardinal digit
DT	determiner
EX	existential there (like: "there is" ... think of it like "there exists")
FW	foreign word
IN	preposition/subordinating conjunction
JJ	adjective	'big'
JJR	adjective, comparative	'bigger'
JJS	adjective, superlative	'biggest'
LS	list marker	1)
MD	modal	could, will
NN	noun, singular 'desk'
NNS	noun plural	'desks'
NNP	proper noun, singular	'Harrison'
NNPS	proper noun, plural	'Americans'
PDT	predeterminer	'all the kids'
POS	possessive ending	parent's
PRP	personal pronoun	I, he, she
PRP$	possessive pronoun	my, his, hers
RB	adverb	very, silently,
RBR	adverb, comparative	better
RBS	adverb, superlative	best
RP	particle	give up
TO	to	go 'to' the store.
UH	interjection	errrrrrrrm
VB	verb, base form	take
VBD	verb, past tense	took
VBG	verb, gerund/present participle	taking
VBN	verb, past participle	taken
VBP	verb, sing. present, non-3d	take
VBZ	verb, 3rd person sing. present	takes
WDT	wh-determiner	which
WP	wh-pronoun	who, what
WP$	possessive wh-pronoun	whose
WRB	wh-abverb	where, when
"""

"""
import nltk
#from nltk.tokenize import PunktSentenceTokenizer
from nltk import *

text = open("Data/sampletext.txt", "r+")
myText=text.read()
#custom_sent_tokenizer=PunktSentenceTokenizer(train_text)
array_sentTokenize=sent_tokenize(myText)

def process_content():
 try:
  for i in array_sentTokenize:
   words=word_tokenize(i)
   tagged=nltk.pos_tag(words)
   print(tagged)
 except Exception as e:
  print(str(e))

process_content()
"""
###**********************************************###########


###**********Chunking**************************************###

"""
import nltk
#from nltk.tokenize import PunktSentenceTokenizer
from nltk import *

text = open("Data/sampletext.txt", "r+")
myText=text.read()
#custom_sent_tokenizer=PunktSentenceTokenizer(train_text)
array_sentTokenize=sent_tokenize(myText)

def process_content():
 try:
  for i in array_sentTokenize:
   words=word_tokenize(i)
   tagged=nltk.pos_tag(words)
   chunkGram=r"""#Chunk: {<RB.?>*<VB.?>*<NNP><NN>?}"""
"""ChunkParser=nltk.RegexpParser(chunkGram)
   chunked=ChunkParser.parse(tagged)
   #print(chunked)
   chunked.draw()
 except Exception as e:
  print(str(e))

process_content()
"""

###*****************************************################



###########Chinking########################################


"""
Here is a quick cheat sheet for various rules in regular expressions:

Identifiers:

    \d = any number
    \D = anything but a number
    \s = space
    \S = anything but a space
    \w = any letter
    \W = anything but a letter
    . = any character, except for a new line
    \b = space around whole words
    \. = period. must use backslash, because . normally means any character.

Modifiers:

    {1,3} = for digits, u expect 1-3 counts of digits, or "places"
    + = match 1 or more
    ? = match 0 or 1 repetitions.
    * = match 0 or MORE repetitions
    $ = matches at the end of string
    ^ = matches start of a string
    | = matches either/or. Example x|y = will match either x or y
    [] = range, or "variance"
    {x} = expect to see this amount of the preceding code.
    {x,y} = expect to see this x-y amounts of the precedng code

White Space Charts:

    \n = new line
    \s = space
    \t = tab
    \e = escape
    \f = form feed
    \r = carriage return

Characters to REMEMBER TO ESCAPE IF USED!

    . + * ? [ ] $ ^ ( ) { } | \

Brackets:

    [] = quant[ia]tative = will find either quantitative, or quantatative.
    [a-z] = return any lowercase letter a-z
    [1-5a-qA-Z] = return all numbers 1-5, lowercase letters a-q and uppercase A-Z

"""




"""
import nltk
#from nltk.tokenize import PunktSentenceTokenizer
from nltk import *

text = open("Data/sampletext.txt", "r+")
myText=text.read()
#custom_sent_tokenizer=PunktSentenceTokenizer(train_text)
array_sentTokenize=sent_tokenize(myText)

def process_content():
 try:
  for i in array_sentTokenize:
   words=word_tokenize(i)
   tagged=nltk.pos_tag(words)
   chunkGram=r"""#Chunk: {<.*>+}
                         #}<VB.?|IN|DT>+{"""
"""ChunkParser=nltk.RegexpParser(chunkGram)
   chunked=ChunkParser.parse(tagged)
   print(chunked)
   #chunked.draw()
 except Exception as e:
  print(str(e))

process_content()
"""



###****************************************##################




####********NAME ENTITY RECOGNITION*****************#########



"""

NE Type and Examples
ORGANIZATION - Georgia-Pacific Corp., WHO
PERSON - Eddy Bonte, President Obama
LOCATION - Murray River, Mount Everest
DATE - June, 2008-06-29
TIME - two fifty a m, 1:30 p.m.
MONEY - 175 million Canadian Dollars, GBP 10.40
PERCENT - twenty pct, 18.75 %
FACILITY - Washington Monument, Stonehenge
GPE - South East Asia, Midlothian


"""

"""

import nltk
#from nltk.tokenize import PunktSentenceTokenizer
from nltk import *

text = open("Data/sampletext.txt", "r+")
myText=text.read()
#custom_sent_tokenizer=PunktSentenceTokenizer(train_text)
array_sentTokenize=sent_tokenize(myText)

def process_content():
 try:
  for i in array_sentTokenize:
   words=word_tokenize(i)
   tagged=nltk.pos_tag(words)
   namedEnt=nltk.ne_chunk(tagged,binary=True)
   print(namedEnt)
 except Exception as e:
  print(str(e))

process_content()


"""


#########************************************###############




#######*************LEMMATIZING****************############


"""
from nltk.stem import WordNetLemmatizer
from nltk import *


text = open("Data/sampletext.txt", "r+")
myText=text.read()
lemmatizer = WordNetLemmatizer()
words=word_tokenize(myText)

for i in words:
 print(lemmatizer.lemmatize(i))

"""


##########***************************************##############

