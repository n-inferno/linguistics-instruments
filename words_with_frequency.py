import sys
import string
from collections import Counter, OrderedDict

args = sys.argv

"""arguments processing"""
filename = sys.argv[1]
if len(args) == 3:
    try:
        limit = int(args[2])
    except:
        stopwords = args[2]
        limit = 0
    else:
        stopwords = None
elif len(args) == 4:
    stopwords = args[2]
    limit = int(args[3])
else:
    stopwords = None
    limit = 0

"""main func"""
def words_with_frequency(filename, stopwords=None, limit=0):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read().split()

    for word_ind in range(len(text)):
        text[word_ind] = text[word_ind].strip().lower()
        text[word_ind] = text[word_ind].translate(str.maketrans('', '', string.punctuation))

    frequency = Counter(text)

    if stopwords:
        with open(stopwords, 'r', encoding='utf-8') as file:
            stoplist = file.read().split()

        frequency = {k: v for k, v in frequency.items() if k not in stoplist}

    try:
        del frequency['']
    except:
        pass

    frequency = OrderedDict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))

    with open('result.csv', 'w') as csvfile:
        for k, v in frequency.items():
            if v < limit:
                break
            csvfile.write('{},{}\n'.format(k, v))



if __name__ == '__main__':
    words_with_frequency(filename, stopwords, limit)
