## Python SDK for InSided Community Forum

### Installation
```bash
pip install insided
```

### Configuration

```bash
from insided import Insided

insided_api = Insided(INSIDED_CLIENT_ID, INSIDED_SECRET)
response = insided_api.Authorization.get_access_token()  # fetch an access token
insided_api.access_token = response.data['access_token'] # store it here
```

### Response Object

The api returns an `InsidedResponse` containing a `data`, `status_code`, and the actual `response` attribute.

### Using the API

#### Webhooks
```bash
insided_api.Webhooks.create_webhook(webhook_name, webhook_response_url)
insided_api.Webhooks.get_webhooks()
```

#### Users
defauls for page is 1 and page_size is 10
```bash
insided_api.Users.get_users(page, page_size) # fetches list of all users
insided_api.Users.create_user(email, password, username=None) # create a user
insided_api.Users.get_user_by_id(user_id) # get user by user_id

insided_api.Users.get_user_activity(page, page_size, api_filter=None) # get's user activity
insided_api.Users.delete_user(user_id) # Removes a user
insided_api.Users.add_user_role(user_id, role=[]) # adds a role to a user

insided_api.Users.get_user_by_field(field, value) # Gets a user by field and value
insided_api.Users.update_user_field_profile(user_id, field, value) # updates the user field
insided_api.Users.delete_user_profile_field(user_id, field) # removes user field.

insided_api.Users.user_logout(field, value) # remote logout a user.
insided_api.Users.update_user_badge(user_id, badge_id) # adds a badge to a user.
insided_api.Users.remove_user_badge(user_id, badge_id) # removes a badge a user.

insided_api.Users.get_badges(page, page_size) # fetches a list of badges.
insided_api.Users.delete_badge(badge_id) # removes a badge.
```

#### Gamification
defauls for page is 1 and page_size is 25

```bash
insided_api.Gamification.get_leaderboard(excluded, page, page_size) # get overall leaderboard.
insided_api.Gamification.get_weekly_leaderbaord(excluded, page, page_size) # weekly leaderboard.
insided_api.Gamification.assign_points(user_id, points) # assign point to user.
insided_api.Gamification.get_points(user_ids, earned_from=None, earned_at=None) # get a list of points for users.
```

#### Contribution
Feel free to make a PR, will be adding tests soon.