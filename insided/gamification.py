from .api_helper import ApiHelper

class Gamification(ApiHelper):
    EXCLUDED_PARAM = 'excluded'

    LEADERBOARD_URL = '/leaderboard'
    LEADERBOARD_WEEKLY_URL = '{}/weekly'.format(LEADERBOARD_URL)
    POINTS_URL = '/points'
    POINTS_ASSIGN_URL = '/{}/assign'.format(POINTS_URL)

    DEFAULT_STARTING_PAGE = 1
    DEFAULT_PAGE_SIZE = 25

    def get_leaderboard(self, excluded, page=DEFAULT_STARTING_PAGE, page_size=DEFAULT_PAGE_SIZE):
        """Fetches a paginated list of users sorted by ascending order of all time points earned.

        Args:
            excluded (list): Muliple user roles can be provided with comma separated strings. Use roles.banned,roles.moderator for testing.
            page (int): Page number pagination starts from.
            page_size (int): Number of results returned in paginated list.

        Returns:
            (InsidedResponse): List of users.
        """
        params = {
            self.EXCLUDED_PARAM: excluded,
            self.PAGE_PARAM: page,
            self.PAGE_SIZE_PARAM: page_size
        }

        return self._request(self.LEADERBOARD_URL, params=params)


    def get_weekly_leaderbaord(self, excluded, page=DEFAULT_STARTING_PAGE, page_size=DEFAULT_PAGE_SIZE):
        """Fetches a paginated list of users sorted by ascending order of points earned this week.

        'This week' is a fixed 7 day time period (Monday-Sunday), rather than a rolling 7 day period.
        This is reset based on the value of timezone chosen when the point system is configured in the control environment.

        Args:
            excluded (list): Muliple user roles can be provided with comma separated strings. Use roles.banned,roles.moderator for testing.
            page (int): Page number pagination starts from.
            page_size (int): Number of results returned in paginated list.

        Returns:
            (InsidedResponse): List of users.
        """
        params = {
           self.EXCLUDED_PARAM: excluded,
           self.PAGE_PARAM: page,
           self.PAGE_SIZE_PARAM: page_size
        }

        return self._request(self.LEADERBOARD_WEEKLY_URL, params=params)

    def assign_points(self, user_id, points):
        """Assign points to a single user by UserId.

        Args:
            user_id (int): Unique User ID.
            points (int): Amount of points to assign.

        Returns:
            (InsidedResponse): 204 status code if successful.
        """
        data = {
            'user': user_id,
            'points': points
        }
        return self._request(self.POINTS_ASSIGN_URL, json=data, method=self.HTTP_POST)

    def get_points(self, user_ids, earned_from=None, earned_at=None):
        """Get points assigned to users in a timeframe.

        Args:
            user_ids (list): Unique User ID's.
            earned_from (str): Starting value for a timeframe. Uses beginning of unix time as default.
            earned_at (str): Ending value for a timeframe. Uses current time as a default.

        Returns:
            (InsidedResponse): List of users with total points assigned.
        """
        params = {
            'userId[]': user_ids,
            'earnedAt[from]': earned_from,
            'earnedAt[to]': earned_at
        }
        return self._request(self.POINTS_URL, params=params)