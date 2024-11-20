def find_anagrams(word_list):

  anagram_dict = {}
  for word in word_list:
    sorted_word = ''.join(sorted(word))
    if sorted_word not in anagram_dict:
      anagram_dict[sorted_word] = []
    anagram_dict[sorted_word].append(word)

  result = {}
  for key, value in anagram_dict.items():
    if len(value) > 1:
      for word in value:
        result[word] = value
  return result


find_anagrams(["enlist" , "listen" , "cat" , "act"])