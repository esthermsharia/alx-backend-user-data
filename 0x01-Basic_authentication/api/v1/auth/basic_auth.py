#!/usr/bin/env python3
"""Basic Authentication"""

from api.v1.auth.auth import Auth


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
