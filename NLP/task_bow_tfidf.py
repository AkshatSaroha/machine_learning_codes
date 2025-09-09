from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

documents = [
    "I love programming in Python",
    "Python is a great programming language",
    "I love to code in Python",
    "Python programming is amazing",
    "I am learning Python programming"
]

print('BOW box:')
vectorise = CountVectorizer()
vectorise_doc = vectorise.fit_transform(documents)

vectorise_doc_array = vectorise_doc.toarray()

print('Feature name(words): ', vectorise.get_feature_names_out())
print('Bag of words matrix(word counts)\n', vectorise_doc_array)

print('\nTF_IDF:')
tf_idf = TfidfVectorizer()
tf_idf_doc = tf_idf.fit_transform(documents)

tf_idf_doc_array = tf_idf_doc.toarray()

print('\nFeature name(words): ', tf_idf.get_feature_names_out())
print('TF_IDF_vectoriser:\n', tf_idf_doc_array)