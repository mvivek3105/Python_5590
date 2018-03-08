from nltk.tokenize import sent_tokenize, word_tokenize; from nltk.stem import WordNetLemmatizer
fw = open('prob3.txt','w'); fw.write('Vivek pursuing masters in UMKC. \n'); fw.write('Loves movies and cricket. \n');fw.close(); fr = open("prob3.txt","r")
text = fr.read() ; print(text) ; fr.close()
print(sent_tokenize(text))
words = word_tokenize(text)
print(words)
lemmatizers = ['NOUN LEMMATIZER', 'VERB LEMMATIZER']
lemmatizer_wordnet = WordNetLemmatizer()

formatted_row = '{:>24}' * (len(lemmatizers) + 1)
print('\n', formatted_row.format('WORD', *lemmatizers), '\n')
for word in words:
    lemmatized_words = [lemmatizer_wordnet.lemmatize(word, pos ='n'),
                        lemmatizer_wordnet.lemmatize(word, pos = 'v')]
    print(formatted_row.format(word, *lemmatized_words))
print("******************** bigrams************************")
from nltk.util import ngrams
bigrams= list(ngrams(words,2))
print(bigrams)
import nltk
frequent_bigram = nltk.FreqDist(bigrams)
a = frequent_bigram.most_common(5)
print(" 5 bigrams in the given list  are\n",a)
concaten = ""
for i in a:
    p = i[0][0]
    q = i[0][1]
    with open('prob3.txt',encoding = "utf-8")as f:
        for line in f.readlines():
            words = line.strip().split()
            for word1,word2 in zip(words,words[1:]):
                if word1==p and word2==q:
                    concaten = concaten + line
print(concaten)
