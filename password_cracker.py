import hashlib

def crack_sha1_hash(hash, use_salts = False):
    with open('top-10000-passwords.txt', 'r', encoding='utf-8') as f:
        passwords = f.read().splitlines()

    if use_salts:
        with open('known-salts.txt', 'r', encoding='utf-8') as f:
            salts = f.read().splitlines()

        for pw in passwords:
            for s in salts:
                # Prepend salt
                if hashlib.sha1((s + pw).encode('utf-8')).hexdigest() == hash:
                    return pw
                # Append salt
                if hashlib.sha1((pw + s).encode('utf-8')).hexdigest() == hash:
                    return pw
    else:
        for pw in passwords:
            if hashlib.sha1(pw.encode('utf-8')).hexdigest() == hash:
                return pw

    return "PASSWORD NOT IN DATABASE"
