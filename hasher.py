from hashlib import md5, sha1, sha256, sha384, sha512

BLOCKSIZE = 131072 # 128MB

ALGORITHMS = ['MD5', 'SHA1', 'SHA256', 'SHA384', 'SHA512']

def get_filehash(path, algorithm):
    if algorithm == 'md5':      
        hasher = md5()
    elif algorithm == 'sha1':
        hasher = sha1()
    elif algorithm == 'sha256':
        hasher = sha256()
    elif algorithm == 'sha384':
        hasher = sha384()
    elif algorithm == 'sha512':
        hasher = sha512()
    else:
        raise UnboundLocalError('Wrong algorithm value! Algorithms: ', ALGORITHMS)

    with open(path, 'rb') as file:
        buff = file.read(BLOCKSIZE)
        while len(buff) > 0:
            hasher.update(buff)
            buff = file.read(BLOCKSIZE)
    return hasher.hexdigest()


if __name__ == '__main__':
    raise RuntimeError('This is not executable file!')