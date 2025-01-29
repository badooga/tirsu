"""Arabic letters for the Tir language."""

tir_alphabet = set(
    [*"abcdefghijklmnopqrstuvwxyz", "ea", "'", "oa", "oi", "ou", "ch", "sh", "th", "zh"]
)


def in_alphabet(letter) -> bool:
    """Checks if the supplied letter is in the Tir'su alphabet."""

    return letter.strip() == "" or letter.lower() in tir_alphabet
