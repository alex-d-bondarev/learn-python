def search_for_vowels(phrase: str) -> set:
    """Display any vowels found in an asked phrase."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


print(search_for_vowels(input("Type some phrase here: ")))
