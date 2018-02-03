a = input("ENTER YOUR SENTENCE")
d = a.split(" ")
print(d)
if len(d)%2 == 0:
    print("Middle words are")
    print( d[int(len(d)/2)], d[int(len(d)/2 - 1)] )
else:
    print("Middle word is")
    print(d[int(len(d)//2)])
def revSen(Sentence):
    words = Sentence.split(" ")
    newWords = [word[::-1] for word in words]
    newSentence = " ".join(newWords)
    return newSentence
def Lar_word(Sentence):
    pool = Sentence.split()
    pool.sort(key=len)
    return pool[-1]
Sentence = input("Enter anything")
print("Reverse:",revSen(Sentence))
print("Largest Word:",Lar_word(Sentence))













