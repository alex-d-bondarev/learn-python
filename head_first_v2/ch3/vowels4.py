vowels = ['a', 'e', 'i', 'o', 'u']
found = {}
text = "Working with dictionary here"

for letter in text:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1
for vowel, times in sorted(found.items()):
    print(vowel, 'was found', times, 'time(s).')
