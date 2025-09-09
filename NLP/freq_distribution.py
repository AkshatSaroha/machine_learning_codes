# import nltk 
# from nltk.tokenize import word_tokenize
# from nltk.probability import FreqDist

# nltk.download('punkt')

# text = 'I love ice cream and pizza. Pizza is my favourite food and I love PIZZA!'
# text = text.lower()

# tokens = word_tokenize(text)
# print('\nTokens: ', tokens)

# fd = FreqDist(tokens)
# print('\nMost common words: ', fd.most_common(3))


import nltk 
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

nltk.download('punkt')

text = 'Chocolate ice cream is the best treat ever!'
text = text.lower()

tokens = word_tokenize(text)
print('\nTokens: ', tokens)

print('\nTotal number of tokens: ', len(tokens))

print('\nFirst word: ', tokens[0])

print('\nLast word: ', tokens[-1])
print('\n')