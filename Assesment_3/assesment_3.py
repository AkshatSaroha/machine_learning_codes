import pandas as pd  
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# nltk.download('punkt')
# nltk.download('stopwords')

# loading dataset
df = pd.read_csv('new_customer_emails.csv')

# data preprocessing
def preprocessing(text):
    text = text.lower()
    text = ''.join(char for char in text if char.isalnum() or char.isspace()) # removing punctuations
    stop_words = set(stopwords.words('english'))
    words = text.split() 
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

df['cleaned_text'] = df['Email Text'].apply(preprocessing)

# vectorization (TF-IDF)
vectorizer = TfidfVectorizer()
x = vectorizer.fit_transform(df['cleaned_text'])
y = df['Category']

# split train/test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# model training
model = LogisticRegression()
model.fit(x_train, y_train)

# Evaluation
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

classification = classification_report(y_test, y_pred)
print('\nClassificaton report: ', classification)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(5,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("True")
plt.tight_layout()
plt.show()

# Show Predictions
# new_mails = pd.Dataframe({
#     'Email Text': {'I want to check the status of my insurance claim',
#                    'Please update my phone number in your records',
#                     'Can I get a copy of my current policy details?',
#                      'When will my claim be approved?',
#                       'My address has changed. Please update it.' 
#                     }

new_mails = pd.DataFrame({
    'Email Text': df.loc[y_test.index, 'Email Text'].values, # getting actual email from dataset
    'True Label': y_test.values,
    'Predicted Label': y_pred
})

# })
print("\nSample Predictions:")
print(new_mails.head(5))


# visualization
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='Category', palette='Set1')
plt.title('Category Distribution')
plt.xlabel('Category')
plt.ylabel('Number of Emails')
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

# Most frequent words per category
cv = CountVectorizer() 
x_counts = cv.fit_transform(df['cleaned_text'])
words = cv.get_feature_names_out()

top_words_df = pd.DataFrame(x_counts.toarray(), columns=words)
top_words_df['Category'] = df['Category']

for itr in df['Category'].unique(): # iterating in each category
    category_df = top_words_df[top_words_df['Category'] == itr].drop(columns=['Category'])
    word_sums = category_df.sum().sort_values(ascending=False)[:10]
    
    plt.figure(figsize=(6,3))
    sns.barplot(x=word_sums.values, y=word_sums.index, palette='mako')
    plt.title(f"Top 10 Words in '{itr}' Emails")
    plt.xlabel('Frequency')
    plt.ylabel('Words')
    plt.tight_layout()
    plt.show()

# Word Clouds per Category
for itr in df['Category'].unique(): 
    text = ' '.join(df[df['Category'] == itr]['cleaned_text'])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    plt.figure(figsize=(8,4))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f"Word Cloud for {itr}")
    plt.tight_layout()
    plt.show()