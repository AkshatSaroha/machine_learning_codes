from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    'I love programming in Python',
    'Python is a great programming language',
    'I love coding in python'
]

tf_idf_vectorizer = TfidfVectorizer()

x_tfIdf = tf_idf_vectorizer.fit_transform(documents)

x_tfIdf_array = x_tfIdf.toarray()

print('Feature name(words): ', tf_idf_vectorizer.get_feature_names_out())
print('TF_IDF_vectoriser:\n', x_tfIdf_array)