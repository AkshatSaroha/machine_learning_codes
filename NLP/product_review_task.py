# Objective:
# The goal of this task is to build a sentiment analysis model that classifies product reviews into positive or negative sentiment categories based on the review content. This task will involve common NLP techniques like text cleaning, tokenization, stopword removal, and TF-IDF feature extraction, along with training a classifier model.
 
# Task Steps:
# Step 1: Load the Dataset
# 	You will be provided with a CSV file containing product reviews and their sentiment labels (positive or negative).
 
# Step 2: Preprocess the Text
# 	Convert text to lowercase.
# 	Remove special characters, numbers, and unnecessary spaces.
# 	Tokenize the text into words (split the text into individual words).
# 	Remove stopwords using an NLP library like nltk to focus on the more meaningful words.
 
# 	Apply stemming or lemmatization to simplify words (e.g., “running” becomes “run”).
 
# Step 3: Feature Extraction
# 	Convert the cleaned text into numerical features using TF-IDF (Term Frequency-Inverse Document Frequency), which weighs the importance of words in the document relative to the entire dataset.
 
# Step 4: Model Training
# 	Train a Logistic Regression or Naive Bayes classifier on the features extracted from the text data. These models are commonly used for text classification tasks.
 
# Step 5: Model Evaluation
# 	Evaluate your model using accuracy (how many reviews were classified correctly).
# 	Generate a confusion matrix to show how well the model distinguishes between positive and negative reviews.
 
# Step 6: Make Predictions
# 	Test the model on some new product reviews and predict whether they are positive or negative.

# import pandas as pd
# import nltk
# import re
# from nltk.tokenize import word_tokenize
# import matplotlib.pyplot as plt
# from nltk.corpus import stopwords
# from nltk.stem import PorterStemmer
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

# nltk.download('punkt')
# nltk.download('stopwords')

# # load data
# df = pd.read_csv('product_review.csv')

# review_data = df['review']

# # remove special chars
# review_data = re.sub(r'[^a-z\s]', '', review_data)

# # tokenization
# tokens = word_tokenize(review_data)

# # Remove stop words
# stop_words = set(stopwords.words('english'))
# filtered = [word for word in tokens if word.lower() not in stop_words]

# # stemming
# stemmer = PorterStemmer()
# cleaned_data = [stemmer.stem(word) for word in filtered]

# # Step 3: Feature Extraction (TF-IDF)
# vectorizer = TfidfVectorizer()
# x = vectorizer.fit_transform(cleaned_data)
# y = df['sentiment']

# # step 4: model training
# x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

# model = LogisticRegression()
# model.fit(x_train, y_train)

# # evaluation
# y_pred = model.predict(x_test)
# accuracy = accuracy_score(y_test, y_pred)
# print('\nAccuracy: ', accuracy)

# # confusion matrix
# cm = confusion_matrix(y_test, y_pred, labels=['positive', 'negative'])
# display = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['positive', 'negative'])
# display.plot(cmap='Blues')
# plt.title("Confusion Matrix")
# plt.show()

# # make predictions 
# new_reviews = [
#     "The product exceeded my expectations.",
#     "Very bad quality. I'm disappointed.",
#     "Excellent quality and fast delivery.",
#     "It's not worth the money."
# ]

# x_new = vectorizer.transform(new_reviews)
# prediction = model.predict(x_new)

# for review, sentiment in zip(new_reviews, prediction):
#     print(f"\nReview: \"{review}\" => Sentiment: {sentiment}")


# ---------------------------------------------------------------------------------------------

import pandas as pd
import nltk
import re
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay, classification_report

# Download required NLTK data
# nltk.download('punkt')
# nltk.download('stopwords')

# Step 1: Load data
df = pd.read_csv('product_review.csv')
df.dropna(subset=['review'], inplace=True)  # Remove missing reviews

# Step 2: Text preprocessing function
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = word_tokenize(text)
    filtered = [word for word in tokens if word not in stop_words]
    stemmed = [stemmer.stem(word) for word in filtered]
    return ' '.join(stemmed)

# Apply preprocessing to each review
df['cleaned_review'] = df['review'].apply(preprocess_text)

# Step 3: TF-IDF Vectorization
vectorizer = TfidfVectorizer()
x = vectorizer.fit_transform(df['cleaned_review'])
y = df['sentiment']

# Step 4: Model training
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(x_train, y_train)

# Step 5: Evaluation
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print('\nAccuracy:', accuracy)

classification = classification_report(y_test, y_pred)
print('\nClassificaton report: ', classification)

cm = confusion_matrix(y_test, y_pred, labels=['positive', 'negative'])
display = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['positive', 'negative'])
display.plot(cmap='Blues')
plt.title("Confusion Matrix")
plt.show()

# Step 6: Predict new reviews
new_reviews = [
    "The product exceeded my expectations.",
    "Very bad quality. I'm disappointed.",
    "Excellent quality and fast delivery.",
    "It's not worth the money."
]

# Preprocess new reviews
cleaned_new = [preprocess_text(review) for review in new_reviews]
x_new = vectorizer.transform(cleaned_new)
prediction = model.predict(x_new)

for review, sentiment in zip(new_reviews, prediction):
    print(f"\nReview: \"{review}\" => Sentiment: {sentiment}")
