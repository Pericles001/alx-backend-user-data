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
        if not ah or type(ah) != str or not ah.startswith("Basic "):
            return
        return "".join(ah.split(" ")[1:])