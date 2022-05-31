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
        res = res.json()
        after = res.get('data').get('after')
        hots = res.get('data').get('children')
        for hot in hots:
            hot_list.append(hot.get('data').get('title'))
        return recurse(subreddit, hot_list, after)
    else:
        return None
