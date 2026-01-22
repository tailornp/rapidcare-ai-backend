import string

BASE62_ALPHABET = string.digits + string.ascii_letters

def encode_base62(num: int) -> str:
    if num < 0:
        raise ValueError("Number must be non-negative")

    if num == 0:
        return BASE62_ALPHABET[0]

    result = []
    base = len(BASE62_ALPHABET)

    while num:
        num, rem = divmod(num, base)
        result.append(BASE62_ALPHABET[rem])

    return ''.join(reversed(result))