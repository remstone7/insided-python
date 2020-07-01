import requests

from insided import __version__


class InsidedResponse(object):
    def __init__(self, data, status_code, response):
        self.data = data
        self.status_code = status_code
        self.response = response


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
        """Makes an HTTP request to the insided api.

        Args:
            path (str): The ending pathname.
            params (dict): Query parameters.
            headers (dict): HTTP Headers for the request.
            data (dict): Information to be passed into the body.
            json (dict): Information to be passed into the body as json.
            is_oauth (bool): Authentication request or not.
            method (str): HTTP method.

        Returns:
            (InsidedResponse): Information from the HTTP Response
        """
        url = '{}{}'.format(self.BASE_URL, path)
        headers = self._build_headers(headers, is_oauth)
        response = getattr(requests, method.lower())(
            url=url,
            params=params,
            headers=headers,
            data=data,
            json=json
        )
        return self._build_response(response)

    def _build_response(self, response):
        """Creates a response object.

        Args:
            response (Response): HTTP response from api.

        Returns:
            (InsidedResponse): Information containing the response.
        """
        if response.status_code in (202, 204,):
            data = response.text
        else:
            data = response.json()

        return InsidedResponse(
            data,
            response.status_code,
            response
        )

    def _build_headers(self, headers, is_oauth=False):
        """Dynamically generates headers based on specific request.

        Args:
            headers (dict):
            is_oauth (bool): True if we should use form encoding for oauth.

        Returns:
            (dict): Headers
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


