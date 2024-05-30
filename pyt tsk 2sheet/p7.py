def count_words(sentence):

    words = sentence.split()
    num_words = len(words)
    return num_words

input_sentence = input("enter a sentence: ")
word_c = count_words(input_sentence)
print(f"no. of w in s : {word_c}")