#!/usr/bin/env python3
"""Basic Authentication"""

from api.v1.auth.auth import Auth
from base64 import b64decode


class BasicAuth(Auth):
    """Basic authentication class"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Performs base64 encoding on the authorization_header"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        authstr = authorization_header.split(' ')
        return authstr[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """Decodes a base 64 string"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            encode_utf8 = base64_authorization_header.encode('utf-8')
            decoded = b64decode(encode_utf8)
            actual_value = decoded.decode('utf-8')
            return actual_value
        except Exception:
            return None
