__author__ = 'arya'
from pprint import pprint
from pysnap import Snapchat
from secrets import snapchat_password,snapchat_username


s = Snapchat()
s.login(snapchat_username, snapchat_password)
snaps = s.get_snaps()
pprint(snaps)