import hashlib, time

#Made by IRISnoir
#12 hash type
#Blake2B length = 128
#Blake2S length = 64
#MD5 length = 32
#SHA1 length = 40
#SHA224 length = 56
#SHA256 length = 64
#SHA384 length = 96
#SHA3_224 length = 56
#SHA3_256 length = 64
#SHA3_384 length = 96
#SHA3_512 length = 128
#SHA512 length = 128

while True:
    input_hash = input('Enter your hash here: ')
    if input_hash != '' and len(input_hash) in [32,40,56,64,96,128]:
        break
    else:
        print('Please enter a valid hash')

while True:
    wordlist = input('Enter your wordlist here: ')
    try:
        open(wordlist,'r')
    except FileNotFoundError:
        print('File does not exist.')
    else:
        print('Using file \'' + wordlist + '\'')
        wl = open(wordlist,'rb').readlines()
        break

linum = 0
word = ''

if len(input_hash) == 32:
    print('Hash type: MD5')
    time.sleep(1)
    print('Begin cracking')
    while True:
        try:
            com_hash = hashlib.md5(wl[linum][:len(wl[linum])-1]).hexdigest()
            word = wl[linum][:len(wl[linum])-1]
            print('Comparing: ' + str(input_hash) + ' - ' + str(com_hash) + ' ( ' + str(word)[1:] + ' )')
            if com_hash == input_hash:
                print('\nHash successfully cracked')
                print('MD5: ' + str(input_hash) + ' : ' + str(word)[1:])
                break
            else:
                linum += 1
        except IndexError:
            print('\nHash uncrackable with MD5')
            break

if len(input_hash) == 40:
    print('Hash type: SHA1')
    time.sleep(1)
    print('Begin cracking')
    while True:
        try:
            com_hash = hashlib.sha1(wl[linum][:len(wl[linum])-1]).hexdigest()
            word = wl[linum][:len(wl[linum])-1]
            print('Comparing: ' + str(input_hash) + ' - ' + str(com_hash) + ' ( ' + str(word)[1:] + ' )')
            if com_hash == input_hash:
                print('\nHash successfully cracked')
                print('SHA1: ' + str(input_hash) + ' : ' + str(word)[1:])
                break
            else:
                linum += 1
        except IndexError:
            print('\nHash uncrackable with SHA1')
            break

if len(input_hash) == 56:
    print('Hash type: SHA224 or SHA3-224')
    time.sleep(1.2)
    print('Trying SHA224')
    time.sleep(0.5)
    print('Begin cracking')
    while True:
        try:
            com_hash1 = hashlib.sha224(wl[linum][:len(wl[linum])-1]).hexdigest()
            word1 = wl[linum][:len(wl[linum])-1]
            print('Comparing: ' + str(input_hash) + ' - ' + str(com_hash1) + ' ( ' + str(word1)[1:] + ' )')
            if com_hash1 == input_hash:
                print('\nHash successfully cracked')
                sha224 = 1
                time.sleep(3)
                break
            else:
                linum += 1
        except IndexError:
            print('\nHash uncrackable with SHA224')
            sha224 = 0
            time.sleep(3)
            break
    print('Trying SHA3-224')
    time.sleep(0.5)
    print('Begin cracking')
    linum = 0
    while True:
        try:
            com_hash2 = hashlib.sha3_224(wl[linum][:len(wl[linum])-1]).hexdigest()
            word2 = wl[linum][:len(wl[linum])-1]
            print('Comparing: ' + str(input_hash) + ' - ' + str(com_hash2) + ' ( ' + str(word2)[1:] + ' )')
            if com_hash2 == input_hash:
                print('\nHash successfully cracked')
                sha3_224 = 1
                time.sleep(3)
                break
            else:
                linum += 1
        except IndexError:
            print('\nHash uncrackable with SHA3-224')
            sha3_224 = 0
            time.sleep(3)
            break
    print('')
    if sha224 == 1:
        print('SHA224: ' + str(input_hash) + ' : ' + str(word1)[1:])
    elif sha3_224 == 1:
        print('SHA3-224: ' + str(input_hash) + ' : ' + str(word2)[1:])
    else:
        print('Hash stays uncracked')

if len(input_hash) == 64:
    print('Hash type: Blake2S or SHA256 or SHA3-256')
    time.sleep(1.2)
    print('Trying Blake2S')
    time.sleep(0.5)
    print('Begin cracking')
    while True:
        try:
            com_hash1 = hashlib.blake2s(wl[linum][:len(wl[linum])-1]).hexdigest()
            word1 = wl[linum][:len(wl[linum])-1]
            print('Comparing: ' + str(input_hash) + ' - ' + str(com_hash1) + ' ( ' + str(word1)[1:] + ' )')
            if com_hash1 == input_hash:
                print('\nHash successfully cracked')
                blake2s = 1
                time.sleep(3)
                break
            else:
                linum += 1
        except IndexError:
            print('\nHash uncrackable with Blake2S')
            blake2s = 0
            time.sleep(3)
            break
    print('Trying SHA256')
    time.sleep(0.5)
    print('Begin cracking')
    linum = 0
    while True:
        try:
            com_hash2 = hashlib.sha256(wl[linum][:len(wl[linum])-1]).hexdigest()
            word2 = wl[linum][:len(wl[linum])-1]
            print('Comparing: ' + str(input_hash) + ' - ' + str(com_hash2) + ' ( ' + str(word2)[1:] + ' )')
            if com_hash2 == input_hash:
                print('\nHash successfully cracked')
                sha256 = 1
                time.sleep(3)
                break
            else:
                linum += 1
        except IndexError:
            print('\nHash uncrackable with SHA256')
            sha256 = 0
            time.sleep(3)
            break
    print('Trying SHA3-256')
    time.sleep(0.5)
    print('Begin cracking')
    linum = 0
    while True:
        try:
            com_hash3 = hashlib.sha3_256(wl[linum][:len(wl[linum])-1]).hexdigest()
            word3 = wl[linum][:len(wl[linum])-1]
            print('Comparing: ' + str(input_hash) + ' - ' + str(com_hash3) + ' ( ' + str(word3)[1:] + ' )')
            if com_hash3 == input_hash:
                print('\nHash successfully cracked')
                sha3_256 = 1
                time.sleep(3)
                break
            else:
                linum += 1
        except IndexError:
            print('\nHash uncrackable with SHA3-256')
            sha3_256 = 0
            time.sleep(3)
            break
    print('')
    if blake2s == 1:
        print('Blake2S: ' + str(input_hash) + ' : ' + str(word1)[1:])
    elif sha256 == 1:
        print('SHA256: ' + str(input_hash) + ' : ' + str(word2)[1:])
    elif sha3_256 == 1:
        print('SHA3-256: ' + str(input_hash) + ' : ' + str(word3)[1:])
    else:
        print('Hash stays uncracked')

if len(input_hash) == 96:
    print('Hash type: SHA384 or SHA3-384')
    time.sleep(1.2)
    print('Trying SHA384')
    time.sleep(0.5)
    print('Begin cracking')
    while True:
        try:
            com_hash1 = hashlib.sha384(wl[linum][:len(wl[linum])-1]).hexdigest()
            word1 = wl[linum][:len(wl[linum])-1]
            print('Comparing: ' + str(input_hash) + ' - ' + str(com_hash1) + ' ( ' + str(word1)[1:] + ' )')
            if com_hash1 == input_hash:
                print('\nHash successfully cracked')
                sha384 = 1
                time.sleep(3)
                break
            else:
                linum += 1
        except IndexError:
            print('\nHash uncrackable with SHA384')
            sha384 = 0
            time.sleep(3)
            break
    print('Trying SHA3-384')
    time.sleep(0.5)
    print('Begin cracking')
    linum = 0
    while True:
        try:
            com_hash2 = hashlib.sha3_384(wl[linum][:len(wl[linum])-1]).hexdigest()
            word2 = wl[linum][:len(wl[linum])-1]
            print('Comparing: ' + str(input_hash) + ' - ' + str(com_hash2) + ' ( ' + str(word2)[1:] + ' )')
            if com_hash2 == input_hash:
                print('\nHash successfully cracked')
                sha3_384 = 1
                time.sleep(3)
                break
            else:
                linum += 1
        except IndexError:
            print('\nHash uncrackable with SHA256')
            sha3_384 = 0
            time.sleep(3)
            break
    if sha384 == 1:
        print('SHA384: ' + str(input_hash) + ' : ' + str(word1)[1:])
    elif sha3_384 == 1:
        print('SHA3-384: ' + str(input_hash) + ' : ' + str(word2)[1:])
    else:
        print('Hash stays uncracked')

if len(input_hash) == 128:
    print('Hash type: Blake2B or SHA512 or SHA3-512')
    time.sleep(1.2)
    print('Trying Blake2B')
    time.sleep(0.5)
    print('Begin cracking')
    while True:
        try:
            com_hash1 = hashlib.blake2b(wl[linum][:len(wl[linum])-1]).hexdigest()
            word1 = wl[linum][:len(wl[linum])-1]
            print('Comparing: ' + str(input_hash) + ' - ' + str(com_hash1) + ' ( ' + str(word1)[1:] + ' )')
            if com_hash1 == input_hash:
                print('\nHash successfully cracked')
                blake2b = 1
                time.sleep(3)
                break
            else:
                linum += 1
        except IndexError:
            print('\nHash uncrackable with Blake2B')
            blake2b = 0
            time.sleep(3)
            break
    print('Trying SHA512')
    time.sleep(0.5)
    print('Begin cracking')
    linum = 0
    while True:
        try:
            com_hash2 = hashlib.sha512(wl[linum][:len(wl[linum])-1]).hexdigest()
            word2 = wl[linum][:len(wl[linum])-1]
            print('Comparing: ' + str(input_hash) + ' - ' + str(com_hash2) + ' ( ' + str(word2)[1:] + ' )')
            if com_hash2 == input_hash:
                print('\nHash successfully cracked')
                sha512 = 1
                time.sleep(3)
                break
            else:
                linum += 1
        except IndexError:
            print('\nHash uncrackable with SHA512')
            sha512 = 0
            time.sleep(3)
            break
    print('Trying SHA3-512')
    time.sleep(0.5)
    print('Begin cracking')
    linum = 0
    while True:
        try:
            com_hash3 = hashlib.sha3_512(wl[linum][:len(wl[linum])-1]).hexdigest()
            word3 = wl[linum][:len(wl[linum])-1]
            print('Comparing: ' + str(input_hash) + ' - ' + str(com_hash3) + ' ( ' + str(word3)[1:] + ' )')
            if com_hash3 == input_hash:
                print('\nHash successfully cracked')
                sha3_512 = 1
                time.sleep(3)
                break
            else:
                linum += 1
        except IndexError:
            print('\nHash uncrackable with SHA3-512')
            sha3_512 = 0
            time.sleep(3)
            break
    print('')
    if blake2b == 1:
        print('Blake2B: ' + str(input_hash) + ' : ' + str(word1)[1:])
    elif sha512 == 1:
        print('SHA512: ' + str(input_hash) + ' : ' + str(word2)[1:])
    elif sha3_512 == 1:
        print('SHA3-512: ' + str(input_hash) + ' : ' + str(word3)[1:])
    else:
        print('Hash stays uncracked')
