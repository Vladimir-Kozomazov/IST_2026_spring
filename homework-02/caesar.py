import typing as tp
import string


class caesar:
    @staticmethod
    def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
        shift = shift % 26
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        table = str.maketrans(
            lower + upper, lower[shift:] + lower[:shift] + upper[shift:] + upper[:shift]
        )
        return plaintext.translate(table)

    def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
        return caesar.encrypt_caesar(ciphertext, -shift)


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
