#!/usr/bin/python3
"""
3. Count
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """List containing the titles of all hot articles for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    res = requests.get(url, headers={'User-Agent': 'AngentMEGO'},
                       params={'after': after})

    if after is None:
        return hot_list

    if res.status_code == 200:
        res = res.json()
        after = res.get('data').get('after')
        hots = res.get('data').get('children')
        hot_list += list(map(lambda elm: elm.get('data').get('title'), hots))
        return recurse(subreddit, hot_list, after)
    return None


def count_words(subreddit, word_list):
    """
    parses the title of all hot articles, and prints a sorted count of
    given keywords
    """
    dict_word = {}
    word_list = list(map(lambda word: word.lower(), word_list))

    for word in word_list:
        dict_word[word] = 0
    titles = recurse(subreddit, [])
    titles = (' '.join(titles)).lower()
    titles = titles.split(" ")

    for word in word_list:
        dict_word[word] += titles.count(word)

    print(dict_word)
