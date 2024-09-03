vowels = ['a', 'e', 'i', 'o', 'u']
found = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
text = "Working with dictionary here"

for letter in text:
    if letter in vowels:
        found[letter] += 1
for vowel, times in sorted(found.items()):
    print(vowel, 'was found', times, 'time(s).')
