#!/usr/bin/env python3
"""
Basic auth
"""


from requests import head
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

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """
        returns the user email and password from the Base64 decoded value
        """
        if not decoded_base64_authorization_header or type(decoded_base64_authorization_header) != str or ":" not in decoded_base64_authorization_header:
            return (None, None)
        a, b = decoded_base64_authorization_header.split(':')[0], "".join(
            decoded_base64_authorization_header.split(':', 1)[1:])
        return (a, b)

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        returns the User instance based on his email and password
        """
        if (not user_email or type(user_email) != str or not user_pwd or type(user_pwd) != str):
            return
        user = None
        try:
            user = User.search({"email": user_email})
        except Exception:
            return
        if not user:
            return
        for u in user:
            if u.is_valid_password(user_pwd):
                return u

    def current_user(self, request=None) -> TypeVar('User'):
        """
         overloads Auth and retrieves the User instance for a request
        """
        header = self.authorization_header(request)
        b64header = self.extract_base64_authorization_header(header)
        decoded = self.decode_base64_authorization_header(b64header)
        user_creds = self.extract_base64_authorization_header(decoded)
        return self.user_object_from_credentials(*user_creds)
