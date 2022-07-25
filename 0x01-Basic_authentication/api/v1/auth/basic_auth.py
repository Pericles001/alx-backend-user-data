#!/usr/bin/env python3
"""
Basic auth
"""

from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """
    BasicAuth class
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        returns the Base64 part
        of the Authorization header for a Basic Authentication
        """
        if not authorization_header or type(authorization_header) != str or not authorization_header.startswith("Basic "):
            return
        return "".join(authorization_header.split(" ")[1:])

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """
         returns the decoded value of a Base64 string base64_authorization_header
        """
        if not base64_authorization_header or type(base64_authorization_header) != str:
            return
        try:
            b64_bytes = base64_authorization_header.encode('utf-8')
            res = base64.b64decode(b64_bytes)
            return res.decode('utf-8')
        except Exception:
            return
