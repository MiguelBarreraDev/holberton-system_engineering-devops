#!/usr/bin/python3
"""
2. Recurse it!
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """List containing the titles of all hot articles for a given subreddit"""
    api_url = 'https://www.reddit.com'

    meta_data = {
        'headers': {
            'user-agent': 'Mozilla/5.0'
        },
        'allow_redirects': False,
        'params': {'after': after}
    }
    res = requests.get(f'{api_url}/r/{subreddit}/hot.json', **meta_data)

    if after is None:
        return hot_list

    if res.status_code == 200:
        after = res.json().get('data').get('after')
        hot_list += res.json().get('data').get('children')
        return recurse(subreddit, hot_list, after)
    else:
        return None
