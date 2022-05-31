#!/usr/bin/python3
"""
2. Recurse it!
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """List containing the titles of all hot articles for a given subreddit"""
    api_url = 'https://www.reddit.com'

    res = requests.get(f'{api_url}/r/{subreddit}/hot.json',
                       headers={'user-agent': 'ineffale'},
                       params={'after': after})

    if after is None:
        return hot_list

    if res.status_code == 200:
        res = res.json()
        after = res.get('data').get('after')
        hots = res.get('data').get('children')
        hot_list += list(map(lambda elm: elm.get('data').get('title'), hots))
        return recurse(subreddit, hot_list, after)
    else:
        return None
