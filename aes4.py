import itertools
from utils import gcd


def AES(text, key, rounds):
    if not isinstance(text, bytearray):
        text = bytearray(text.encode())

    if not isinstance(key, bytes):
        key = bytes(key)

    assert len(key) == 128

    def chunks(text, width=16):
        orig = text[:]
        missing = 16 - (len(orig) % 16)
        orig.extend([0] * missing)
        i = 0
        while i < len(orig):
            yield orig[i:i + width]
            i += width

    def sub_bytes(text, round):
        pass

    def shift_row(text, round):
        text[4:8] = text[5:8] + text[4:5]
        text[8:12] = text[10:12] + text[8:10]
        text[12:16] = text[15:16] + text[12:15]

    def mix_column(text, round):
        matrix = (2, 3, 1, 1, 1, 2, 3, 1, 1, 1, 2, 3, 3, 1, 1, 2)
        for i in range(16):
            text[i] ^= matrix[i]

    def add_round_key(text, round):
        pass

    for chunk in chunks(text):
        add_round_key(chunk, 0)
        for round in range(1, rounds):
            sub_bytes(chunk, round)
            shift_row(chunk, round)
            mix_column(chunk, round)
            add_round_key(chunk, round)
        sub_bytes(chunk, rounds)
        shift_row(chunk, rounds)
        add_round_key(chunk, rounds)
