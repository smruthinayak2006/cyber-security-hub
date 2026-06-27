import hashlib


def generate_hashes(text: str) -> dict:
    """
    Generate multiple cryptographic hashes for the given text.
    """

    encoded_text = text.encode("utf-8")

    return {
        "md5": hashlib.md5(encoded_text).hexdigest(),
        "sha1": hashlib.sha1(encoded_text).hexdigest(),
        "sha256": hashlib.sha256(encoded_text).hexdigest(),
        "sha512": hashlib.sha512(encoded_text).hexdigest(),
    }