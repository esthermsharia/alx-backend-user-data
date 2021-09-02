#!/usr/bin/env python3
""" takes in a password string arguments and returns bytes.
    The returned bytes is a salted hash of the input password
"""
import bcrypt
salt = bcrypt.gensalt()


def _hash_password(password: str) -> bytes:
    """Hashes a password"""
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed
