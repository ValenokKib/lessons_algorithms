import hashlib

def count_substring(string):
    substring = set()

    for i in range(len(string)):
        for j in range(len(string), i, -1):
            hash_str = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
            substring.add(hash_str)
    print(f'В строке {string} - {len(substring) - 1} различных подстрок')

a = 'asdfghjklqwertyuiop'
b = 'qwertyui'
c = 'zxcvbnmasdfghj'
print(count_substring(a))
print(count_substring(b))
print(count_substring(c))