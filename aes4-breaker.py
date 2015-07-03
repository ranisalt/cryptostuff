import aes4
import random
import string

def gen_integral(constant):
    ret = []
    for i in range(256):
        _set = [i] + [constant] * 15
        ret.append(_set)

    return ret

# generate random key
key = ''.join(random.sample(string.ascii_letters, 32))

# cipher ingegrals with key
integrals = gen_integral(1)
ciphered = (aes4.AES128(x, key.encode(), 4) for x in integrals)
pre_last_sr = list(aes4.inv_shift_row(text) for text in ciphered)
possible_key = []
for _ in range(32):
    possible_key.append([])

for pos in range(16):
    for kick in range(256):
        # invert kick bits?
        nkick = ~kick & 0xFF
        xoration = 0
        for text in pre_last_sr:
            # xor with xorred byte and kick
            xoration ^= aes4.sbox.index(text[pos] ^ nkick)

        if xoration == 0:
            possible_key[pos].append(kick)

pass
