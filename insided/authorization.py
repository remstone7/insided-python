from .api_helper import ApiHelper


class Authorization(ApiHelper):
    # AUTHENTICATION CONSTANTS
    CLIENT_CREDENTIALS_PARAM = 'client_credentials'
    CLIENT_ID_PARAM = 'client_id'
    CLIENT_SECRET_PARAM = 'client_secret'
    GRANT_TYPE_PARAM = 'grant_type'
    SCOPE_PARAM = 'scope'

    OAUTH_URL = '/oauth2/token'

    def get_access_token(self):
        """Generates an access token to be used for all requests.

        Args:
            scopes (str): Specific scopes the returned token should have.

        Returns:
            (dict): containing the access_token key.
        """
        data = {
            self.GRANT_TYPE_PARAM: self.CLIENT_CREDENTIALS_PARAM,
            self.CLIENT_ID_PARAM: self.client_id,
            self.CLIENT_SECRET_PARAM: self.client_secret,
            self.SCOPE_PARAM: self.scopes,
        }

        return self._request(self.OAUTH_URL, data=data, is_oauth=True, method=self.HTTP_POST)