import requests
from requests.auth import HTTPBasicAuth
import json
import utilities as utils

config = utils.read_config()
ISD_api_token = config.get('ISD_api_token')
notification_url = "https://your-domain.atlassian.net/rest/api/3/notificationscheme"
username = config.get('username')
auth = HTTPBasicAuth(username, ISD_api_token)


def ISD_api_function(url, page_size=10):
    """Get the response from ISD API.
    :param str url: URL of the API.
    :param int page_size: Number of issues to get per request.
    :return: Response from the API.
    :rtype: requests.models.Response
    """
    params = {
        'maxResults': page_size,
        'startAt': 0
    }
    response = requests.get(url, params=params, auth=auth)
    return response
