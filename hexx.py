import binascii
import string

class OddLengthString(Exception):
    pass 

class NonHexCharacter(Exception):
    pass 

def encode(s):
    if isinstance(s, str):
        return binascii.hexlify(s.encode())
    elif isinstance(s, bytes):
        return binascii.hexlify(s)
    else:
        raise Exception("Not a string")

def decode(s):
    if isinstance(s, str):
        if len(s)%2 == 1:
            raise OddLengthString
        elif any([x not in string.hexdigits for x in s]):
            raise NonHexCharacter
        else:
            return binascii.unhexlify(s)
    else:
        raise Exception("Not a string")
