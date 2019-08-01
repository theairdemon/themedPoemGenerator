import nltk


text = 'Now love, shine. And so, the love will inflame'
text = nltk.word_tokenize(text)
result = nltk.pos_tag(text)
result = [i for i in result if i[0].lower() == 'love']

print(result) # [('table', 'JJ'), ('table', 'VB'), ('table', 'NN')]

