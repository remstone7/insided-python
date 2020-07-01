from .api_helper import ApiHelper


class Users(ApiHelper):
    USER_URL = '/user'
    USER_CREATE_URL = '{}/register'.format(USER_URL)
    USER_ID_URL = USER_URL + '/{}'
    USER_ACTIVITY_URL = '{}/activity'.format(USER_URL)
    USER_ID_DELETE_URL = USER_URL + '/{}/erase'
    USER_ROLE_ADD_URL = USER_URL + '/{}/role'
    USER_FIELD_VALUE_URL = USER_URL +  '/{}/{}'
    USER_ID_FIELD_VALUE_URL = USER_ID_URL + '/{}/{}'
    USER_DELETE_CUSTOM_FIELD_URL = USER_URL + '/{}/profile_field/{}'
    USER_REMOTE_LOGOUT_URL = '/remotelogout/{}/{}'
    USER_BADGE_URL = USER_ID_URL + '/badge/{}'

    GAMIFICATION_BADGES_URL = '/gamification/badges'
    GAMIFICATION_BADGE_ID_URL = GAMIFICATION_BADGES_URL + '/{}'

    DEFAULT_STARTING_PAGE = 1
    DEFAULT_PAGE_SIZE = 10

    def get_users(self, page=DEFAULT_STARTING_PAGE, page_size=DEFAULT_PAGE_SIZE):
        """Fetches a list of all users.

        Args:
            page (int): Page number pagination starts from.
            page_size (int): Number of results returned in paginated list.

        Returns:
            (InsidedResponse): A list of users.
        """
        params = {
            self.PAGE_PARAM: page,
            self.PAGE_SIZE_PARAM: page_size
        }

        return self._request(self.USER_URL, params=params)

    def create_user(self, email, password, username=None):
        """Generates a new User in Insided.

        Args:
            email (str): User's email address.
            password (str): User's password.
            username (str): User's username.

        Returns:
            (InsidedResponse): Information about the created user.
        """
        data = {
            'data': {
                'email': email,
                'username': username or email,
                'password': password
            }
        }
        return self._request(self.USER_CREATE_URL, json=data, method=self.HTTP_POST)

    def get_user_by_id(self, user_id):
        """Fetches a user by their ID.

        Args:
            user_id (int): Unique User ID.

        Returns:
            (InsidedResponse): Information about the requested User.
        """
        return self._request(self.USER_ID_URL.format(user_id))

    def get_user_activity(self, page=DEFAULT_STARTING_PAGE, page_size=DEFAULT_PAGE_SIZE, api_filter=None):
        """Fetches all users activities or a single user's activities in public categories.

        Args:
            page (int): Page number pagination starts from.
            page_size (int): Number of results returned in paginated list.
            api_filter (array[array]): Filter based on subset of defined events.

        Returns:
            (InsidedResponse): User activity.
        """
        params = {
            self.PAGE_PARAM: page,
            self.PAGE_SIZE_PARAM: page_size
        }
        if api_filter:
            params[self.FILTER_PARAM] = api_filter

        return self._request(self.USER_ACTIVITY_URL, params=params)

    def delete_user(self, user_id):
        """Removes a user.

        Args:
            user_id (int): Unique User ID.

        Returns:
            (InsidedResponse): Information about the removed user.
        """
        return self._request(self.USER_ID_DELETE_URL.format(user_id), method=self.HTTP_DELETE)

    def add_user_role(self, user_id, role=[]):
        """Adds a new role to a user.

        Args:
            user_id (int): Unique User ID.
            role (list): Roles to be added to the user.

        Returns:
            (InsidedResponse)
        """
        data = {
            'data': role
        }
        return self._request(self.USER_ROLE_ADD_URL.format(user_id), json=data)


    def get_user_by_field(self, field, value):
        """Get's a user by field.

        Args:
            field (str): The field to look for.
            value (str): The value to look for.

        Returns:
            (InsidedResponse): Returns a Json User.
        """
        return self._request(self.USER_FIELD_VALUE_URL.format(field, value))

    def update_user_field_profile(self, user_id, field, value):
        """Updates a user field.

        Args:
            user_id (int): Unique User ID.
            field (str): The field that will be updated.
            value (str):The new value (url encoded).

        Returns:
            (InsidedResponse): Returns a Json User.
        """
        return self._request(self.USER_ID_FIELD_VALUE_URL.format(user_id, field, value), method=self.HTTP_PUT)

    def delete_user_profile_field(self, user_id, field):
        """Deletes a users profile field.

        Args:
            user_id (int): Unique User ID.
            field (str): The field that will be deleted.

        Returns:
            (InsidedResponse): Returns a Json User.
        """
        return self._request(self.USER_DELETE_CUSTOM_FIELD_URL.format(user_id, field), method=self.HTTP_DELETE)

    def user_logout(self, field, value):
        """Generates a Remote logout for a User.

        Args:
            field (str): The field to look for.
            value (str): The value to look for.

        Returns:
            (InsidedResponse): Returns a Json User.
        """
        return self._request(self.USER_REMOTE_LOGOUT_URL.format(field, value), method=self.HTTP_DELETE)

    def update_user_badge(self, user_id, badge_id):
        """Award a badge identified by ID to the user identified by the user ID.

        Args:
            user_id (int): Unique User ID.
            badge_id (int): The ID of the badge to be awarded.

        Returns:
            (InsidedResponse): Empty if succcessful.
        """
        return self._request(self.USER_BADGE_URL.format(user_id, badge_id), method=self.HTTP_PUT)

    def remove_user_badge(self, user_id, badge_id):
        """Revoke badge from user.

        Args:
            user_id (int): Unique User ID.
            badge_id (int): The id of the badge to be revoked.

        Returns:
            (InsidedResponse): Empty if succcessful.
        """
        return self._request(self.USER_BADGE_URL.format(user_id, badge_id), method=self.HTTP_DELETE)

    def get_badges(self, page=DEFAULT_STARTING_PAGE, page_size=DEFAULT_PAGE_SIZE):
        """Gets a list of all badges.

        Args:
            page (int): Page number pagination starts from.
            page_size (int): Number of results returned in paginated list.

        Returns:
            (InsidedResponse): A list of badges.
        """
        params = {
            self.PAGE_PARAM: page,
            self.PAGE_SIZE_PARAM: page_size
        }
        return self._request(self.GAMIFICATION_BADGES_URL, params=params)

    def delete_badge(self, badge_id):
        """Permanently delete a badge identified by ID from community and revoke it from all users.

        Args:
            badge_id (int): The id of the badge to be removed.

        Returns:
            (InsidedResponse): Status code 304 if successful.
        """
        return self._request(self.GAMIFICATION_BADGE_ID_URL.format(badge_id), method=self.HTTP_DELETE)