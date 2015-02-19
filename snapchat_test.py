__author__ = 'arya'
from secrets import snapchat_password,snapchat_username
from snapchat_bots import SnapchatBot
import shutil

from tumblpy import Tumblpy
from secrets import tumblr_oauth_key , tumblr_secret_key, tumblr_token, tumblr_token_secret


class ReflectorBot(SnapchatBot):
    # when receiving a snap, sends the same snap back to the sender
    def on_snap(self, sender, snap):
        t = Tumblpy( tumblr_oauth_key, tumblr_secret_key, tumblr_token, tumblr_token_secret)
        blog_url = t.post('user/info')
        blog_url = blog_url['user']['blogs'][0]['url']
        post = t.post('post', blog_url=blog_url, params={'type':'photo', 'caption': 'Submitted photo via snapchat, send a snapchat to tumblr-snapr to have your photo anonymously submitted too!', 'data': snap.file, 'tags':"kik, snapchat, auto-snapr, tumblr-snapr"})
        print ("\a")
        #print "Snapchat sent from" + snap.username

        self.send_snap([sender], snap)

    # when someone adds the bot, the bot adds them back
    def on_friend_add(self, friend):
        #self.add_friend(self, friend)
        pass

    # when someone deletes the bot, the bot deletes them too
    def on_friend_delete(self, friend):
        #self.delete_friend(self, friend)
        pass

bot = ReflectorBot(snapchat_username,snapchat_password)
bot.listen()