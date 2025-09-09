import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('punkt_tab')
nltk.download('stopwords')

text = 'I am learning natural language processing in a fun and exciting way !'
text2 = "Studying machine learning and deep learning is exciting and challenging at the same time."

# step 1: Tokenization
tokens = word_tokenize(text2)
print('Tokens: ', tokens)

# step 2: Remove stop words
stop_words = set(stopwords.words('english'))
filtered = [word for word in tokens if word.lower() not in stop_words]
print('After removing stop words: ', filtered)

# step 3: stemming
stemmer = PorterStemmer()
stemmed = [stemmer.stem(word) for word in filtered]
print('After stemming', stemmed)
