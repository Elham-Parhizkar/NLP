from __future__ import print_function, division
from future.utils import iteritems
from builtins import range



from gensim.models import KeyedVectors


# warning: takes quite awhile
# https://code.google.com/archive/p/word2vec/
# direct link: https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?usp=sharing
# 3 million words and phrases
# D = 300
word_vectors = KeyedVectors.load_word2vec_format(
  '../large_files/GoogleNews-vectors-negative300.bin',
  binary=True
)



def find_analogies(w1, w2, w3):
  r = word_vectors.most_similar(positive=[w1, w3], negative=[w2])
  print("%s - %s = %s - %s" % (w1, w2, r[0][0], w3))

def nearest_neighbors(w):
  r = word_vectors.most_similar(positive=[w])
  print("neighbors of: %s" % w)
  for word, score in r:
    print("\t%s" % word)


find_analogies('king', 'man', 'woman')
find_analogies('france', 'paris', 'london')
find_analogies('france', 'paris', 'rome')
find_analogies('paris', 'france', 'italy')
find_analogies('france', 'french', 'english')
find_analogies('japan', 'japanese', 'chinese')
find_analogies('japan', 'japanese', 'italian')
find_analogies('japan', 'japanese', 'australian')
find_analogies('december', 'november', 'june')
find_analogies('miami', 'florida', 'texas')
find_analogies('einstein', 'scientist', 'painter')
find_analogies('china', 'rice', 'bread')
find_analogies('man', 'woman', 'she')

nearest_neighbors('king')
nearest_neighbors('france')
nearest_neighbors('japan')
nearest_neighbors('einstein')
nearest_neighbors('woman')
nearest_neighbors('nephew')
nearest_neighbors('february')
nearest_neighbors('rome')
