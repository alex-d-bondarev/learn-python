def search_for_letters(phrase: str = 'life, the universe, and everything', letters: str = 'forty two') -> set:
    """Display any 'letters' found in a 'phrase'."""
    return set(letters).intersection(set(phrase))


print(search_for_letters(input("Type some phrase here: "), input("Type letters to search for: ")))

print(search_for_letters())

print(search_for_letters(letters='qaz', phrase='abcdefg'))
