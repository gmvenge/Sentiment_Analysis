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





