found = {}
found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0

word = "Working with dictionary here"
for letter in word:
    if letter in found:
        found[letter] += 1
for vowel, times in sorted(found.items()):
    print(vowel, 'was found', times, 'time(s).')