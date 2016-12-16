# day 5 puzzle 2
import hashlib
from string import ascii_lowercase

prefix='ugkcyxxp'
password = [None] * 8
chars_added = 0
for i in range(100000000):
    md5hash = hashlib.md5((prefix + str(i)).encode('ascii')).hexdigest()
    if md5hash.startswith('00000'):
        position = md5hash[5:6]
        if position in ascii_lowercase or int(position) > 7 or password[int(position)] is not None:
            continue
        else:
            password[int(position)] = md5hash[6:7]
            chars_added += 1
            if chars_added == 8:
                break
print(''.join(password))
