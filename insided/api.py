import sys

from insided import __version__
from .authorization import Authorization
from .gamification import Gamification
from .users import Users
from .webhooks import Webhooks


class Insided(object):
    """The API Wrapper around the InSided API

    Args:
        client_id (str): Client ID for Insided API.
        client_secret (str): Client Secret for Insided API.
        access_token (str): Bearer token to make API calls with.
        client_id (str): User agent for HTTP requests.
    """
    def __init__(self, client_id=None, client_secret=None, access_token=None, user_agent=None, scopes=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = access_token
        self.scopes = scopes
        self.user_agent = user_agent or 'InsidedPythonSDK/{}'.format(__version__)

    def __getattr__(self, item):
        return InsidedWrapper(item, self)


class InsidedWrapper(object):
    def __init__(self, resource_class, api, *args, **kwargs):
        """An API Wrapper to dynamically load the class and method"""
        if isinstance(resource_class, str):
            self.resource_class = self.str_to_class(resource_class, api)
        else:
            self.resource_class = resource_class

    def __getattr__(self, item):
        """Overwrite to make us dynamically call the called class and it's method automatically"""
        return lambda *args, **kwargs: getattr(self.resource_class, item)(*args, **kwargs)

    @classmethod
    def str_to_class(cls, str, api):
        """Transforms a string class name into a class object.
        Assumes that the class is already loaded.
        Args:
            str (str): Name of a class.
            api (obj): Insided api object.
        Returns:
            (dict): Insided API Response
        """
        return getattr(sys.modules[__name__], str)(
            client_id=api.client_id,
            client_secret=api.client_secret,
            access_token=api.access_token,
            user_agent=api.user_agent
        )




