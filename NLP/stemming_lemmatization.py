import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

# nltk.download('punkt') # for tokenization
# nltk.download('wordnet') # for lemmatizer

sentence = 'The cats are running towards the running cat.'
sentence_2 = 'The children were playing in the parks and having fun while the dogs were running happily.'

# tokenization
# tokens = word_tokenize(sentence_2.lower())
# print('Tokens: ', tokens)

# Stemming
stemmer = PorterStemmer()

# Lemmatization
lemmatizer = WordNetLemmatizer()

# apply stemming
# stemmed_words = [stemmer.stem(i) for i in tokens]
# print('\nStemmed words: ', stemmed_words)

# lemmatized_words = [lemmatizer.lemmatize(i) for i in tokens]
# print('\nLemmatised words: ', lemmatized_words)


words = ['running', 'better', 'easily', 'happier', 'swimming', 'studies', 'flying', 'worse', 'cats', 'geese']

print('Original words: ',words)

stemmed_words = [stemmer.stem(i) for i in words]
print('\nStemmed words: ', stemmed_words)

lemmatized_words = [lemmatizer.lemmatize(i) for i in words]
print('\nLemmatised words: ', lemmatized_words)