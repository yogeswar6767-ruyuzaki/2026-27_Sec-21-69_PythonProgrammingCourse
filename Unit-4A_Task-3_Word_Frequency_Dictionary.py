# program to count the frequency of words in a sentence using a dictionary

sentence = input("Enter a sentence: ")
words = sentence.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print("Frequency:", freq)