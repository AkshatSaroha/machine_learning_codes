from sklearn.feature_extraction.text import CountVectorizer

documents = [
    'I love programming in Python',
    'Python is a great programming language',
    'I love coding in python'
]

vectorize = CountVectorizer()

x = vectorize.fit_transform(documents)

x_array = x.toarray()

print('Feature name(words): ', vectorize.get_feature_names_out())
print('Bag of words matrix(word counts)\n', x_array)