# He needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal.
#
# To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

from hashlib import md5

raw_string = input()

counter = 1
while True:
    before_hash = (raw_string + str(counter)).encode('utf-8')
    after_hash = md5(before_hash).hexdigest()
    if after_hash[:5] == '00000':
        break
    counter += 1
print(after_hash, counter)

counter = 1
while True:
    before_hash = (raw_string + str(counter)).encode('utf-8')
    after_hash = md5(before_hash).hexdigest()
    if after_hash[:6] == '000000':
        break
    counter += 1
print(after_hash, counter)
