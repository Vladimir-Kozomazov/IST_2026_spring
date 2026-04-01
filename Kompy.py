import string

# string.ascii_uppercase
# "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# shift = 3
# lower = string.ascii_lowercase
# upper = string.ascii_uppercase
# lower + upper

# lower[shift:] + lower[:shift] + upper[shift:] + upper[:shift]


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

    @staticmethod
    def decrypt_caesar(chiphertext, shift):
        return caesar.encrypt_caesar(chiphertext, -shift)


# print(caesar.encrypt_caesar("Python", 3))
# print(caesar.decrypt_caesar("Sbwkrq", 3))

import random
import string
import unittest


class CaesarTestCase(unittest.TestCase):
    def test_encrypt(self):
        cases = [
            ("", 0, ""),
            ("python", 0, "python"),
            ("PYTHON", 0, "PYTHON"),
            ("Python", 0, "Python"),
            ("Python3.6", 0, "Python3.6"),
            ("", 3, ""),
            ("PYTHON", 3, "SBWKRQ"),
            ("python", 3, "sbwkrq"),
            ("Python", 3, "Sbwkrq"),
            ("Python3.6", 3, "Sbwkrq3.6"),
        ]

        for i, (plaintext, shift, chiphertext) in enumerate(cases):
            with self.subTest(case=i, plaintext=plaintext, chiphertext=chiphertext):
                self.assertEqual(
                    chiphertext, caesar.encrypt_caesar(plaintext, shift=shift)
                )

    def test_decrypt(self):
        cases = [
            ("", 0, ""),
            ("python", 0, "python"),
            ("PYTHON", 0, "PYTHON"),
            ("Python", 0, "Python"),
            ("Python3.6", 0, "Python3.6"),
            ("", 3, ""),
            ("SBWKRQ", 3, "PYTHON"),
            ("sbwkrq", 3, "python"),
            ("Sbwkrq", 3, "Python"),
            ("Sbwkrq3.6", 3, "Python3.6"),
        ]

        for i, (chiphertext, shift, plaintext) in enumerate(cases):
            with self.subTest(case=i, chiphertext=chiphertext, plaintext=plaintext):
                self.assertEqual(
                    plaintext, caesar.decrypt_caesar(chiphertext, shift=shift)
                )

    def test_randomized(self):
        shift = random.randint(8, 24)
        plaintext = "".join(
            random.choice(string.ascii_letters + " -,") for _ in range(64)
        )
        ciphertext = caesar.encrypt_caesar(plaintext, shift=shift)
        self.assertEqual(
            plaintext,
            caesar.decrypt_caesar(ciphertext, shift=shift),
            msg=f"shift={shift}, ciphertext={ciphertext}",
        )


suite = unittest.TestLoader().loadTestsFromTestCase(CaesarTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)
