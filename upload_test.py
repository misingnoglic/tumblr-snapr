#from __future__ import unicode_literals
__author__ = 'arya'

from tumblpy import Tumblpy
from secrets import tumblr_oauth_key , tumblr_secret_key, tumblr_token, tumblr_token_secret


t = Tumblpy( tumblr_oauth_key, tumblr_secret_key, tumblr_token, tumblr_token_secret)

blog_url = t.post('user/info')
blog_url = blog_url['user']['blogs'][0]['url']

photo = open('content/image.jpg')

post = t.post('post', blog_url=blog_url, params={'type':'photo', 'caption': 'Test Caption', 'data': photo, 'tags':"stuff"})
print post  # returns id if posted successfully