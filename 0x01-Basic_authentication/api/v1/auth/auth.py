#!/usr/bin/env python3
"""
Auth class

Create the class Auth:
in the file api/v1/auth/auth.py
import request from flask
class name Auth
public method def require_auth(self, path: str, excluded_paths: List[str]) -> bool: that returns False - path and excluded_paths will be used later, now, you don’t need to take care of them
public method def authorization_header(self, request=None) -> str: that returns None - request will be the Flask request object
public method def current_user(self, request=None) -> TypeVar('User'): that returns None - request will be the Flask request object
"""


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
        
        
    def authorization_header(self, request=None) -> str:
        """
        returns None - request
        """
    
    
    def current_user(self, request=None) -> TypeVar('User'):
        """
        returns None - request
        """
