import base64

def encode(s, url):
    if isinstance(s, str):
        return base64.urlsafe_b64encode(s.encode()) if url else base64.b64encode(s.encode())
    elif isinstance(s, bytes):
        return base64.urlsafe_b64encode(s) if url else base64.b64encode(s)
    else:
        raise Exception("Not a string")

def decode(s, url):
    if isinstance(s, str):
        try:
            s += "=" * ((4 - len(s) % 4) % 4)
            return base64.urlsafe_b64decode(s) if url else base64.b64decode(s)
        except:
            raise Exception("Can not decode base64 string")
