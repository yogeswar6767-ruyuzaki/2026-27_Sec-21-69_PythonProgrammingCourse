# program to count the frequency of each character in a string

s = input("Enter a string: ")

frequency = {}

for ch in s:
    if ch in frequency:
        frequency[ch] = frequency[ch] + 1
    else:
        frequency[ch] = 1

for ch, count in frequency.items():
    print(ch, ":", count)