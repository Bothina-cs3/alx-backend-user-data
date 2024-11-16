#!/usr/bin/env python3
""" Basic Authentication Module """
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """ BasicAuth class for handling basic authentication """

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Returns the User instance based on email and password.

        Args:
            user_email (str): User's email
            user_pwd (str): User's password

        Returns:
            User: The User instance if email and password match, None otherwise
        """
        # Validate input
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        # Search for the user by email
        user_list = User.search({"email": user_email})
        if not user_list:
            return None

        # Verify the user's password
        user = user_list[0]
        if not user.is_valid_password(user_pwd):
            return None

        return user
