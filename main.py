from instafollower import InstaFollower

EMAIL =''
PASSWORD = ''
followers_account = ''
insta_bot = InstaFollower()
# Open the instagram page and login to account
insta_bot.instagram_login(PASSWORD,EMAIL)

#  Go to a specific Account in instagram and find his followers and follow them
insta_bot.find_followers(followers_account)
