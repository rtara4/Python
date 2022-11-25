import random
inspirational_quote = []
f = open('inspirationalquotes.txt','rt')
for quote in f:
    inspirational_quote.append(quote)
f.close()
print('inspirational quote of the day')
print(random.choice(inspirational_quote))
    