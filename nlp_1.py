import pandas as pd
from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather."


blob = TextBlob(text)
print(blob)
'''
""" TOKENIZATION """
print(blob.sentences)
print(blob.words)
print(type(blob.words))
print(blob.tags)
print(blob.noun_phrases)
print(
    blob.sentiment
)  # gives us a sentiment object which gives us polarity and subjectivity
# -1 is negative and +1 is positive
# is the statement subjective or objective; higher number equals more subective.
print(round(blob.sentiment.polarity, 2))
print(round(blob.sentiment.subjectivity, 2))

sentences = blob.sentences

for sentence in sentences:
    print(sentence)
    print(sentence.sentiment)
    print(round(sentence.sentiment.polarity, 3))
'''

########                   #########
""" Changing the analyzer we use """
########                   #########

from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

# print(blob.sentiment)

# print(blob.detect_language())

german = blob.translate(to="de")
print(german)
spanish = blob.translate(to="es")
print(spanish)
french = blob.translate(to="fr")
print(french)

from textblob import Word

index = Word("index")

print(index.pluralize())

cacti = Word("cacti")

print(cacti.singularize())

animals = TextBlob("dog cat fish bird").words

print(animals.pluralize())

word = Word("theyr")

print(word.spellcheck())

corrected_word = word.correct()

print(corrected_word)

sentence = TextBlob("Ths sentnce has misspeled wrds.")
corrected_sentence = sentence.correct()

print(corrected_sentence)

#############

word1 = Word("studies")
word2 = Word("varieties")

print(word1.lemmatize())
print(word2.lemmatize())

happy = Word("happy")
print(happy.definitions)

for synset in happy.synsets:
    print(synset)
    for lemma in synset.lemmas():
        print(lemma)
        print(lemma.name())


lemmas = happy.synsets[0].lemmas()

for lemma in lemmas[0].antonyms():
    print(lemma.name())


# delete "stop" words - which are filler/ supplemental to the actual text we are analyzing
import nltk

nltk.download("stopwords")

from nltk.corpus import stopwords

stops = stopwords.words("english")

print(stops)
print()
print()

blob = TextBlob("today is a beautiful day.")
cleanlist = [word for word in blob.words if word not in stops]
print(cleanlist)
# we cleaned out the statement "today is a beautiful day" by removing any word from stops
# stops is a list of the stopwords