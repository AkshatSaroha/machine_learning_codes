from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

documents = [
    'Free lottery ticket, claim now',
    'Hey, How are you doing today ?',
    'Click here to get free meal',
    'Interview scheduled tomorrow 12 PM',
    'IMportant: Your account has been compormised'
]

# labels : 1 - spam, 0 - not spam
labels = [1,0,1,0,1]

# Convert text into numerical values
vectorizer = TfidfVectorizer(stop_words='english')
x = vectorizer.fit_transform(documents)

# split train and test
x_train, x_test, y_train, y_test = train_test_split(x, labels, test_size=0.3, random_state=42)

# train model
model = LogisticRegression()
model.fit(x_train, y_train)

# predict using trained model
y_pred = model.predict(x_test)

# evaluate
print('Classification report: \n', classification_report(y_test, y_pred))