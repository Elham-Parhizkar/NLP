from __future__ import print_function, division
from future.utils import iteritems
from builtins import range



# WHERE TO GET THE VECTORS:
# GloVe: https://nlp.stanford.edu/projects/glove/
# Direct link: http://nlp.stanford.edu/data/glove.6B.zip

import numpy as np
from sklearn.metrics.pairwise import pairwise_distances


def dist1(a, b):
    return np.linalg.norm(a - b)
def dist2(a, b):
    return 1 - a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))

# pick a distance type
dist, metric = dist2, 'cosine'
# dist, metric = dist1, 'euclidean'



def find_analogies(w1, w2, w3):
  for w in (w1, w2, w3):
    if w not in word2vec:
      print("%s not in dictionary" % w)
      return

  king = word2vec[w1]
  man = word2vec[w2]
  woman = word2vec[w3]
  v0 = king - man + woman

  distances = pairwise_distances(v0.reshape(1, D), embedding, metric=metric).reshape(V)
  idxs = distances.argsort()[:4]
  for idx in idxs:
    word = idx2word[idx]
    if word not in (w1, w2, w3): 
      best_word = word
      break

  print(w1, "-", w2, "=", best_word, "-", w3)


def nearest_neighbors(w, n=5):
  if w not in word2vec:
    print("%s not in dictionary:" % w)
    return

  v = word2vec[w]
  distances = pairwise_distances(v.reshape(1, D), embedding, metric=metric).reshape(V)
  idxs = distances.argsort()[1:n+1]
  print("neighbors of: %s" % w)
  for idx in idxs:
    print("\t%s" % idx2word[idx])



# load in pre-trained word vectors
print('Loading word vectors...')
word2vec = {}
embedding = []
idx2word = []
with open('glove.6B.50d.txt', encoding='utf-8') as f:
  # is just a space-separated text file in the format:
  # word vec[0] vec[1] vec[2] ...
  for line in f:
    values = line.split()
    word = values[0]
    vec = np.asarray(values[1:], dtype='float32')
    word2vec[word] = vec
    embedding.append(vec)
    idx2word.append(word)
print('Found %s word vectors.' % len(word2vec))
embedding = np.array(embedding)
V, D = embedding.shape


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


nearest_neighbors('king')
nearest_neighbors('france')
nearest_neighbors('japan')
nearest_neighbors('einstein')
nearest_neighbors('woman')
nearest_neighbors('nephew')
nearest_neighbors('february')
nearest_neighbors('rome')
