import requests

from insided import __version__


class ApiHelper(object):
    # HTTP METHOD CONSTANTS
    HTTP_DELETE = 'delete'
    HTTP_GET = 'get'
    HTTP_POST = 'post'
    HTTP_PUT = 'put'

    DEFAULT_API_SCOPES = 'write read'
    PAGE_PARAM = 'page'
    PAGE_SIZE_PARAM = 'pageSize'
    FILTER_PARAM = 'filter'

    # URL CONSTANTS
    BASE_URL = 'https://api2-us-west-2.insided.com'

    def __init__(self, client_id=None, client_secret=None, access_token=None, user_agent=None, scopes=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = access_token
        self.scopes = scopes or self.DEFAULT_API_SCOPES
        self.user_agent = user_agent or 'InsidedPythonSDK/{}'.format(__version__)

    def _request(self, path, params=None, headers={}, data=None, json=None, is_oauth=False, method=HTTP_GET):
        """

        Args:
            path:
            params:
            headers:
            data:
            json:
            is_oauth:
            method:

        Returns:
            (Response)
        """
        url = '{}{}'.format(self.BASE_URL, path)
        headers = self._build_headers(headers, is_oauth)
        return getattr(requests, method.lower())(
            url=url,
            params=params,
            headers=headers,
            data=data,
            json=json
        )

    def _build_headers(self, headers, is_oauth=False):
        """Dynamically generates headers based on specific request.

        Args:
            headers (dict):
            is_oauth (bool): True if we should use form encoding for oauth.

        Returns:
            (dict):
        """
        headers['User-Agent'] = self.user_agent

        if is_oauth:
            headers.update({
                'Content-Type': 'application/x-www-form-urlencoded'
            })
        else:
            headers.update({
                'Authorization': 'Bearer {}'.format(self.access_token),
            })

        return headers


