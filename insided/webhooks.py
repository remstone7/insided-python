from .api_helper import ApiHelper

class Webhooks(ApiHelper):
    WEBHOOKS_URL = '/v2/webhooks'
    WEBHOOK_SUBSCRIBE_URL = WEBHOOKS_URL + '/{}/subscriptions'

    def create_webhook(self, webhook_name, webhook_response_url):
        """Generates a webhook for an action.

        Available webhook_names found here: https://api2-us-west-2.insided.com/docs/#section/Webhooks/Available-events

        Args:
            webhook_name (str): Name of the actual event.
            webhook_response_url (str): Name of the url Insided should send a webhook too.

        Returns:

        """
        data = {
            'url': webhook_response_url,
            'username': self.client_id,
            'secret': self.client_secret
        }

        self._request(self.WEBHOOK_SUBSCRIBE_URL.format(webhook_name), json=data, method=self.HTTP_POST)

    def get_webhooks(self):
        """Returns a list of all subscribed webhooks."""
        return self._request(self.WEBHOOKS_URL)
