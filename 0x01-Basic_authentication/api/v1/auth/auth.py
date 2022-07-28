#!/usr/bin/env python3
"""
Auth class
"""

from tkinter.messagebox import NO
from flask import request
from typing import TypeVar, List
User = TypeVar('User')


class Auth:
    """
    a class to manage the API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        returns False - path and excluded_paths
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        returns None - request
        """
        return None

    def current_user(self, request=None) -> User:
        """
        returns None - request
        """
        return None
