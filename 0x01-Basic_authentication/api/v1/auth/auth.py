#!/usr/bin/env python3
"""Module defines the authorization class"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Authorization class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Retricts app access to authorization first"""
        return False

    def authorization_header(self, request=None) -> str:
        """Defines the authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns current user"""
        return None
