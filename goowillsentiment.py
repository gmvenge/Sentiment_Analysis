#Welcome and lets start by calling the twitter api
#
import twitter
api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)

#Getting user_Timeline
ScreenName = "gmvenge"
UserTimeline = api.GetUserTimeline(screen_name = ScreenName)

#pass the screen name of the user to the GetUserTimeline function 
#it returns a JSON formatted data which contains Tweets, Retweet Count, Like Count, Hashtags, User Mentions

[
  {
    "created_at": "Sat Mar 24 16:24:43 +0000 2018",
    "id": 850007368138018817,
    "id_str": "850007368138018817",
    "text": "RT @TwitterDev: 1/ Today we’re sharing our vision for the future of the Twitter API platform!\nhttps://t.co/XweGngmxlP",
    "truncated": false,
    "entities": {
      "hashtags": [],
      "symbols": [],
      "user_mentions": [
        {
          "screen_name": "TwitterDev",
          "name": "TwitterDev",
          "id": 2244994945,
          "id_str": "2244994945",
          "indices": [
            3,
            14
          ]
        }
      ],
      .
      .
      .
      .
      .
      .
   }
]

# parse the result using JSON library in Python
ScreenName = "gmvenge"
Friends = GetFriends(screen_name = ScreenName)
Followers = GetFollowers(screen_name = ScreenName)
"users": [
    {
      "profile_sidebar_fill_color": "252429",
      "profile_sidebar_border_color": "181A1E",
      "profile_background_tile": false,
      "name": "Ezekiel Munyawiri",
      "profile_image_url": "http://a0.twimg.com/profile_images/2838630046/4b82e286a659fae310012520f4f756bb_normal.png",
      "created_at": "Thu Jan 18 00:10:45 +0000 2012",
      "location": "Harare",
      "follow_request_sent": false,
      "profile_link_color": "2FC2EF",
      "is_translator": false,
      "id_str": "657693",
      "default_profile": false,
      "contributors_enabled": true,
      "favourites_count": 1973,
      "url": "http://afroginthevalley.com/",
      "profile_banner_url": "https://si0.twimg.com/profile_banners/657693/1353537845",
      "profile_image_url_https": "https://si0.twimg.com/profile_images/2838630046/4b82e286a659fae310012520f4f756bb_normal.png",
      "utc_offset": -18000,
      "id": 657693,
      "profile_use_background_image": true,
      "listed_count": 324,
      "profile_text_color": "666666",
      "lang": "en",
      "followers_count": 4993,
      "protected": false,
      "notifications": false,
      "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme9/bg.gif",
      "profile_background_color": "1A1B1F",
      "verified": false,
      "geo_enabled": true,
      "time_zone": "GMT+2 ",
      "description": "Banking Specialist at Twitter.\r\n\r\nInternet, opensource, media & geo/local geek.\r\n\r\nFollow @ezekiel for LANG=FR.",
      "default_profile_image": false,
      "profile_background_image_url": "http://a0.twimg.com/images/themes/theme9/bg.gif",
      "statuses_count": 8504,
      "friends_count": 2743,
      "following": true,
      "screen_name": "ambassador_muntony"
    }
]    

   #Thank you!



