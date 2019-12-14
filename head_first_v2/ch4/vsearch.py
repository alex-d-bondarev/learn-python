def search_for_vowels(word):
    """Display any vowels found in an asked word."""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    for vowel in sorted(found):
        print(vowel)


search_for_vowels(input("Type some word here: "))