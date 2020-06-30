from .api_helper import ApiHelper


class Users(ApiHelper):
    USER_URL = '/user'
    USER_CREATE_URL = '{}/register'.format(USER_URL)
    USER_ID_URL = USER_URL + '/{}'
    USER_ACTIVITY_URL = '{}/activity'.format(USER_URL)
    USER_ID_DELETE_URL = USER_URL + '/{}/erase'
    USER_ROLE_ADD_URL = USER_URL + '/{}/role'

    DEFAULT_STARTING_PAGE = 1
    DEFAULT_PAGE_SIZE = 10

    def get_users(self, page=DEFAULT_STARTING_PAGE, page_size=DEFAULT_PAGE_SIZE):
        """

        Args:
            page:
            page_size:

        Returns:

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
            (dict): Information about the created user.
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
            (dict): Information abotu the requested User.
        """
        return self._request(self.USER_ID_URL.format(user_id))

    def get_user_activity(self, page=DEFAULT_STARTING_PAGE, page_size=DEFAULT_PAGE_SIZE, api_filter=None):
        """

        Args:
            page:
            page_size:
            api_filter:

        Returns:

        """
        params = {
            self.PAGE_PARAM: page,
            self.PAGE_SIZE_PARAM: page_size
        }
        if api_filter:
            params[self.FILTER_PARAM] = api_filter

        return self._request(self.USER_ACTIVITY_URL, params=params)

    def delete_user(self, user_id):
        """

        Args:
            user_id:

        Returns:

        """
        return self._request(self.USER_ID_DELETE_URL.format(user_id), method=self.HTTP_DELETE)

    def add_user_role(self, user_id, role=[]):
        data = {
            'data': role
        }
        self._request(self.USER_ROLE_ADD_URL.format(user_id), json=data)

