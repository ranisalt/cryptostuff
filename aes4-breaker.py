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
pre_last_sr = (aes4.inv_shift_row(text) for text in ciphered)

xoration = []
kick = 0


