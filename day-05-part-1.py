# day 5 puzzle 1
import hashlib

prefix='ugkcyxxp'
password = ''
for i in range(100000000):
    md5hash = hashlib.md5((prefix+str(i)).encode('ascii')).hexdigest()
    if md5hash.startswith('00000'):
        password += md5hash[5:6]
        if len(password) == 8:
            break
print(password)
