def is_pangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    sentence_letters = set(sentence.lower())
    return sentence_letters.issuperset(alphabet)
