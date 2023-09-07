def is_unique_bit_vector(string):
    """Uses bitwise operation instead of extra data structures."""
    
    if len(string) > 128:
        return False
    
    checker = 0
    for c in string:
        val = ord(c)
        if (checker & (1 << val)) > 0:
            return False
        checker |= 1 << val

    return True

def is_unique_chars_using_dictionary(string: str) -> bool:
    character_counts = {}
    for char in string:
        if char in character_counts:
            return False
        character_counts[char] = 1
    return True


def is_unique_chars_using_set(string: str) -> bool:
    characters_seen = set()
    for char in string:
        if char in characters_seen:
            return False
        characters_seen.add(char)
    return True