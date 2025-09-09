# from sklearn.feature_extraction.text import CountVectorizer # words into numbers
# from sklearn.naive_bayes import MultinomialNB # categorization

# texts = ['I love this','I hate that', 'This is awesome', 'This is awful']
# labels = ['positive', 'negative', 'positive', 'negative']

# vectorizer = CountVectorizer()
# x = vectorizer.fit_transform(texts)# converting sentence into list of words

# model = MultinomialNB()
# model.fit(x, labels)

# text = ['I am love it', 'This is very awful']
# xtext = vectorizer.transform(text)

# predictions = model.predict(xtext)
# print(list(zip(text, predictions)))

# # converting = fit_transform and transform = ?


from sklearn.feature_extraction.text import CountVectorizer # words into numbers
from sklearn.naive_bayes import MultinomialNB # categorization

texts = [
    "I love this game",
    "This is amazing",
    "I feel so happy today",
    "This is awful",
    "I hate this",
    "I am really sad",
    "It was a great day",
    "I don’t like it",
    "This is terrible",
    "I feel fantastic!"
]
labels = ['positive', 'positive', 'positive',
           'negative', 'negative', 'negative',
           'positive', 'negative', 'negative', 'positive']

vectorizer = CountVectorizer()
x = vectorizer.fit_transform(texts)# converting sentence into list of words

model = MultinomialNB()
model.fit(x, labels)

test_sentences = [
    "I really love it",
    "This is the worst",
    "What a wonderful day",
    "I am not happy with this",
    "It makes me sad"
]
xtext = vectorizer.transform(test_sentences)

predictions = model.predict(xtext)
print('\n')
print(list(zip(test_sentences, predictions)),'\n')
