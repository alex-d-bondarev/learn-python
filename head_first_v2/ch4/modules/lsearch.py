def search_for_letters(phrase: str = 'life, the universe, and everything', letters: str = 'forty two') -> set:
    """Display any 'letters' found in a 'phrase'."""
    return set(letters).intersection(set(phrase))


def search_for_vowels(phrase: str) -> set:
    """Display any vowels found in an asked phrase."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))