import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt


# read data
df = pd.read_csv('imdb_data.csv')

# features and target
x = df['review']
y = df['label']

vectorizer = CountVectorizer(stop_words='english')
x_vectorized = vectorizer.fit_transform(x) # converting sentence into list of words(bag of words)

# Split into train and test 
x_train, x_test, y_train, y_test = train_test_split(x_vectorized, y, test_size=0.2, random_state=42)

# # Train a Naive Bayes model
# model = MultinomialNB()
# model.fit(x_train, y_train)

# Train using Logistic regression
model = LogisticRegression()
model.fit(x_train, y_train)

# evaluate
y_pred = model.predict(x_test)
print('Accuracy: ', accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Test Predictions
test_reviews = [
    "The movie was bad.",
    "The movie was good."
]
x_test = vectorizer.transform(test_reviews)

# Predict
test_predictions = model.predict(x_test)

for review, label in zip(test_reviews, test_predictions):
    sentiment = "Positive" if label == 1 else "Negative"
    print(f"Review: \"{review}\" -> Sentiment: {sentiment}")

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=["Negative", "Positive"], yticklabels=["Negative", "Positive"])
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.show()

# 2. Basic visualization: Count of positive and negative reviews
plt.figure(figsize=(5, 3))
df['label'].value_counts().plot(kind='bar', color=['red', 'green'])
plt.title("Label Counts: 0=Negative, 1=Positive")
plt.xlabel("Sentiment Label")
plt.ylabel("Count")
plt.xticks(ticks=[0,1], labels=["Negative", "Positive"], rotation=0)
plt.tight_layout()
plt.show()