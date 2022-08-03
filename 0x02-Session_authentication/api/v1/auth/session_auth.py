#!/usr/bin/env python3
"""
SessionAuth
"""

from api.v1.auth.auth import Auth
from typing import TypeVar
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """
    Session auth class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        creates a Session ID for a user_id
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        SessionAuth.user_id_by_session_id[user_id] = session_id
        return session_id
