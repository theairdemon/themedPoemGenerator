import numpy as np
import random
import re
from collections import defaultdict
import string

filename = "walt-whitman-poems.txt"

# Read text from file and tokenize.
with open(filename) as f:
    text = f.read()
tokenized_text = [
    word
    for word in re.split('\W+', text)
    if word != ''
]
 

# Create graph.
markov_graph = defaultdict(lambda: defaultdict(int))

last_word = tokenized_text[0].lower()
for word in tokenized_text[1:]:
  word = word.lower()
  markov_graph[last_word][word] += 1
  last_word = word

# Preview graph.
'''
limit = 3
for first_word in ('the', 'by', 'who'):
  next_words = list(markov_graph[first_word].keys())[:limit]
  for next_word in next_words:
    print(first_word, next_word)
'''


def walk_graph(graph, distance=5, start_node=None):
  """Returns a list of words from a randomly weighted walk."""
  if distance <= 0:
    return []
  
  # If not given, pick a start node at random.
  if not start_node:
    start_node = random.choice(list(graph.keys()))
  
  
  weights = np.array(
      list(markov_graph[start_node].values()),
      dtype=np.float64)
  # Normalize word counts to sum to 1.
  weights /= weights.sum()

  # Pick a destination using weighted distribution.
  choices = list(markov_graph[start_node].keys())
  chosen_word = np.random.choice(choices, None, p=weights)
  
  return [chosen_word] + walk_graph(
      graph, distance=distance-1,
      start_node=chosen_word)
  
alphabet = list(string.ascii_lowercase)

len_stanza = random.randint(4,10)
num_stanza = random.randint(1,5)
for i in range(num_stanza):
  for j in range(len_stanza):
    len_line = random.randint(6,12)
    line = ' '.join(walk_graph(markov_graph, distance = len_line))
    line = line.replace(" i ", " I ")
    line = line.replace(" d ", "ed  ")
    line = line.replace(" _ ", "")
    line_list = list(line)
    line_list[0] = line_list[0].upper()
    new_line = ''.join(line_list)
    print(new_line)
  print(" ")

