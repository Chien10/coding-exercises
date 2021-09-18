# O(n) + O(m) in time where m is the number of words within a sentence
def brute_force(sentence: str) -> str:
	# Sentence seperated by space only
	sentence = ''.join(reversed(sentence))
	list_words = sentence.split(' ')
	for i, word in enumerate(list_words):
		list_words[i] = ''.join(reversed(word))

	return ' '.join(list_words)