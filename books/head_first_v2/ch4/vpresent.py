def search_for_vowels(word):
    """Display any vowels found in an asked word."""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return bool(found)


print(search_for_vowels(input("Type some word here: ")))