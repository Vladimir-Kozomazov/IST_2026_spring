import string


class caesar:
    @staticmethod
    def encrypt_caesar(plaintext, shift):
        shift = shift % 26
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        table = str.maketrans(
            lower + upper, lower[shift:] + lower[:shift] + upper[shift:] + upper[:shift]
        )
        return plaintext.translate(table)


class vigenere:
    @staticmethod
    def encrypt_vigenere(plaintext: str, keyword: str) -> str:
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        n = len(keyword)
        cipher_text = list(plaintext)
        for i in range(n):
            if keyword[i] in lower:
                shift = lower.find(keyword[i])
            else:
                shift = upper.find(keyword[i])
            cipher_text[i::n] = caesar.encrypt_caesar(plaintext[i::n], shift)
        cipher_text = "".join(cipher_text)
        return cipher_text

    def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        n = len(keyword)
        cipher_text = list(ciphertext)
        for i in range(n):
            if keyword[i] in lower:
                shift = lower.find(keyword[i])
            else:
                shift = upper.find(keyword[i])
            cipher_text[i::n] = caesar.encrypt_caesar(ciphertext[i::n], -shift)
        cipher_text = "".join(cipher_text)
        return cipher_text
