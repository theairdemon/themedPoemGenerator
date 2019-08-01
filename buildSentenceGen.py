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
    for word in re.findall(r"[\w']+|[.,!?;]", text)
    if word != ''
]
 

# Create graph.
markov_graph = defaultdict(lambda: defaultdict(int))

last_word = tokenized_text[0].lower()
for word in tokenized_text[1:]:
  word = word.lower()
  if not word.isdigit():
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
    start_node = random.choice(list(markov_graph['.'].keys()))
  
  
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

num_stanza = random.randint(2,8)
len_stanza = random.randint(4,10)
len_line = random.randint(6,12)

total_len = len_stanza * num_stanza * len_line

punct_set = {'.', ',', '!', '?', ';'}
end_punct_set = {'.', '!', '?'}

word_list = walk_graph(markov_graph, distance = total_len)
for i in range(0, len(word_list)):
  if i == 0 and word_list[i] in punct_set:
    word_list[i] = ""
  elif word_list[i] =="i":
    word_list[i] = "I"
  elif word_list[i] == " _ ":
    word_list[i] = ""
  elif word_list[i] == "D":
    word_list[i] = ""
  elif word_list[i] == ",":
    word_list[i] = ","
  elif i != 0 and word_list[i-1] in end_punct_set:
    char_list = list(word_list[i])
    char_list[0] = char_list[0].upper()
    word_list[i] = ''.join(char_list)


if word_list[0] == "":
  word_list.pop(0)

for j in range(0, total_len):
  if j % len_line == 0 and j != 0:
    word_list[j] = word_list[j]+"\n"
  if j % (len_line * len_stanza) == 0 and j != 0:
    word_list[j] = word_list[j]+" \n"

line = ' '.join(word_list)
punct_list = list(punct_set)
for p in punct_list:
  line = line.replace(" "+p, p)

line_list = list(line)
line_list[0] = line_list[0].upper()
for k in range(1, len(line_list)):
  if line_list[k-1] == "\n" and line_list[k] in punct_set:
    line_list[k-1] = ""
    line_list[k] = "\n"
    line_list[k+1] = ""
    line_list[k+2] = line_list[k+2].upper()
  elif line_list[k-1] == "\n" and line_list[k] == " ":
    line_list[k] = ""
    line_list[k+1] = line_list[k+1].upper()
  elif line_list[k-1] == "\n" and line_list[k] == "\n":
    line_list[k+1] = ""
    line_list[k+2] = line_list[k+2].upper()
  elif line_list[k-1] == "\n" and line_list[k] == " " and line_list[k+1] == "d":
    line_list[k] = ""
    line_list[k+1] = ""
    line_list[k+2] = ""
    line_list[k+3] = line_list[k+3].upper()

new_line = ''.join(line_list)
print(new_line)
print(" ")
  
