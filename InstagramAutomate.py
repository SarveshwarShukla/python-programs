# Automating instagram using instabot
# Sarveshwar Shukla (19 March 2022)

from instabot import Bot

bot = Bot()
username_instagram = "test_username"
password_instagram = "abcdefgh"
bot .login(username=username_instagram, password=password_instagram)

# Automating the follow of the passed username account
bot.follow("sandeep__maheshwari")

# Uploading Photo
bot.upload_photo("Path to photo", caption="Image Caption")

# Unfollowing user
bot.unfollow("hello__world")

# Automatting messages
bot.send_message("Messaging", ["username1", "username2", "..etc"])

# getting info about followers
followers = bot.get_user_followers("main-username")
for follower in followers:
    print(bot.get_user_info(follower))
    
# getting info about followings
followings = bot.get_user_following("main-username")
for following in followings:
    print(bot.get_user_info(following))
