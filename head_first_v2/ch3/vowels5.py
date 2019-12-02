vowels = set('aeiou')
word = "extraordinary"
found = []

found = vowels.intersection(set(word))
for vowel in sorted(found):
    print(vowel)
