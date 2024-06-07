""" 
648. Replace Words

In English, we have a concept called root, which can be followed by some other word to form another longer word 
- let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. 
If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c" """



class Solution:
  def __init__(self):
    self.root = {}

  def insert(self, word: str) -> None:
    node = self.root
    for c in word:
      if c not in node:
        node[c] = {}
      node = node[c]
    node['word'] = word

  def search(self, word: str) -> str:
    node = self.root
    for c in word:
      if 'word' in node:
        return node['word']
      if c not in node:
        return word
      node = node[c]
    return word

  def replaceWords(self, dictionary: List[str], sentence: str) -> str:
    for word in dictionary:
      self.insert(word)

    words = sentence.split(' ')
    return ' '.join([self.search(word) for word in words])


