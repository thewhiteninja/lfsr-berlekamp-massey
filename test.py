from __future__ import print_function

import random

from berlekamp_massey import *
from lfsr import *


def step(name):
    n = (78 - len(name)) / 2
    print("\n" + n*"#" + " " + name + " " + n*"#" + "\n")

def bytes_to_bin(bytedata):
    return "".join([format(ord(b), '08b') for b in bytedata])


def xor(a, b):
    return "".join([chr(ord(a[i]) ^ ord(b[i % len(b)])) for i in range(len(a))])


def test():
    step("Encryption")

    cleartext = "the secret is: there is no spoon"

    print("Cleartext       :", cleartext)

    seed1 = "".join([random.choice("01") for _ in range(6)])
    poly1 = LFSR([0, 1, 5, 6], seed1)
    print("LFSR init       :", str(poly1), "(" + seed1 + ")")

    bitstream = "".join([chr(poly1.next_byte()) for _ in range(len(cleartext))])
    print("LFSR stream     :", bitstream.encode("hex"))

    ciphertext = xor(cleartext, bitstream)

    print("Ciphertext      :", ciphertext.encode("hex"))

    step("Decryption")

    known_cleartext = "the"
    print("Known cleartext :", known_cleartext)

    bitstream = xor(known_cleartext, ciphertext[:len(known_cleartext)])
    print("Stream start    : " + bitstream.encode("hex"))

    bm = BerlekampMassey(bytes_to_bin(bitstream))

    print("Recovered LFSR  : " + str(bm))

    poly2 = LFSR(bm.get_polynomial(), bytes_to_bin(bitstream)[:bm.get_polynomial_degree()])

    bitstream = "".join([chr(poly2.next_byte()) for _ in range(len(cleartext))])
    print("LFSR stream     :", bitstream.encode("hex"))

    decrypted = xor(ciphertext, bitstream)
    print("\nDecrypted       :", decrypted)

    step("Test")

    print("Test OK         :", str(cleartext == decrypted))


if __name__ == '__main__':
    print()
    print("TEST - LFSR & Berlekamp-Massey")

    test()
